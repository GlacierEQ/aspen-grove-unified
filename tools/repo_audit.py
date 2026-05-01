#!/usr/bin/env python3
"""Aspen Grove family audit utility.

This script scores Aspen Grove repos by maturity and identifies likely merge/
archive candidates. It is intentionally dependency-light so it can run in CI or
locally with only the standard library.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
import json
from typing import List, Dict, Any


@dataclass
class RepoScore:
    repo: str
    role: str
    status: str
    priority: int
    documentation_score: int
    implementation_score: int
    workflow_score: int
    duplication_risk: int
    canonicality_score: int
    total_score: int
    recommendation: str


def load_manifest(path: Path) -> Dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    # very light YAML-ish parser for the current manifest format
    # to avoid external dependencies in the first scaffold version.
    lines = [line.rstrip() for line in text.splitlines() if line.strip()]
    repos: List[Dict[str, Any]] = []
    current: Dict[str, Any] | None = None
    in_repos = False
    for line in lines:
        if line.startswith("repos:"):
            in_repos = True
            continue
        if not in_repos:
            continue
        if line.startswith("rules:"):
            break
        if line.startswith("  - repo:"):
            if current:
                repos.append(current)
            current = {"repo": line.split(":", 1)[1].strip()}
            continue
        if current and line.startswith("    ") and ":" in line:
            k, v = line.strip().split(":", 1)
            current[k.strip()] = v.strip()
    if current:
        repos.append(current)
    return {"repos": repos}


def score_repo(repo_meta: Dict[str, Any]) -> RepoScore:
    repo = repo_meta.get("repo", "unknown")
    role = repo_meta.get("role", "unknown")
    status = repo_meta.get("status", "unknown")
    priority = int(repo_meta.get("priority", 999))

    documentation_score = 4 if role in {"canonical-core", "public-front-door"} else 2
    implementation_score = 5 if role == "canonical-core" else 3 if role in {"reconciliation-engine", "connector-bridge"} else 1
    workflow_score = 4 if role in {"canonical-core", "connector-bridge", "reconciliation-engine"} else 2
    duplication_risk = 5 if role == "migration-candidate" else 2
    canonicality_score = 5 if role == "canonical-core" else 3 if role in {"public-front-door", "reconciliation-engine", "connector-bridge"} else 1

    total_score = documentation_score + implementation_score + workflow_score + canonicality_score - duplication_risk

    if role == "migration-candidate":
        recommendation = "merge-or-archive"
    elif role == "research-lab":
        recommendation = "retain-as-experimental"
    elif total_score >= 14:
        recommendation = "expand-now"
    else:
        recommendation = "stabilize-and-clarify"

    return RepoScore(
        repo=repo,
        role=role,
        status=status,
        priority=priority,
        documentation_score=documentation_score,
        implementation_score=implementation_score,
        workflow_score=workflow_score,
        duplication_risk=duplication_risk,
        canonicality_score=canonicality_score,
        total_score=total_score,
        recommendation=recommendation,
    )


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    manifest_path = root / "repos" / "manifest.yaml"
    data = load_manifest(manifest_path)
    scores = [score_repo(repo_meta) for repo_meta in data["repos"]]
    scores.sort(key=lambda x: (x.priority, -x.total_score))

    output_dir = root / "reports"
    output_dir.mkdir(exist_ok=True)
    out_path = output_dir / "repo_scorecard.json"
    out_path.write_text(json.dumps([asdict(s) for s in scores], indent=2), encoding="utf-8")

    print(f"Wrote scorecard to {out_path}")
    for score in scores:
        print(f"[{score.recommendation}] {score.repo} :: total={score.total_score}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
