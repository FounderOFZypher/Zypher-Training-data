---
id: PATHWAY-0701
title: "Neural Pathway: hippocampus → temporal (associative)"
doc_type: neural_pathway
category: graphrag
hub: coltex_living_brain
lobe_source: hippocampus
lobe_target: temporal
pathway_type: associative
tags: [pathway, associative, hippocampus, temporal]
related: [LOBE-HIPPOCAMPUS, LOBE-TEMPORAL]
see_also: [LOBE-HIPPOCAMPUS, LOBE-TEMPORAL]
synthesizes: [LOBE-HIPPOCAMPUS]
---

# Neural Pathway: hippocampus → temporal

**Type:** `associative` · **Tier:** association layer

## Route
Documents in lobe `hippocampus` connect to lobe `temporal` via this commissural pathway.

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
- Target: `LOBE-TEMPORAL` (temporal)

## Coltex Hypercortex
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
