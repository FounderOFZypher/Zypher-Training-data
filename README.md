# Coltex

**Hypercortex v2 — The Living Brain** — the most advanced connected RAG knowledge architecture on earth. Six cortical layers, ten brain lobes, eighteen neural hubs, four memory tiers, and procedural growth to unlimited scale.

Coltex is a **living knowledge brain**: 62+ domain folders, thousands of graph-linked documents, inter-lobe pathways, synapses, and a premium export pipeline for commercial distribution.

---

## Hypercortex Architecture

```
                         ┌─── L6 Meta (Brain Identity) ───┐
                         │   L5 Executive (Reranking)     │
                         │   L4 Reasoning (GraphRAG)      │
                         │   L3 Integration (Hubs)        │
                         │   L2 Association (Metadata)    │
                         │   L1 Sensory (Ingestion)       │
                         └───────────────┬────────────────┘
                                         │
     ┌───────────┬───────────┬───────────┼───────────┬───────────┐
     ▼           ▼           ▼           ▼           ▼           ▼
  Frontal    Temporal    Parietal   Occipital    Limbic    Cerebellum
     │           │           │           │           │           │
     └───────────┴───────────┴─────► Thalamus ◄──────┴───────────┘
                                   Amygdala
                                         │
              ┌──────────────────────────┼──────────────────────────┐
              ▼                          ▼                          ▼
         62+ Domains              18 Neural Hubs            4 Memory Tiers
              │                          │                          │
              └──────────► Synapses + Pathways ◄───────────────────┘
                                   │
                    Vector + Metadata + NeuralRouter GraphRAG
                                   │
                          brain retrieve / pulse
```

| Region | Path | Purpose |
|--------|------|---------|
| **Cortex L1–L6** | `living-brain/cortex/` | Six-layer processing stack |
| **Lobes** | `living-brain/lobes/` | Frontal, temporal, parietal, occipital, limbic |
| **Domains** | `living-brain/domains/` | 62+ technology categories |
| **Hubs** | `living-brain/hubs/` | 18 neural service clusters |
| **Synapses** | `living-brain/synapses/` | Hub-to-hub graph links |
| **Pathways** | `living-brain/pathways/` | Inter-lobe neural routes |
| **Memory** | `living-brain/memory/` | Working, episodic, semantic, procedural |
| **Hippocampus** | `living-brain/hippocampus/` | Long-term consolidation |
| **Reflexes** | `living-brain/reflexes/` | Instant-recall FAQs |

Full reference: [docs/architecture/hypercortex-v2.md](docs/architecture/hypercortex-v2.md)

---

## Quick Start

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Bootstrap Hypercortex v2 (500 docs + pathways + hub anchors + cortex layers)
make living-brain-advanced

make index
python3 -m brain retrieve "Explain Hypercortex pathway routing" --context
python3 -m brain pulse
```

---

## Grow the Brain

| Command | Output |
|---------|--------|
| `make living-brain-advanced` | Full Hypercortex: 500 docs + pathways + 18 hub anchors |
| `make living-brain-grow COUNT=1000` | Add 1,000 domain documents |
| `make living-brain-mega` | **10,000** documents |
| `make generate-mega` | 100,000 procedural documents |
| `make generate-ultra` | 1,000,000 documents |
| `make generate-hyper` | Uncapped (604T+ combinations) |

Manifests: `data/brain/neural-map.json` · `data/brain/architecture-manifest.json`

---

## Advanced Retrieval

Hypercortex enables **NeuralRouter** — region-aware GraphRAG with:

- **4-hop** graph traversal (up from 2)
- **20 relationship types** (extends, validates, synthesizes, triggers…)
- **Region boost** for synapses (+15%), pathways (+12%), cortex L4/L5 (+10%)
- **16 max** graph-expanded documents per query

```yaml
# config/brain.yaml
graph:
  advanced_routing: true
  max_hops: 4
  max_extra_chunks: 16
```

---

## Scale

| Metric | Current | Target |
|--------|---------|--------|
| Neural hubs | 18 | 18 |
| Brain lobes | 10 | 10 |
| Cortex layers | 6 | 6 |
| Domains | 62+ | 62 |
| Documents | 3,000+ | 250,000 |
| Graph edges | 50,000+ | 1,000,000 |

---

## Premium Dataset Export

```bash
make product-premium-smoke   # 25,000 documents
make product-premium         # Full pipeline
make evaluate                # recall@8 benchmarks
```

---

## Documentation

- [Hypercortex v2 Architecture](docs/architecture/hypercortex-v2.md)
- [Product setup](docs/product-setup.md)
- [Quality standards](docs/product-quality.md)
- [Evaluation guide](docs/product-evaluation.md)

---

## License

Licensed under the [End User License Agreement](EULA). Third-party dependencies in [NOTICE](NOTICE).
