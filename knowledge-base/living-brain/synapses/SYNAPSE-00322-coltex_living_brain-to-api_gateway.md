---
id: SYNAPSE-00322
title: "Synapse: coltex_living_brain ↔ api_gateway"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, coltex_living_brain, api_gateway]
related: [HUB-COLTEX_LIVING_BRAIN, HUB-API_GATEWAY]
see_also: [HUB-COLTEX_LIVING_BRAIN, HUB-API_GATEWAY]
depends_on: [HUB-COLTEX_LIVING_BRAIN]
---

# Neural Synapse: coltex_living_brain → api_gateway

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**see_also** — documents in `coltex_living_brain` is related to `api_gateway`.

## Source hub
- Hub: `coltex_living_brain`
- Anchor: `HUB-COLTEX_LIVING_BRAIN`

## Target hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
