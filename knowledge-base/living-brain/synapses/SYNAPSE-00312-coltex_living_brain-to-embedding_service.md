---
id: SYNAPSE-00312
title: "Synapse: coltex_living_brain ↔ embedding_service"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, coltex_living_brain, embedding_service]
related: [HUB-COLTEX_LIVING_BRAIN, HUB-EMBEDDING_SERVICE]
see_also: [HUB-COLTEX_LIVING_BRAIN, HUB-EMBEDDING_SERVICE]
depends_on: [HUB-COLTEX_LIVING_BRAIN]
---

# Neural Synapse: coltex_living_brain → embedding_service

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**documents** — documents in `coltex_living_brain` documents `embedding_service`.

## Source hub
- Hub: `coltex_living_brain`
- Anchor: `HUB-COLTEX_LIVING_BRAIN`

## Target hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
