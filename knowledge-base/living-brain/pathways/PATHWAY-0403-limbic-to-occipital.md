---
id: PATHWAY-0403
title: "Neural Pathway: limbic → occipital (modulatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_living_brain
lobe_source: limbic
lobe_target: occipital
pathway_type: modulatory
tags: [pathway, modulatory, limbic, occipital]
related: [LOBE-LIMBIC, LOBE-OCCIPITAL]
see_also: [LOBE-LIMBIC, LOBE-OCCIPITAL]
synthesizes: [LOBE-LIMBIC]
---

# Neural Pathway: limbic → occipital

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in lobe `limbic` connect to lobe `occipital` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-LIMBIC` (limbic)
- Target: `LOBE-OCCIPITAL` (occipital)

## Coltex Hypercortex
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
