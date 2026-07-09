# Coltex Mega RAG — Product Spec

**Commercial RAG corpus — 100,000,000+ documents for production retrieval.**

**Goal:** Deliver a GraphRAG-ready commercial knowledge corpus: streaming-generated,
audit-ready, and packaged as Personal → Professional → Enterprise → Mega SKUs.

---

## Primary build

```bash
make product-mega-smoke   # capped validation
make product-mega         # full 100M+ commercial build (cluster)
```

Config: `config/product_mega.yaml`

---

## Commercial docs

- [Product overview](../commercial/product-overview.md)
- [SKU matrix](../commercial/sku-matrix.md)
- [Datasheet](../commercial/datasheet.md)
- [EULA](../../EULA.md)

---

## Runtime console

```bash
pip install -e .
coltex serve
coltex deploy
```

See [deployment guide](../deployment/self-hosted.md)

---

## License

- Runtime: MIT
- Commercial dataset: EULA + tier license (Professional, Enterprise, or Mega)
- Personal: non-commercial evaluation only; commercial SKUs grant full project access
