# Coltex Mega RAG — Setup Guide

Build and query the Coltex Mega RAG commercial corpus (100,000,000+ documents).

## Install

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

## Validate commercial pipeline

```bash
make product-mega-smoke
python3 examples/load_dataset.py
make audit-distribution
```

## Full Mega build (100M+)

Requires cluster storage and CPU:

```bash
make product-mega
# equivalent:
python3 scripts/product/build_premium_product.py --config config/product_mega.yaml
```

## Marketplace packs

```bash
make marketplace-packs
cat data/product/marketplace/packs.json
```

## Bootstrap curated seed (optional)

```bash
make corpus-advanced
make corpus-mega
make expand-curated-kb COUNT=500
```

## Query / console

```bash
python3 -m runtime status
python3 -m runtime ask "your question"
coltex serve
```

## License

- Runtime: MIT — [LICENSE](../LICENSE)
- Commercial dataset: [EULA.md](../EULA.md)
