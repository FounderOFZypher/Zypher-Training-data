# Coltex Mega RAG — SKU Matrix

Commercial packaging for the Coltex Mega RAG corpus (100,000,000+ documents).

| SKU | Documents | License | Includes |
|-----|-----------|---------|----------|
| **Personal** | Sample pack (~25k) | Personal + EULA | Sample corpus, benchmark sample, MIT runtime |
| **Professional** | Domain packs (1M–10M) | Professional + EULA | Selected domain shards, graph, embeddings export |
| **Enterprise** | Multi-domain (10M–50M) | Enterprise + EULA | Multi-team seats, private delivery, support SLA |
| **Mega** | **100,000,000+** | Mega + EULA | Full streaming corpus, all shards, catalog, GraphRAG edges |

Pricing is defined on the order form or invoice for each SKU.

---

## Marketplace packs

Sold individually or bundled under Professional / Enterprise / Mega:

| Pack ID | Focus | Typical scale |
|---------|-------|---------------|
| `pack-rag-core` | RAG, GraphRAG, embeddings, retrieval | Multi-million |
| `pack-languages` | Python, JS/TS, Go, Rust, Java, C#, SQL | Multi-million |
| `pack-cloud-devops` | AWS, Azure, GCP, Kubernetes, Terraform, CI/CD | Multi-million |
| `pack-security-sre` | Security, observability, incidents, performance | Multi-million |
| `pack-architecture` | Microservices, DDD, API design, event-driven | Multi-million |

See `config/marketplace.yaml` for registry categories and publishing rules.

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
