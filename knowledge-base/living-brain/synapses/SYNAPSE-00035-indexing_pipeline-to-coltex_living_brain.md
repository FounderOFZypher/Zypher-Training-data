---
id: SYNAPSE-00035
title: "Synapse: indexing_pipeline ↔ coltex_living_brain"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, indexing_pipeline, coltex_living_brain]
related: [HUB-INDEXING_PIPELINE, HUB-COLTEX_LIVING_BRAIN]
see_also: [HUB-INDEXING_PIPELINE, HUB-COLTEX_LIVING_BRAIN]
depends_on: [HUB-INDEXING_PIPELINE]
---

# Neural Synapse: indexing_pipeline → coltex_living_brain

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**calls** — documents in `indexing_pipeline` calls into `coltex_living_brain`.

## Source hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Target hub
- Hub: `coltex_living_brain`
- Anchor: `HUB-COLTEX_LIVING_BRAIN`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
