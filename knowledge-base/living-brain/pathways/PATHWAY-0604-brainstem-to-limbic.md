---
id: PATHWAY-0604
title: "Neural Pathway: brainstem → limbic (excitatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_living_brain
lobe_source: brainstem
lobe_target: limbic
pathway_type: excitatory
tags: [pathway, excitatory, brainstem, limbic]
related: [LOBE-BRAINSTEM, LOBE-LIMBIC]
see_also: [LOBE-BRAINSTEM, LOBE-LIMBIC]
synthesizes: [LOBE-BRAINSTEM]
---

# Neural Pathway: brainstem → limbic

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in lobe `brainstem` connect to lobe `limbic` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-BRAINSTEM` (brainstem)
- Target: `LOBE-LIMBIC` (limbic)

## Coltex Hypercortex
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
