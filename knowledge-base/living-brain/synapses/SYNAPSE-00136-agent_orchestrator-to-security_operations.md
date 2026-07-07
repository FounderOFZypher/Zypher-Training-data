---
id: SYNAPSE-00136
title: "Synapse: agent_orchestrator ↔ security_operations"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, agent_orchestrator, security_operations]
related: [HUB-AGENT_ORCHESTRATOR, HUB-SECURITY_OPERATIONS]
see_also: [HUB-AGENT_ORCHESTRATOR, HUB-SECURITY_OPERATIONS]
depends_on: [HUB-AGENT_ORCHESTRATOR]
---

# Neural Synapse: agent_orchestrator → security_operations

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**see_also** — documents in `agent_orchestrator` is related to `security_operations`.

## Source hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Target hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
