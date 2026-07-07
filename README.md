# Coltex

**The Living Brain** — the largest connected RAG knowledge dataset with hybrid retrieval, graph-linked domains, neural hubs, and procedural growth to unlimited scale.

Coltex is not a SaaS platform. It is a **living knowledge brain**: hundreds of domain folders, thousands of graph-linked documents, synapses between neural hubs, and an export pipeline that packages the entire corpus for commercial distribution.

---

## What Is the Living Brain?

```
                    ┌─────────────────────────────────┐
                    │         COLTEX CORTEX           │
                    │    (meta-reasoning layer)       │
                    └───────────────┬─────────────────┘
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        ▼                           ▼                           ▼
  ┌───────────┐              ┌───────────┐              ┌───────────┐
  │  DOMAINS  │◄──synapse──►│   HUBS    │◄──synapse──►│  REFLEXES │
  │ 30+ tech  │              │  neural   │              │ fast FAQ  │
  │ categories│              │ clusters  │              │           │
  └─────┬─────┘              └─────┬─────┘              └───────────┘
        │                          │
        └──────────┬───────────────┘
                   ▼
         Vector Index + GraphRAG + Metadata
                   ▼
              brain retrieve / pulse
```

| Region | Path | Purpose |
|--------|------|---------|
| **Domains** | `knowledge-base/living-brain/domains/` | Category-organized docs (RAG, K8s, Python, security…) |
| **Hubs** | `living-brain/hubs/` | Service clusters (auth, GraphRAG, indexing…) |
| **Synapses** | `living-brain/synapses/` | Cross-hub neural graph links |
| **Cortex** | `living-brain/cortex/` | Brain identity and meta-layer |
| **Memory** | `living-brain/memory/` | Long-horizon episodic knowledge |
| **Reflexes** | `living-brain/reflexes/` | Instant-recall FAQs |

---

## Quick Start

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Bootstrap the living brain (folders + 300 domain docs + synapses)
make living-brain

# Index and query
make index
python3 -m brain retrieve "What is GraphRAG?" --context
python3 -m brain pulse
```

---

## Grow the Brain

| Command | Output |
|---------|--------|
| `make living-brain` | Scaffold + 300 domain docs + synapses + neural map |
| `make living-brain-grow COUNT=500` | Add 500 docs across all domains |
| `make living-brain-mega` | **10,000** documents across 30+ domains |
| `make expand-curated-kb COUNT=200` | High-quality CHUNK docs at KB root |
| `make generate-mega` | 100,000 procedural documents |
| `make generate-ultra` | 1,000,000 documents |
| `make generate-hyper` | Uncapped streaming (604T+ combinations) |

```bash
# Check brain vitals anytime
make living-brain-pulse
python3 -m brain pulse
```

Neural map manifest: `data/brain/neural-map.json`

---

## Retrieval Engine

Hybrid RAG pipeline in `brain/`:

1. Query embedding (MiniLM)
2. Vector search (ChromaDB)
3. Metadata filtering (doc_type, category, hub)
4. GraphRAG expansion (synapses, `depends_on`, `see_also`)
5. Source-weighted reranking
6. Context assembly

```bash
python3 -m brain index --reindex
python3 -m brain retrieve "<query>" --context
python3 -m brain stats
python3 -m brain pulse
```

---

## Premium Dataset Export

Package the entire brain for commercial sale:

```bash
make product-premium-smoke   # 25,000 documents
make product-premium         # Full premium pipeline
make evaluate                # recall@8 benchmark evidence
make audit-distribution      # Compliance audit
```

| Artifact | Description |
|----------|-------------|
| `chunks.jsonl` | Vector-ready segments |
| `embeddings.jsonl` | Pre-computed vectors |
| `edges.jsonl` | Graph relationship export |
| `catalog.jsonl` | Document provenance index |
| `manifest.json` | SHA-256 checksums |

---

## Scale

| Tier | Documents | Command |
|------|-----------|---------|
| Curated seed | 500+ | Included in repo |
| Living brain bootstrap | 300+ per run | `make living-brain` |
| Premium smoke | 25,000 | `make product-premium-smoke` |
| Mega | 100,000 | `make generate-mega` |
| Ultra | 1,000,000 | `make generate-ultra` |
| Hyper | Uncapped | `make generate-hyper` |

Procedural expansion enables **604+ trillion** unique document combinations via streaming generation.

---

## Repository Structure

```
.
├── brain/                      # Living brain retrieval engine + CLI
├── knowledge-base/
│   ├── CHUNK-*.md              # Curated seed documents
│   └── living-brain/           # Domain folders, hubs, synapses, cortex
│       ├── domains/            # 30+ technology domains
│       ├── hubs/               # Neural clusters
│       ├── synapses/           # Cross-hub graph links
│       ├── cortex/             # Brain meta-layer
│       ├── memory/             # Episodic knowledge
│       └── reflexes/           # Fast-path FAQs
├── scripts/
│   ├── living_brain.py         # Grow, wire, and map the brain
│   ├── generate_corpus.py      # Hyper-scale procedural generation
│   └── product/                # Dataset export pipeline
├── data/brain/neural-map.json  # Brain manifest (auto-generated)
├── benchmarks/                 # Evaluation datasets
└── docs/                       # Setup, quality, evaluation guides
```

---

## Documentation

- [Product setup](docs/product-setup.md)
- [Quality standards](docs/product-quality.md)
- [Evaluation guide](docs/product-evaluation.md)
- [Licensing](docs/product-licensing.md)
- [Content provenance](knowledge-base/PROVENANCE.md)

---

## License

Licensed under the [End User License Agreement](EULA). Third-party dependencies are listed in [NOTICE](NOTICE).
