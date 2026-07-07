---
id: SYNAPSE-00024
title: "Synapse: indexing_pipeline ↔ embedding_service"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, indexing_pipeline, embedding_service]
related: [HUB-INDEXING_PIPELINE, HUB-EMBEDDING_SERVICE]
see_also: [HUB-INDEXING_PIPELINE, HUB-EMBEDDING_SERVICE]
depends_on: [HUB-INDEXING_PIPELINE]
---

# Neural Synapse: indexing_pipeline → embedding_service

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**documents** — documents in `indexing_pipeline` documents `embedding_service`.

## Source hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Target hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
