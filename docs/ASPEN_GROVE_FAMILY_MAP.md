# Aspen Grove Family Map

## Canonical Core

- `GlacierEQ/aspen-grove-operator-v7`
  - Primary Aspen memory substrate
  - Owns memory capture, routing, dedupe, sink fan-out, audit, and legal-graph primitives

## Fusion / Wrapper Layer

- `GlacierEQ/aspen-grove-unified`
  - Public front door / documentation / release surface
- `GlacierEQ/aspen-grove-apex-fusion`
  - Cross-system reconciliation and packet compiler target
- `GlacierEQ/aspen-grove-omni-bridge`
  - Connector bridge layer for cloud, repo, and case-system sync

## Research / Experimental Layer

- `GlacierEQ/aspen-grove-quantum-transcendence`
  - Experimental ranking, clustering, contradiction scoring, and narrative synthesis

## Resource / Audit Layer

- `GlacierEQ/aspen-grove-resource-analysis`
  - Inventory, maturity scoring, duplication detection, and system health registry

## Migration / Archive Candidates

- `GlacierEQ/aspen-grove-integration-project`
- `GlacierEQ/second-aspen-grove-integration`
- `GlacierEQ/third-aspen-grove-project`

These should be explicitly classified as one of:
- merged into a canonical repo
- retained for a single narrow purpose
- archived after extraction of unique assets

---

# Build Order

## Phase 1 — Stabilize the Core
1. `aspen-grove-operator-v7`
2. `aspen-grove-unified`
3. `aspen-grove-apex-fusion`

## Phase 2 — Standardize Ingestion + Bridges
4. `aspen-grove-omni-bridge`
5. `aspen-grove-resource-analysis`

## Phase 3 — Reduce Entropy
6. `aspen-grove-integration-project`
7. `second-aspen-grove-integration`
8. `third-aspen-grove-project`
9. `aspen-grove-quantum-transcendence` as research-only unless promoted

---

# Required Shared Schema

Every Aspen Grove component should converge on the same object model:

- `Actor`
- `Evidence`
- `Event`
- `Violation`
- `Authority`
- `Packet`
- `Task`
- `Source`
- `System`

Each record should support:

- `id`
- `type`
- `title`
- `summary`
- `source_refs`
- `actor_refs`
- `event_refs`
- `violation_refs`
- `confidence`
- `pleading_safe`
- `source_verified`
- `created_at`
- `updated_at`

---

# Immediate Upgrade Targets

## aspen-grove-operator-v7
- Add typed legal graph layer
- Add actor/evidence/event relation builder
- Add confidence + pleading-safety fields
- Add case-mode overlays

## aspen-grove-unified
- Add monorepo manifest
- Add architecture portal
- Add maturity dashboard
- Add canonicality map

## aspen-grove-apex-fusion
- Add reconciliation engine
- Add source precedence rules
- Add packet compiler
- Add duplicate/staleness detector

## aspen-grove-omni-bridge
- Add standard connector adapters
- Add retry/audit layer
- Add normalized source contract

## aspen-grove-resource-analysis
- Add repo maturity scorecard
- Add duplication report
- Add workflow health inventory
- Add connector utilization map

---

# Canonical Rule

Until a stronger implementation is proven, treat `GlacierEQ/aspen-grove-operator-v7` as the canonical Aspen core and route doctrine, graph work, and shared contracts around that assumption.
