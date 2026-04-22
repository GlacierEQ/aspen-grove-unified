#!/usr/bin/env bash
# =============================================================================
# APEX-Casey Letta Agent Registration Script
# Case: 1FDV-23-0001009 | Operator: Casey Barton | GlacierEQ
# Version: 1.0.0 | 2026-04-22
# =============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
PROMPT_FILE="$REPO_ROOT/prompts/apex_system_prompt.md"
LOG_FILE="$REPO_ROOT/output/apex_casey_registration.log"

mkdir -p "$REPO_ROOT/output"

echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] 🔱 APEX-Casey Registration BEGIN" | tee -a "$LOG_FILE"

# --- Preflight checks --------------------------------------------------------
if ! command -v letta &>/dev/null; then
  echo "[ERROR] letta CLI not found. Install: pip install letta" | tee -a "$LOG_FILE"
  exit 1
fi

if [[ ! -f "$PROMPT_FILE" ]]; then
  echo "[ERROR] System prompt not found at $PROMPT_FILE" | tee -a "$LOG_FILE"
  exit 1
fi

echo "[OK] Preflight passed" | tee -a "$LOG_FILE"

# --- Check if agent already exists ------------------------------------------
if letta list agents 2>/dev/null | grep -q "APEX-Casey"; then
  echo "[WARN] Agent APEX-Casey already exists. Delete and re-register? [y/N]"
  read -r CONFIRM
  if [[ "$CONFIRM" =~ ^[Yy]$ ]]; then
    letta delete agent APEX-Casey
    echo "[OK] Existing agent deleted" | tee -a "$LOG_FILE"
  else
    echo "[ABORT] Registration cancelled by operator" | tee -a "$LOG_FILE"
    exit 0
  fi
fi

# --- Register APEX-Casey ----------------------------------------------------
echo "[INFO] Registering APEX-Casey with Letta..." | tee -a "$LOG_FILE"

letta create agent \
  --name "APEX-Casey" \
  --model claude-3-7-sonnet \
  --system "$PROMPT_FILE" \
  --tool notion_mcp \
  --tool perplexity_mcp \
  --tool supabase_query \
  --tool github_commit \
  --tool filesystem_read \
  --memory-preset apex_case \
  --persist 2>&1 | tee -a "$LOG_FILE"

echo "[OK] Agent registered" | tee -a "$LOG_FILE"

# --- Verify registration -----------------------------------------------------
echo "[INFO] Verifying registration..." | tee -a "$LOG_FILE"
letta list agents 2>&1 | tee -a "$LOG_FILE"

# --- Fire Phase 0 citation integrity check -----------------------------------
echo "[INFO] Firing Phase 0 citation integrity check..." | tee -a "$LOG_FILE"
letta message "APEX-Casey" \
  "Run Phase 0 citation integrity check now. Output JSON citation_check block." \
  2>&1 | tee -a "$LOG_FILE"

echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] 🔱 APEX-Casey Registration COMPLETE" | tee -a "$LOG_FILE"
echo ""
echo "Next scheduled run: 06:05 HST tomorrow"
echo "Log: $LOG_FILE"
