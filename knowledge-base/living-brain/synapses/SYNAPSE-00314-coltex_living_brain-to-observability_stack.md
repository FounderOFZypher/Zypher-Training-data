---
id: SYNAPSE-00314
title: "Synapse: coltex_living_brain ↔ observability_stack"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, coltex_living_brain, observability_stack]
related: [HUB-COLTEX_LIVING_BRAIN, HUB-OBSERVABILITY_STACK]
see_also: [HUB-COLTEX_LIVING_BRAIN, HUB-OBSERVABILITY_STACK]
depends_on: [HUB-COLTEX_LIVING_BRAIN]
---

# Neural Synapse: coltex_living_brain → observability_stack

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**see_also** — documents in `coltex_living_brain` is related to `observability_stack`.

## Source hub
- Hub: `coltex_living_brain`
- Anchor: `HUB-COLTEX_LIVING_BRAIN`

## Target hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
