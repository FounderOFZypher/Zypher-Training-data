---
id: SYNAPSE-00298
title: "Synapse: api_gateway ↔ security_operations"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, api_gateway, security_operations]
related: [HUB-API_GATEWAY, HUB-SECURITY_OPERATIONS]
see_also: [HUB-API_GATEWAY, HUB-SECURITY_OPERATIONS]
depends_on: [HUB-API_GATEWAY]
---

# Neural Synapse: api_gateway → security_operations

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**calls** — documents in `api_gateway` calls into `security_operations`.

## Source hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Target hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
