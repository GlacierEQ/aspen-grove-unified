#!/usr/bin/env bash
# =============================================================================
# APEX Daily 06:05 HST Cron Runner
# Case: 1FDV-23-0001009
# Crontab entry: 5 6 * * * /path/to/aspen-grove-unified/scripts/apex_daily_cron.sh
# =============================================================================
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.."; pwd)"
OUTPUT_DIR="$REPO_ROOT/output"
DATE=$(date -u +%Y-%m-%d)
LOG="$OUTPUT_DIR/daily_$DATE.log"

mkdir -p "$OUTPUT_DIR"

echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] 🔱 APEX DAILY CYCLE START — $DATE" | tee "$LOG"

# Phase 0-4 via single message to APEX-Casey
letta message "APEX-Casey" \
"Execute full daily protocol now:
- PHASE 0: Citation integrity check (JSON)
- PHASE 1: Evidence triage from Supabase (JSON)
- PHASE 2: Deadline surveillance from Notion (sorted table)
- PHASE 3: Generate today's APEX Tactical Plan
- PHASE 4: Write output to output/tactical-plan.json
Date: $DATE
Case: 1FDV-23-0001009
Thread: APEX-PPLX-SUPERTHREAD-∞" \
  2>&1 | tee -a "$LOG"

echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] 🔱 APEX DAILY CYCLE COMPLETE" | tee -a "$LOG"
