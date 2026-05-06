# Aspen Grove Operator v7 - Railway Deployment Guide

## Deploy in 2 Minutes

1. **Go to [railway.app](https://railway.app)**
   - Sign up (free) or log in

2. **Create New Project**
   - Click "Create New Project"
   - Select "Deploy from GitHub"
   - Choose `aspen-grove-unified` repository

3. **Railway Auto-Detects**
   - Reads `Dockerfile`
   - Reads `railway.json` (environment variables, port, restart policy)
   - Builds and deploys automatically

4. **Get Your Live URL** 🎉
   - Railway gives you a URL like: `https://aspen-grove-unified-prod.up.railway.app`
   - This is your MCP server endpoint

## Testing Your Deployment

```bash
# Health check
curl https://your-railway-url/health

# Full status
curl https://your-railway-url/status

# Send a query
curl -X POST https://your-railway-url/query \
  -H "Content-Type: application/json" \
  -d '{
    "query_type": "legal",
    "content": "Motion to dismiss filed in federal court",
    "priority": "high"
  }'

# Check memory stats
curl https://your-railway-url/memory
```

## Features Live on Your Deployment

✅ **GENIUS Intelligence** - 75% token reduction
✅ **Glacier Mansion** - Orchestrates 8 MCP powerhouses (820 agents)
✅ **Aspen Grove Cognition** - Token-optimized memory with deduplication
✅ **Priority Routing** - Legal, evidence, RICO cases prioritized
✅ **Memory Stats** - Real-time token savings tracking

## Integration with Tasklet MCP

Once deployed, use your Railway URL as an MCP server connection in Tasklet:

```
https://your-railway-url
```

This will activate all 8 powerhouses and Library of Links integrations.
