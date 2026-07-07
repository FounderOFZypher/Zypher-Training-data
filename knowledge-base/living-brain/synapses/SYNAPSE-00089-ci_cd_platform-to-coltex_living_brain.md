---
id: SYNAPSE-00089
title: "Synapse: ci_cd_platform ↔ coltex_living_brain"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, ci_cd_platform, coltex_living_brain]
related: [HUB-CI_CD_PLATFORM, HUB-COLTEX_LIVING_BRAIN]
see_also: [HUB-CI_CD_PLATFORM, HUB-COLTEX_LIVING_BRAIN]
depends_on: [HUB-CI_CD_PLATFORM]
---

# Neural Synapse: ci_cd_platform → coltex_living_brain

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**see_also** — documents in `ci_cd_platform` is related to `coltex_living_brain`.

## Source hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Target hub
- Hub: `coltex_living_brain`
- Anchor: `HUB-COLTEX_LIVING_BRAIN`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
