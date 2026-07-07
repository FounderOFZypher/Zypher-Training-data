---
id: PATHWAY-0700
title: "Neural Pathway: hippocampus → frontal (modulatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_living_brain
lobe_source: hippocampus
lobe_target: frontal
pathway_type: modulatory
tags: [pathway, modulatory, hippocampus, frontal]
related: [LOBE-HIPPOCAMPUS, LOBE-FRONTAL]
see_also: [LOBE-HIPPOCAMPUS, LOBE-FRONTAL]
synthesizes: [LOBE-HIPPOCAMPUS]
---

# Neural Pathway: hippocampus → frontal

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in lobe `hippocampus` connect to lobe `frontal` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-HIPPOCAMPUS` (hippocampus)
- Target: `LOBE-FRONTAL` (frontal)

## Coltex Hypercortex
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
