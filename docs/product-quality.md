# Coltex Product Quality Standards

Coltex Mega RAG enforces quality gates so commercial builds deliver retrieval value, not empty volume. Gates are defined in product configs such as `config/product_mega.yaml`.

## Core principles

### Original, well-written content

- Distributable documents only (see `knowledge-base/PROVENANCE.md`)
- **Excluded:** placeholder stubs (`_excluded_from_distribution/`) and stress-test mega corpus (`generated/`)
- Content is original synthetic documentation — not copied from third-party sources
- Each document has a clear title, category, and tags

### Accurate metadata

Required fields on every document and chunk:

- `id` / `doc_id` — stable document identifier
- `title` — human-readable title

Additional metadata exported in `data/product/metadata/documents.json`:

- `doc_type`, `category`, `tags`, `hub`
- Relationship counts and types
- Source path and license

### Minimal duplication

- Chunks are deduplicated by `content_hash`
- Maximum duplicate ratio: **5%** (`max_duplicate_ratio: 0.05`)
- Builds fail if duplication exceeds threshold

### Clear licensing

- Runtime source: MIT — [LICENSE](../LICENSE)
- Commercial Mega RAG dataset: [EULA.md](../EULA.md)

### Regular updates

- `CHANGELOG.md` tracks version history
- `data/product/manifest.json` records `built_at` timestamp and SHA-256 checksums
- Product configs include `version` and `updated` fields

### Documentation

- Setup guide, evaluation guide, and quality standards (this document)
- Example applications in `examples/`
- Inline docstrings in `scripts/product/`

## Quality gates

| Gate | Threshold | Enforced by |
|------|-----------|-------------|
| Min chunk size | config-driven | `validate_quality.py` |
| Max duplicate ratio | 5% | stream / `validate_quality.py` |
| Required metadata | `doc_id`, `title` | `validate_quality.py` |
| Metadata accuracy | ≥ 90% | `evaluate_rag.py` |
| Retrieval recall@8 | config-driven | `evaluate_rag.py` |
| EULA / provenance | required for Mega SKUs | `audit_distribution.py` |

## What we exclude from product builds

- `knowledge-base/generated/**` — procedural stress-test corpus
- `knowledge-base/_excluded_from_distribution/**` — placeholder stubs
- `**/_seed/**` — internal seed copies

Run `make audit-distribution` before any commercial release.

## Product priorities

The commercial package prioritizes:

1. Retrieval accuracy over raw document count
2. Graph connectivity over unstructured volume
3. Benchmark evidence over vanity metrics
4. Checksums and manifests over undocumented dumps
