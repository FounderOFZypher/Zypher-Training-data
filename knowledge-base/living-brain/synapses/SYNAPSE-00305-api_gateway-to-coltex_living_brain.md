---
id: SYNAPSE-00305
title: "Synapse: api_gateway ↔ coltex_living_brain"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, api_gateway, coltex_living_brain]
related: [HUB-API_GATEWAY, HUB-COLTEX_LIVING_BRAIN]
see_also: [HUB-API_GATEWAY, HUB-COLTEX_LIVING_BRAIN]
depends_on: [HUB-API_GATEWAY]
---

# Neural Synapse: api_gateway → coltex_living_brain

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**see_also** — documents in `api_gateway` is related to `coltex_living_brain`.

## Source hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Target hub
- Hub: `coltex_living_brain`
- Anchor: `HUB-COLTEX_LIVING_BRAIN`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
