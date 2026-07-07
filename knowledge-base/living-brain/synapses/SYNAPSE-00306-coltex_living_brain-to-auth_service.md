---
id: SYNAPSE-00306
title: "Synapse: coltex_living_brain ↔ auth_service"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, coltex_living_brain, auth_service]
related: [HUB-COLTEX_LIVING_BRAIN, HUB-AUTH_SERVICE]
see_also: [HUB-COLTEX_LIVING_BRAIN, HUB-AUTH_SERVICE]
depends_on: [HUB-COLTEX_LIVING_BRAIN]
---

# Neural Synapse: coltex_living_brain → auth_service

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**see_also** — documents in `coltex_living_brain` is related to `auth_service`.

## Source hub
- Hub: `coltex_living_brain`
- Anchor: `HUB-COLTEX_LIVING_BRAIN`

## Target hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
