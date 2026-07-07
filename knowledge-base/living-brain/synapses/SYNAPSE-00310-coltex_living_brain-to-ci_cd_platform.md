---
id: SYNAPSE-00310
title: "Synapse: coltex_living_brain ↔ ci_cd_platform"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, coltex_living_brain, ci_cd_platform]
related: [HUB-COLTEX_LIVING_BRAIN, HUB-CI_CD_PLATFORM]
see_also: [HUB-COLTEX_LIVING_BRAIN, HUB-CI_CD_PLATFORM]
depends_on: [HUB-COLTEX_LIVING_BRAIN]
---

# Neural Synapse: coltex_living_brain → ci_cd_platform

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**see_also** — documents in `coltex_living_brain` is related to `ci_cd_platform`.

## Source hub
- Hub: `coltex_living_brain`
- Anchor: `HUB-COLTEX_LIVING_BRAIN`

## Target hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
