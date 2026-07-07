---
id: SYNAPSE-00161
title: "Synapse: observability_stack ↔ coltex_living_brain"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, observability_stack, coltex_living_brain]
related: [HUB-OBSERVABILITY_STACK, HUB-COLTEX_LIVING_BRAIN]
see_also: [HUB-OBSERVABILITY_STACK, HUB-COLTEX_LIVING_BRAIN]
depends_on: [HUB-OBSERVABILITY_STACK]
---

# Neural Synapse: observability_stack → coltex_living_brain

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**see_also** — documents in `observability_stack` is related to `coltex_living_brain`.

## Source hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Target hub
- Hub: `coltex_living_brain`
- Anchor: `HUB-COLTEX_LIVING_BRAIN`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
