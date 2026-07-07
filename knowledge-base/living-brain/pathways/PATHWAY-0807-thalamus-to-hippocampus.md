---
id: PATHWAY-0807
title: "Neural Pathway: thalamus → hippocampus (excitatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_living_brain
lobe_source: thalamus
lobe_target: hippocampus
pathway_type: excitatory
tags: [pathway, excitatory, thalamus, hippocampus]
related: [LOBE-THALAMUS, LOBE-HIPPOCAMPUS]
see_also: [LOBE-THALAMUS, LOBE-HIPPOCAMPUS]
synthesizes: [LOBE-THALAMUS]
---

# Neural Pathway: thalamus → hippocampus

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in lobe `thalamus` connect to lobe `hippocampus` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-THALAMUS` (thalamus)
- Target: `LOBE-HIPPOCAMPUS` (hippocampus)

## Coltex Hypercortex
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
