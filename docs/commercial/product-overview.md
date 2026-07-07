# Coltex Enterprise RAG Vector Dataset

**Production-grade retrieval-augmented generation corpus for commercial deployment.**

Coltex is a fully auditable, graph-linked, vector-ready knowledge dataset designed for teams building enterprise RAG products, AI agents, and domain-specific copilots. Every document carries typed metadata, cross-reference edges, and compliance provenance.

---

## License tiers

| Tier | Price | License |
|------|-------|---------|
| **Personal** | $79 USD (one-time) | [PERSONAL-LICENSE.md](../../PERSONAL-LICENSE.md) |
| **Commercial** | Contact / $1,000+ | [EULA.md](../../EULA.md) |

---

## Why Coltex

| Capability | Detail |
|------------|--------|
| **Scale** | 35,000+ deliverable documents (Enterprise tier); procedural capacity to billions+ |
| **Structure** | 63 technology domains · 18 knowledge hubs · 306 graph links · 90 domain routes |
| **Vector-ready** | Pre-chunked JSONL · optional pre-computed embeddings (MiniLM-L6-v2) |
| **GraphRAG** | Typed relationship edges · hub clustering · region-aware GraphRouter |
| **Compliance** | Personal or Commercial EULA · full provenance · audit pipeline |
| **Benchmarks** | FAQ pairs · retrieval gold · RAG evaluation datasets included |

---

## Architecture at a glance

```
Documents → Chunks → Embeddings → Vector index
     ↓
  Graph edges → GraphRAG expansion
     ↓
  Benchmarks → Quality evidence
```

Six processing layers (L1 ingestion through L6 governance), ten functional clusters, and four memory tiers organize content for retrieval routing and enterprise governance.

---

## Ideal use cases

- **Enterprise RAG copilots** — pre-built domain coverage across cloud, security, data, and platform engineering
- **Agent toolchains** — graph-linked runbooks, ADRs, and API references for multi-hop reasoning
- **Vector database seeding** — load `chunks.jsonl` + `embeddings.jsonl` into Pinecone, Weaviate, Chroma, or pgvector
- **Benchmark baselines** — reproducible recall@k and metadata accuracy evidence for buyer due diligence
- **Fine-tuning prep** — structured Q&A and retrieval gold pairs for domain adaptation

---

## What's included in a commercial build

| Artifact | Format | Purpose |
|----------|--------|---------|
| `catalog.jsonl` | JSONL | Full document metadata catalog |
| `chunks/chunks.jsonl` | JSONL | Vector-index-ready text chunks |
| `embeddings/embeddings.jsonl` | JSONL | Pre-computed 384-dim vectors |
| `graph/edges.jsonl` | JSONL | Typed relationship graph |
| `metadata/documents.json` | JSON | Sample metadata for inspection |
| `manifest.json` | JSON | SHA-256 checksums and build provenance |
| `benchmarks/` | JSONL | FAQ, retrieval gold, RAG eval sets |

Compliance files: `PERSONAL-LICENSE.md` or `EULA.md`, `NOTICE`, `PROVENANCE.md`, `distribution_audit.json`

---

## Build commands

```bash
# Enterprise curated tier (recommended starting point)
make product-enterprise

# Premium hyper tier (25k smoke / uncapped production)
make product-premium-smoke
make product-premium

# Verify compliance
make audit-distribution
make evaluate
```

See [SKU matrix](sku-matrix.md) for tier comparison and [datasheet](datasheet.md) for technical specifications.

---

## License

**Personal License ($79)** for non-commercial use, or **Commercial EULA** for business. See [PERSONAL-LICENSE.md](../../PERSONAL-LICENSE.md) and [product licensing](../product-licensing.md).
