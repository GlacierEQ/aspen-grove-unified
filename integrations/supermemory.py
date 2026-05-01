"""APEX Supermemory Integration
Enforces 7 memory classes and provides read/write to Supermemory API.
"""
import os
import requests
from datetime import datetime
from typing import Literal, Dict, Any, Optional, List

SUPERMEMORY_BASE = "https://api.supermemory.ai/v1"

MemoryClass = Literal[
    "identity",
    "operator_preferences",
    "repo_knowledge",
    "case_knowledge",
    "document_knowledge",
    "failure_patterns",
    "decision_history",
]


class SupermemoryClient:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.environ["SUPERMEMORY_API_KEY"]
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    # ── WRITE ──────────────────────────────────────────────────────────────
    def write(
        self,
        memory_class: MemoryClass,
        content: str,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        payload = {
            "class": memory_class,
            "content": content,
            "metadata": {
                **(metadata or {}),
                "written_at": datetime.utcnow().isoformat(),
                "source": "aspen-grove-unified",
            },
        }
        r = requests.post(f"{SUPERMEMORY_BASE}/memories", headers=self.headers, json=payload)
        r.raise_for_status()
        return r.json()

    # ── RETRIEVE ───────────────────────────────────────────────────────────
    def retrieve(
        self,
        query: str,
        memory_class: Optional[MemoryClass] = None,
        limit: int = 10,
    ) -> List[Dict[str, Any]]:
        params = {"query": query, "limit": limit}
        if memory_class:
            params["class"] = memory_class
        r = requests.get(f"{SUPERMEMORY_BASE}/memories/search", headers=self.headers, params=params)
        r.raise_for_status()
        return r.json().get("results", [])

    # ── CONVENIENCE WRITERS ────────────────────────────────────────────────
    def write_repo_knowledge(self, repo: str, commit: str, summary: str, diff_stat: str):
        return self.write(
            "repo_knowledge",
            f"Repository: {repo}\nCommit: {commit}\nSummary: {summary}\nChanges: {diff_stat}",
            {"repo": repo, "commit": commit},
        )

    def write_failure_pattern(self, incident_id: str, message: str, fix: str, prevention: str):
        return self.write(
            "failure_patterns",
            f"Incident: {message}\nFix Applied: {fix}\nPrevention: {prevention}",
            {"incident_id": incident_id},
        )

    def write_case_knowledge(self, case_id: str, fact: str, source: str):
        return self.write(
            "case_knowledge",
            f"Case: {case_id}\nFact: {fact}\nSource: {source}",
            {"case_id": case_id},
        )

    def write_decision(self, decision: str, rationale: str, context: Dict[str, Any]):
        return self.write(
            "decision_history",
            f"Decision: {decision}\nRationale: {rationale}",
            context,
        )

    def write_document_knowledge(self, doc_id: str, title: str, key_clauses: List[str]):
        return self.write(
            "document_knowledge",
            f"Document: {title}\nKey clauses:\n" + "\n".join(f"- {c}" for c in key_clauses),
            {"doc_id": doc_id},
        )


if __name__ == "__main__":
    client = SupermemoryClient()
    print("Supermemory client ready.")
    # Quick write test
    result = client.write_repo_knowledge(
        repo="GlacierEQ/aspen-grove-unified",
        commit="HEAD",
        summary="APEX pipeline integration modules added",
        diff_stat="+350 -0 across 3 files",
    )
    print(f"Memory written: {result}")
