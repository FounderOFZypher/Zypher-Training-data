# Coltex Mega RAG — SKU Matrix

Commercial packaging for the Coltex Mega RAG corpus (100,000,000+ documents).

All **commercial SKUs** (Professional, Enterprise, Mega) grant access to the
**full project** — the complete corpus, catalog, GraphRAG edges, benchmarks, and
delivery artifacts. SKUs differ by deployment scope, support, and delivery options.

| SKU | Corpus access | License | Commercial use | Includes |
|-----|---------------|---------|----------------|----------|
| **Personal** | Sample pack (~25k) | Personal + EULA | **Not permitted** | Evaluation sample, benchmark sample, MIT runtime |
| **Professional** | **Full project** (100M+) | Professional + EULA | Permitted | Single-entity production deployment, full corpus delivery |
| **Enterprise** | **Full project** (100M+) | Enterprise + EULA | Permitted | Multi-team deployment, private delivery, support SLA |
| **Mega** | **Full project** (100M+) | Mega + EULA | Permitted | Strategic delivery, partner programs, cluster-scale distribution |

Pricing is defined on the order form or invoice for each SKU.

---

## Marketplace packs

Domain packs are included in all commercial SKUs. They may also be referenced
individually for evaluation or partner bundling — see `config/marketplace.yaml`:

| Pack ID | Focus | Typical scale |
|---------|-------|---------------|
| `pack-rag-core` | RAG, GraphRAG, embeddings, retrieval | Multi-million |
| `pack-languages` | Python, JS/TS, Go, Rust, Java, C#, SQL | Multi-million |
| `pack-cloud-devops` | AWS, Azure, GCP, Kubernetes, Terraform, CI/CD | Multi-million |
| `pack-security-sre` | Security, observability, incidents, performance | Multi-million |
| `pack-architecture` | Microservices, DDD, API design, event-driven | Multi-million |

---

## Delivery formats

| Format | Path / artifact |
|--------|-----------------|
| Chunks JSONL | `data/product/chunks/chunks.jsonl` |
| Catalog JSONL | `data/product/catalog.jsonl` |
| Graph edges | `data/product/graph/edges.jsonl` |
| Embeddings | `data/product/embeddings/` |
| Manifest | `data/product/manifest.json` |
| Generation stats | `data/product/generation_stats.json` |
| Audit samples | `knowledge-base/distributable/_samples/` |

---

## Build targets

```bash
make product-mega-smoke   # capped commercial validation build
make product-mega         # full 100M+ Mega SKU build (cluster)
```
