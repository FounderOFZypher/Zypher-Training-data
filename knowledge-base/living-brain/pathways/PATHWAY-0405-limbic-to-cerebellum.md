---
id: PATHWAY-0405
title: "Neural Pathway: limbic → cerebellum (commissural)"
doc_type: neural_pathway
category: graphrag
hub: coltex_living_brain
lobe_source: limbic
lobe_target: cerebellum
pathway_type: commissural
tags: [pathway, commissural, limbic, cerebellum]
related: [LOBE-LIMBIC, LOBE-CEREBELLUM]
see_also: [LOBE-LIMBIC, LOBE-CEREBELLUM]
synthesizes: [LOBE-LIMBIC]
---

# Neural Pathway: limbic → cerebellum

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in lobe `limbic` connect to lobe `cerebellum` via this commissural pathway.

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
- Target: `LOBE-CEREBELLUM` (cerebellum)

## Coltex Hypercortex
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
