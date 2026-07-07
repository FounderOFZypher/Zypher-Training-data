---
id: SYNAPSE-00071
title: "Synapse: payment_service ↔ coltex_living_brain"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, payment_service, coltex_living_brain]
related: [HUB-PAYMENT_SERVICE, HUB-COLTEX_LIVING_BRAIN]
see_also: [HUB-PAYMENT_SERVICE, HUB-COLTEX_LIVING_BRAIN]
depends_on: [HUB-PAYMENT_SERVICE]
---

# Neural Synapse: payment_service → coltex_living_brain

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**depends_on** — documents in `payment_service` depends on `coltex_living_brain`.

## Source hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Target hub
- Hub: `coltex_living_brain`
- Anchor: `HUB-COLTEX_LIVING_BRAIN`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
