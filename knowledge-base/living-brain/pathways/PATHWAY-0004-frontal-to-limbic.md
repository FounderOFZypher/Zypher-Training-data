---
id: PATHWAY-0004
title: "Neural Pathway: frontal → limbic (commissural)"
doc_type: neural_pathway
category: graphrag
hub: coltex_living_brain
lobe_source: frontal
lobe_target: limbic
pathway_type: commissural
tags: [pathway, commissural, frontal, limbic]
related: [LOBE-FRONTAL, LOBE-LIMBIC]
see_also: [LOBE-FRONTAL, LOBE-LIMBIC]
synthesizes: [LOBE-FRONTAL]
---

# Neural Pathway: frontal → limbic

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in lobe `frontal` connect to lobe `limbic` via this commissural pathway.

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
- Target: `LOBE-LIMBIC` (limbic)

## Coltex Hypercortex
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
