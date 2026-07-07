---
id: PATHWAY-0008
title: "Neural Pathway: frontal → thalamus (associative)"
doc_type: neural_pathway
category: graphrag
hub: coltex_living_brain
lobe_source: frontal
lobe_target: thalamus
pathway_type: associative
tags: [pathway, associative, frontal, thalamus]
related: [LOBE-FRONTAL, LOBE-THALAMUS]
see_also: [LOBE-FRONTAL, LOBE-THALAMUS]
synthesizes: [LOBE-FRONTAL]
---

# Neural Pathway: frontal → thalamus

**Type:** `associative` · **Tier:** association layer

## Route
Documents in lobe `frontal` connect to lobe `thalamus` via this commissural pathway.

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
- Target: `LOBE-THALAMUS` (thalamus)

## Coltex Hypercortex
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
