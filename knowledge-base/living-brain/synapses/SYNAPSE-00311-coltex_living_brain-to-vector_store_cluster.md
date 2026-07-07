---
id: SYNAPSE-00311
title: "Synapse: coltex_living_brain ↔ vector_store_cluster"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, coltex_living_brain, vector_store_cluster]
related: [HUB-COLTEX_LIVING_BRAIN, HUB-VECTOR_STORE_CLUSTER]
see_also: [HUB-COLTEX_LIVING_BRAIN, HUB-VECTOR_STORE_CLUSTER]
depends_on: [HUB-COLTEX_LIVING_BRAIN]
---

# Neural Synapse: coltex_living_brain → vector_store_cluster

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**calls** — documents in `coltex_living_brain` calls into `vector_store_cluster`.

## Source hub
- Hub: `coltex_living_brain`
- Anchor: `HUB-COLTEX_LIVING_BRAIN`

## Target hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
