---
id: SYNAPSE-00125
title: "Synapse: embedding_service ↔ coltex_living_brain"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, embedding_service, coltex_living_brain]
related: [HUB-EMBEDDING_SERVICE, HUB-COLTEX_LIVING_BRAIN]
see_also: [HUB-EMBEDDING_SERVICE, HUB-COLTEX_LIVING_BRAIN]
depends_on: [HUB-EMBEDDING_SERVICE]
---

# Neural Synapse: embedding_service → coltex_living_brain

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**documents** — documents in `embedding_service` documents `coltex_living_brain`.

## Source hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Target hub
- Hub: `coltex_living_brain`
- Anchor: `HUB-COLTEX_LIVING_BRAIN`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
