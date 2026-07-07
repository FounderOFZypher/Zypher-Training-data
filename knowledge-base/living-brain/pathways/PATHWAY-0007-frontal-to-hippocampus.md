---
id: PATHWAY-0007
title: "Neural Pathway: frontal → hippocampus (modulatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_living_brain
lobe_source: frontal
lobe_target: hippocampus
pathway_type: modulatory
tags: [pathway, modulatory, frontal, hippocampus]
related: [LOBE-FRONTAL, LOBE-HIPPOCAMPUS]
see_also: [LOBE-FRONTAL, LOBE-HIPPOCAMPUS]
synthesizes: [LOBE-FRONTAL]
---

# Neural Pathway: frontal → hippocampus

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in lobe `frontal` connect to lobe `hippocampus` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-FRONTAL` (frontal)
- Target: `LOBE-HIPPOCAMPUS` (hippocampus)

## Coltex Hypercortex
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
