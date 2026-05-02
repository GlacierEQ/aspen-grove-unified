# AGENTS.md

## Purpose

This repository is the control plane for the Aspen Grove family.

It exists to:
- define canonical roles across Aspen repositories
- coordinate agent behavior and repo boundaries
- prevent duplicate implementation work
- standardize contracts between memory, fusion, bridge, and audit layers
- keep legal/case-oriented data pipelines structured and reviewable

---

## Canonical Aspen Roles

### 1. aspen-grove-operator-v7
Role: canonical-core

Responsibilities:
- memory capture
- normalization of source events
- evidence/actor/event graph primitives
- deduplication and audit trace
- packet input generation

### 2. aspen-grove-unified
Role: public-front-door and family control plane

Responsibilities:
- architecture docs
- repo registry
- manifests and scorecards
- family-level planning artifacts
- shared agent rules and contracts

### 3. aspen-grove-apex-fusion
Role: reconciliation engine

Responsibilities:
- resolve duplicates and source conflicts
- apply source precedence rules
- compile packets from normalized records
- produce contradiction and staleness reports

### 4. aspen-grove-omni-bridge
Role: connector bridge

Responsibilities:
- adapter layer for Drive, Notion, GitHub, ClickUp, Dropbox, and related systems
- source event normalization
- retry handling
- sync auditing

### 5. aspen-grove-resource-analysis
Role: audit and maturity analysis

Responsibilities:
- repo maturity scoring
- duplication detection
- connector utilization reporting
- workflow health analysis

### 6. aspen-grove-quantum-transcendence
Role: research lab

Responsibilities:
- experiments only
- ranking, clustering, and contradiction-scoring prototypes
- candidate promotion ideas for core repos

### 7. integration / second / third Aspen repos
Role: migration-candidate

Responsibilities:
- temporary holding area only until classified
- extraction of unique working code
- merge or archive decisions

---

## Agent Classes

### Control Agent
Primary repo: aspen-grove-unified

Duties:
- maintain manifest integrity
- update family maps and roadmaps
- track canonical vs deprecated repos
- publish scorecards and decision records

### Core Memory Agent
Primary repo: aspen-grove-operator-v7

Duties:
- implement typed records
- maintain evidence/event/actor ingestion
- enforce confidence and pleading-safety metadata
- preserve auditability

### Fusion Agent
Primary repo: aspen-grove-apex-fusion

Duties:
- merge normalized records
- detect conflicts
- emit resolved outputs and packet bundles

### Bridge Agent
Primary repo: aspen-grove-omni-bridge

Duties:
- implement connector adapters
- normalize external source payloads
- maintain retry and dead-letter handling

### Audit Agent
Primary repo: aspen-grove-resource-analysis

Duties:
- score repos
- surface entropy and overlap
- detect stale workflows and weak documentation

### Research Agent
Primary repo: aspen-grove-quantum-transcendence

Duties:
- prototype only
- document inputs, outputs, and failure modes
- propose promotable patterns

---

## Shared Data Contract

All Aspen repos should converge on the following shared entity families:
- Actor
n- Evidence
- Event
- Violation
- Authority
- Packet
- Task
- Source
- System

Required common fields:
- id
- type
- title
- summary
- source_refs
- actor_refs
- event_refs
- violation_refs
- confidence
- pleading_safe
- source_verified
- created_at
- updated_at

Additional recommended control fields:
- case_id
- jurisdiction
- tags
- ingest_path
- derived_from
- supersedes
- contradiction_refs
- review_status

---

## Operational Rules

1. Do not add shared schema definitions to experimental repos first unless clearly marked experimental.
2. Do not duplicate connector logic across multiple Aspen repos unless a migration is actively underway.
3. Do not treat README ambition as implementation truth. Prefer code and workflow evidence.
4. Do not mark a record pleading-safe unless source_verified is true and review has passed.
5. Do not mix canonical production logic with speculative research code.
6. Do not create new Aspen repos when an existing canonical repo can absorb the work.
7. Every major cross-repo change should be reflected in the manifest and planning docs.

---

## Merge / Archive Policy

A migration-candidate repo must end in one of three states:
- merged into canonical repo
- retained for one narrow justified purpose
- archived after extraction of unique assets

No repo should remain indefinitely in an ambiguous state.

---

## Preferred Build Order

### Phase 1
- aspen-grove-operator-v7
- aspen-grove-unified
- aspen-grove-apex-fusion

### Phase 2
- aspen-grove-omni-bridge
- aspen-grove-resource-analysis

### Phase 3
- migration-candidate repos
- research repo promotion review

---

## Definition of Done for Aspen Work

A unit of Aspen work is considered complete when:
- canonical target repo is identified
- schema impact is documented
- implementation exists in code or executable artifact form
- failure modes are noted
- manifest and plan docs are updated
- duplication risk is assessed
- the output can be traced to its owning repo and agent class
