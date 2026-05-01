# APEX Integration Modules

This directory contains the six pipeline integration connectors for **aspen-grove-unified**.

## Pipeline Topology

```
GitHub Push / PR
    │
    ▼
1️⃣  Supabase Schema Sync  ─── runs migrations, gen types, branch-per-PR
    │
    ▼
2️⃣  Vercel Deploy  ─────────── preview (PR) or production (main)
    │
    ├──▶ 3️⃣  Supabase Event Log  ── deployment record + metadata
    ├──▶ 4️⃣  Sentry Release ─────── commit-tagged release + deploy
    ├──▶ 5️⃣  Supermemory Write ──── repo_knowledge class entry
    └──▶ 6️⃣  MotherDuck ETL ──────── replicate tables + analytics views

Sentry Error  ──▶  Supabase incident_log  ──▶  GitHub Issue (auto)

On-demand:  prism_doc_gen.py  ──▶  Supabase documents  ──▶  Prism editor
```

## Files

| File | Purpose |
|------|---------|
| `supermemory.py` | Write/retrieve memory objects across 7 classes |
| `motherduck_etl.py` | Replicate Supabase → MotherDuck, build analytics views |
| `prism_doc_gen.py` | Generate court-ready LaTeX from Supabase + Supermemory |

## Required GitHub Secrets

Add these in **Settings → Secrets and variables → Actions**:

```
VERCEL_TOKEN
VERCEL_ORG_ID
VERCEL_PROJECT_ID
SUPABASE_ACCESS_TOKEN
SUPABASE_URL
SUPABASE_DB_URL
SUPABASE_PROJECT_ID
SUPABASE_ANON_KEY
SUPABASE_SERVICE_KEY
SENTRY_AUTH_TOKEN
SENTRY_ORG
SENTRY_PROJECT
SUPERMEMORY_API_KEY
MOTHERDUCK_TOKEN
```

## Memory Classes

| Class | Written by | Used by |
|-------|------------|--------|
| `identity` | Manual | All agents |
| `operator_preferences` | Manual | All agents |
| `repo_knowledge` | Phase 5 (every push) | Code agents |
| `case_knowledge` | Case event ingestion | Prism, legal agents |
| `document_knowledge` | `prism_doc_gen.py` | Future doc drafts |
| `failure_patterns` | Sentry incident resolution | Reliability agents |
| `decision_history` | Manual / decision writes | Strategy agents |
