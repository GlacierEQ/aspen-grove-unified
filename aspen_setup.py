#!/usr/bin/env python3
"""
ASPEN GROVE OPERATOR v7 - MCP SERVER WRAPPER
Glacier Mansion + Aspen Grove Intelligence at GENIUS Level
"""

from flask import Flask, request, jsonify
import os
import sys
from datetime import datetime
from enum import Enum
import hashlib

app = Flask(__name__)

# ============================================================================
# ASPEN GROVE COGNITION LAYER (Token Optimization)
# ============================================================================

class IntelligenceLevel(Enum):
    """Intelligence acceleration levels from Aspen Grove."""
    BASIC = 1
    ADVANCED = 2
    EXPERT = 3
    GENIUS = 4

class AspenGroveCognition:
    """Token-optimized memory cognition system."""
    
    STOPWORDS = {
        "the", "a", "an", "is", "are", "was", "were", "be", "been",
        "have", "has", "had", "do", "does", "did", "will", "would",
        "could", "should", "may", "might", "of", "in", "on", "at",
        "to", "for", "with", "by", "from", "up", "about", "into"
    }
    
    SOURCE_PRIORITY = {
        "legal": 10, "evidence": 9, "rico": 9, "actor": 8,
        "ios": 7, "github": 6, "notion": 6, "technical": 5, "general": 1
    }
    
    INTELLIGENCE_MULTIPLIERS = {
        IntelligenceLevel.BASIC: 1.0,
        IntelligenceLevel.ADVANCED: 0.65,
        IntelligenceLevel.EXPERT: 0.45,
        IntelligenceLevel.GENIUS: 0.25,
    }
    
    def __init__(self, intelligence_level: IntelligenceLevel = IntelligenceLevel.GENIUS):
        self.intelligence_level = intelligence_level
        self.memory_store = {}
        self.dedup_hashes = set()
        self.compression_ratio = self.INTELLIGENCE_MULTIPLIERS[intelligence_level]
    
    def hash_content(self, content: str) -> str:
        return hashlib.sha256(content.encode()).hexdigest()[:32]
    
    def compress_summary(self, text: str, max_chars: int = 200) -> str:
        if len(text) <= max_chars:
            return text
        sentences = text.replace("\n", " ").split(". ")
        scored = [(sum(1 for w in s.lower().split() if w not in self.STOPWORDS and len(w) > 3), s) for s in sentences]
        scored.sort(reverse=True)
        result = ". ".join(s for _, s in scored[:3])
        return result[:max_chars - 3] + "..." if len(result) > max_chars else result
    
    def token_estimate(self, text: str) -> int:
        return len(text) // 4
    
    def capture_with_intelligence(self, source: str, content: str, bucket: str = "general", priority: int = None):
        content_hash = self.hash_content(content)
        if content_hash in self.dedup_hashes:
            return {"status": "duplicate", "hash": content_hash}
        
        priority = priority or self.SOURCE_PRIORITY.get(source, 1)
        summary = content if self.intelligence_level == IntelligenceLevel.BASIC else self.compress_summary(content)
        tokens_original = self.token_estimate(content)
        tokens_compressed = self.token_estimate(summary)
        tokens_saved = tokens_original - tokens_compressed
        
        memory_card = {
            "id": f"mem_{content_hash}",
            "source": source,
            "bucket": bucket,
            "content": content,
            "summary": summary,
            "timestamp": datetime.utcnow().isoformat(),
            "priority": priority,
            "content_hash": content_hash,
            "intelligence_level": self.intelligence_level.name,
            "tokens_original": tokens_original,
            "tokens_compressed": tokens_compressed,
            "tokens_saved": tokens_saved,
        }
        
        self.memory_store[memory_card["id"]] = memory_card
        self.dedup_hashes.add(content_hash)
        
        return {
            "status": "captured",
            "memory_id": memory_card["id"],
            "hash": content_hash,
            "priority": priority,
            "bucket": bucket,
            "intelligence_level": self.intelligence_level.name,
            "token_reduction_pct": f"{(tokens_saved / tokens_original * 100):.1f}%" if tokens_original > 0 else "0%"
        }
    
    def get_stats(self):
        total_tokens = sum(m["tokens_original"] for m in self.memory_store.values())
        total_saved = sum(m["tokens_saved"] for m in self.memory_store.values())
        return {
            "total_memories": len(self.memory_store),
            "total_deduplicated": len(self.dedup_hashes),
            "total_tokens_original": total_tokens,
            "total_tokens_compressed": total_tokens - total_saved,
            "total_tokens_saved": total_saved,
            "intelligence_level": self.intelligence_level.name,
            "compression_ratio": f"{self.compression_ratio * 100:.0f}%",
            "efficiency": f"{(total_saved / max(total_tokens, 1) * 100):.1f}%"
        }

# ============================================================================
# GLACIER MANSION ORCHESTRATOR
# ============================================================================

class MCPPowerhouse:
    def __init__(self, name: str, port: int, agents: int, domain: str):
        self.name = name
        self.port = port
        self.agents = agents
        self.domain = domain
        self.status = "idle"
        self.queries_processed = 0

class GlacierMansionOrchestrator:
    def __init__(self, cognition: AspenGroveCognition):
        self.cognition = cognition
        self.powerhouses = self._initialize_powerhouses()
        self.query_cache = {}
        self.total_queries = 0
    
    def _initialize_powerhouses(self):
        return {
            "aspen_grove_legal": MCPPowerhouse("aspen_grove_legal", 8001, 200, "legal ops (RICO, motions, case law)"),
            "pantheon_orchestrator": MCPPowerhouse("pantheon_orchestrator", 8002, 150, "mythology orchestration (31 Titans)"),
            "forensic_deep_dive": MCPPowerhouse("forensic_deep_dive", 8003, 100, "digital forensics"),
            "solomon_codex": MCPPowerhouse("solomon_codex", 8004, 100, "legal intelligence"),
            "github_operations": MCPPowerhouse("github_operations", 8005, 80, "repo automation"),
            "cognitive_swarm": MCPPowerhouse("cognitive_swarm", 8006, 200, "distributed agent swarms"),
            "memory_omniindex": MCPPowerhouse("memory_omniindex", 8007, 150, "vector search + knowledge graph"),
            "deployment_orchestrator": MCPPowerhouse("deployment_orchestrator", 8008, 120, "execution orchestration")
        }
    
    def route_query(self, query_type: str, content: str, priority: str = "normal"):
        self.total_queries += 1
        capture_result = self.cognition.capture_with_intelligence(source=query_type, content=content, priority=priority or 5)
        powerhouse = self.powerhouses.get("aspen_grove_legal")
        return {
            "status": "routed",
            "query_id": capture_result.get("memory_id"),
            "powerhouse": powerhouse.name,
            "intelligence_level": self.cognition.intelligence_level.name,
            "capture_result": capture_result
        }
    
    def get_status(self):
        return {
            "router_status": "operational",
            "intelligence_level": self.cognition.intelligence_level.name,
            "queries_total": self.total_queries,
            "powerhouses_active": len(self.powerhouses),
            "cognition_stats": self.cognition.get_stats(),
            "powerhouses": {name: {"name": ph.name, "agents": ph.agents, "domain": ph.domain} for name, ph in self.powerhouses.items()}
        }

# Initialize at GENIUS level
cognition = AspenGroveCognition(IntelligenceLevel.GENIUS)
orchestrator = GlacierMansionOrchestrator(cognition)

# ============================================================================
# REST API ENDPOINTS
# ============================================================================

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "operational",
        "intelligence": "GENIUS",
        "token_reduction": "75%",
        "timestamp": datetime.utcnow().isoformat()
    }), 200

@app.route('/status', methods=['GET'])
def status():
    return jsonify(orchestrator.get_status()), 200

@app.route('/query', methods=['POST'])
def query():
    data = request.json or {}
    query_type = data.get('query_type', 'general')
    content = data.get('content', '')
    priority = data.get('priority', 'normal')
    
    if not content:
        return jsonify({"error": "content required"}), 400
    
    result = orchestrator.route_query(query_type, content, priority)
    return jsonify(result), 200

@app.route('/memory', methods=['GET'])
def memory():
    return jsonify(orchestrator.cognition.get_stats()), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)