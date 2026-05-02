# PLANS.md

## Mission

Transform the Aspen Grove family from a repo constellation into a coherent, high-power legal-memory and reconciliation platform.

This plan assumes:
- `aspen-grove-operator-v7` is the canonical Aspen core
- `aspen-grove-unified` is the family control plane
- `aspen-grove-apex-fusion` becomes the reconciliation engine
- `aspen-grove-omni-bridge` becomes the connector normalization layer
- `aspen-grove-resource-analysis` becomes the scorecard/audit layer

---

## Plan A — Stabilize the Family

### Objective
Reduce ambiguity and define repo ownership clearly.

### Deliverables
- family map
- manifest
- AGENTS.md
- repo scorecard
- architecture docs
- merge/archive candidate list

### Tasks
1. Publish canonical repo map
2. Add machine-readable manifest
3. Add repo audit tooling
4. Document agent classes and operating rules
5. Score all Aspen repos and mark merge/archive candidates

### Success Criteria
- every Aspen repo has a declared role
- canonical core is explicit
- migration candidates are visible
- family-level control artifacts exist in one repo

---

## Plan B — Build the Core Graph

### Objective
Turn Aspen Grove Operator into a typed legal-memory graph rather than only a sink router.

### Deliverables
- typed entity models
- graph relation builders
- confidence and pleading-safety controls
- case-mode overlays

### Tasks
1. Define models for Actor, Evidence, Event, Violation, Authority, Packet, Source
2. Add relation builders for:
   - actor -> event
   - event -> evidence
   - evidence -> violation
   - violation -> packet
   - contradiction -> packet
3. Add `confidence`, `source_verified`, `pleading_safe`, and `review_status`
4. Add case-mode routing presets

### Success Criteria
- operator-v7 emits typed normalized records
- graph edges can be serialized consistently
- records can be filtered by pleading safety

---

## Plan C — Build Fusion

### Objective
Create a reconciler that resolves conflicts across Notion, Airtable, ClickUp, MotherDuck, GitHub, and memory sinks.

### Deliverables
- source precedence rules
- duplicate detector
- staleness detector
- packet compiler
- conflict report format

### Tasks
1. Define source precedence policy
2. Implement duplicate and conflict detection
3. Emit fused records
4. Compile packet bundles by actor, violation, contradiction, or motion lane
5. Produce machine-readable conflict reports

### Success Criteria
- multiple source records can collapse into one fused record
- disagreements are surfaced explicitly
- packet outputs are reproducible

---

## Plan D — Build Bridges

### Objective
Normalize external connectors into one event contract.

### Deliverables
- adapter contract
- retry policy
- sync audit records
- dead-letter handling

### Tasks
1. Define adapter inputs and outputs
2. Add connector-specific adapters
3. Add retry and failure classification
4. Log sync events in a uniform format

### Success Criteria
- every connector produces normalized source events
- failures are classified and recoverable
- auditability exists across bridge runs

---

## Plan E — Score and Simplify

### Objective
Continuously reduce Aspen Grove entropy.

### Deliverables
- repo maturity scorecard
- duplication report
- workflow health report
- archive recommendations

### Tasks
1. Run repo audit regularly
2. Add workflow scans and documentation coverage checks
3. Track duplicates and stale repos
4. produce merge/archive actions

### Success Criteria
- Aspen family shrinks in ambiguity over time
- repo sprawl becomes measurable
- archive candidates stop drifting indefinitely

---

## Immediate Execution Queue

### Priority 1
- build `aspen-grove-unified` control plane
- deep-scan `aspen-grove-operator-v7`
- scaffold `aspen-grove-apex-fusion`

### Priority 2
- scaffold `aspen-grove-omni-bridge`
- scaffold `aspen-grove-resource-analysis`
- create repo scorecard automation

### Priority 3
- classify and collapse migration-candidate repos
- promote proven research outputs only

---

## Risks

### 1. Repo duplication
Too many similarly named Aspen repos can hide the real implementation path.

### 2. Doctrine drift
Different repos may redefine the same contracts in slightly different ways.

### 3. Research contamination
Experimental logic may get treated as production truth without promotion review.

### 4. Legal contamination
Facts, allegations, theories, and strategies may blur if records are not typed and confidence-controlled.

---

## Required Documentation Updates per Milestone

For each major Aspen milestone, update:
- `repos/manifest.yaml`
- `docs/ASPEN_GROVE_FAMILY_MAP.md`
- `AGENTS.md`
- `PLANS.md`
- scorecard outputs

---

## Definition of Satisfaction

This plan is satisfied when:
- Aspen Grove has one obvious canonical core
- the family is machine-readable and scoreable
- reconciliation and bridge layers are real code, not only naming
- migration candidates are classified
- legal-memory outputs are typed, auditable, and pleading-safe aware
