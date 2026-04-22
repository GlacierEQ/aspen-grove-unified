# 🔱 APEX-Casey v1.0.0

**Agent:** APEX-Casey (Letta)  
**Thread:** APEX-PPLX-SUPERTHREAD-∞  
**Case:** 1FDV-23-0001009  
**Operator:** Casey Barton | GlacierEQ  
**Deployed:** 2026-04-22  

---

## Mission

Reunification of Casey Barton with his son **Kekoa Barton**.  
Federal escalation via RICO / 42 U.S.C. § 1983 is **always active**.

---

## Architecture

```
aspen-grove-unified/
├── prompts/
│   └── apex_system_prompt.md     ← APEX-Casey system prompt (v1.0.0)
├── scripts/
│   ├── register_apex_casey.sh    ← One-time Letta agent registration
│   └── apex_daily_cron.sh        ← 06:05 HST daily automation runner
├── templates/
│   └── motion_template.md        ← Court-ready motion scaffold
└── output/
    └── tactical-plan.json        ← Written each morning by APEX-Casey
```

---

## Deployment

### Step 1 — Install Letta
```bash
pip install letta
letta server start  # or use Letta Cloud
```

### Step 2 — Register APEX-Casey
```bash
chmod +x scripts/register_apex_casey.sh
./scripts/register_apex_casey.sh
```

### Step 3 — Set Daily Cron (06:05 HST = 16:05 UTC)
```bash
crontab -e
# Add:
5 16 * * * /path/to/aspen-grove-unified/scripts/apex_daily_cron.sh
```

### Step 4 — Verify
```bash
letta list agents
letta message "APEX-Casey" "Status check. Report current stage and next deadline."
```

---

## APEX Axiom (10 Laws)

1. Never summarize — actionable steps only  
2. Every legal claim cites authority  
3. Every factual claim cites an exhibit  
4. Federal escalation always active  
5. Kekoa's best interests are the anchor (HRS § 571-46)  
6. Chain of custody is sacred (sha256 + FRE 901)  
7. No deference to prior adverse rulings (HRCP 60(b))  
8. Judicial misconduct is documented, not tolerated  
9. Deadlines are non-negotiable (48hr rule)  
10. **Reunification is the only win condition**  

---

## Federal Escalation Pipeline

| Stage | Status | Action |
|-------|--------|--------|
| 1 — State Record Building | **CURRENT** | Document violations, exhaust remedies |
| 2 — § 1983 Complaint | Pending | Color of law mapping, QI defeat |
| 3 — RICO Pattern | Pending | Enterprise + predicate acts |
| 4 — 9th Circuit Mandamus | Standby | Emergency petition ready |

---

## Connector Priority

| Connector | Role | Priority |
|-----------|------|----------|
| Notion MCP | Case dashboard, evidence DB | P0 |
| Perplexity MCP | Citation integrity, law research | P0 |
| Supabase | Exhibits, pgvector, transcripts | P0 |
| GitHub | Templates, snapshots | P1 |
| Filesystem | Audio, PDFs, raw exhibits | P1 |
| Sentry | Observability | P2 |
