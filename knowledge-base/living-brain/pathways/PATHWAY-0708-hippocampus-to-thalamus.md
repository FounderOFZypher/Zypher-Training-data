---
id: PATHWAY-0708
title: "Neural Pathway: hippocampus → thalamus (excitatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_living_brain
lobe_source: hippocampus
lobe_target: thalamus
pathway_type: excitatory
tags: [pathway, excitatory, hippocampus, thalamus]
related: [LOBE-HIPPOCAMPUS, LOBE-THALAMUS]
see_also: [LOBE-HIPPOCAMPUS, LOBE-THALAMUS]
synthesizes: [LOBE-HIPPOCAMPUS]
---

# Neural Pathway: hippocampus → thalamus

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in lobe `hippocampus` connect to lobe `thalamus` via this commissural pathway.

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
- Target: `LOBE-THALAMUS` (thalamus)

## Coltex Hypercortex
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
