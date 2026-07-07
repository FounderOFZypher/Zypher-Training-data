---
id: PATHWAY-0705
title: "Neural Pathway: hippocampus → cerebellum (modulatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_living_brain
lobe_source: hippocampus
lobe_target: cerebellum
pathway_type: modulatory
tags: [pathway, modulatory, hippocampus, cerebellum]
related: [LOBE-HIPPOCAMPUS, LOBE-CEREBELLUM]
see_also: [LOBE-HIPPOCAMPUS, LOBE-CEREBELLUM]
synthesizes: [LOBE-HIPPOCAMPUS]
---

# Neural Pathway: hippocampus → cerebellum

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in lobe `hippocampus` connect to lobe `cerebellum` via this commissural pathway.

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
- Target: `LOBE-CEREBELLUM` (cerebellum)

## Coltex Hypercortex
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
