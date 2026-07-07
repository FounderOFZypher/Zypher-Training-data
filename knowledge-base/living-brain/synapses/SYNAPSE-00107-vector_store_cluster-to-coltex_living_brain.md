---
id: SYNAPSE-00107
title: "Synapse: vector_store_cluster ↔ coltex_living_brain"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, vector_store_cluster, coltex_living_brain]
related: [HUB-VECTOR_STORE_CLUSTER, HUB-COLTEX_LIVING_BRAIN]
see_also: [HUB-VECTOR_STORE_CLUSTER, HUB-COLTEX_LIVING_BRAIN]
depends_on: [HUB-VECTOR_STORE_CLUSTER]
---

# Neural Synapse: vector_store_cluster → coltex_living_brain

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**calls** — documents in `vector_store_cluster` calls into `coltex_living_brain`.

## Source hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Target hub
- Hub: `coltex_living_brain`
- Anchor: `HUB-COLTEX_LIVING_BRAIN`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
