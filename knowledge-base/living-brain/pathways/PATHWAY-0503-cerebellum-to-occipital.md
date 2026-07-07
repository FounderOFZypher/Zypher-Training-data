---
id: PATHWAY-0503
title: "Neural Pathway: cerebellum → occipital (associative)"
doc_type: neural_pathway
category: graphrag
hub: coltex_living_brain
lobe_source: cerebellum
lobe_target: occipital
pathway_type: associative
tags: [pathway, associative, cerebellum, occipital]
related: [LOBE-CEREBELLUM, LOBE-OCCIPITAL]
see_also: [LOBE-CEREBELLUM, LOBE-OCCIPITAL]
synthesizes: [LOBE-CEREBELLUM]
---

# Neural Pathway: cerebellum → occipital

**Type:** `associative` · **Tier:** association layer

## Route
Documents in lobe `cerebellum` connect to lobe `occipital` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-CEREBELLUM` (cerebellum)
- Target: `LOBE-OCCIPITAL` (occipital)

## Coltex Hypercortex
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
