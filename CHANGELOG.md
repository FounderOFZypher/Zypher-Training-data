# Changelog

All notable changes to the Coltex product package are documented here.

## [4.11.0] - 2026-07-08

### Changed — Self-hosted deployment platform

- **Repositioned as self-hosted** — "A Self-Hosted AI Knowledge Platform" (localhost is one profile, not the product)
- **Deployment system** — `config/deployment.yaml` with profiles: local, lan, production
- **Configurable** — host, port, protocol, domain, SSL certs, networking via config or env vars
- **Commands** — `coltex serve --profile lan`, `coltex deploy`
- **Docker** — Dockerfile and docker-compose.yml for container deployment
- **Docs** — `docs/deployment/self-hosted.md` for Windows, Linux, TLS, reverse proxy
- **Knowledge Studio** — Deployment page showing access URLs and configuration

## [4.10.0] - 2026-07-08

### Added — Native `.ctex` workspaces

- **Workspace as project file** — `coltex new`, `open`, `build`, `status`, `validate`, `export`, `import`
- **`.ctex` manifest** — auto-managed metadata (UUID, settings, stats, health); never stores vectors or documents
- **Workspace layout** — knowledge/, documents/, embeddings/, graph/, metadata/, settings/, runtime/
- **Session tracking** — `.coltex-session` and `COLTEX_WORKSPACE` for active workspace
- **`coltex` CLI entry point** — `./coltex` or `python3 -m runtime`

## [4.9.0] - 2026-07-08

### Changed — Coltex V1 is CLI-only, MIT licensed

- **Removed web UI** — deleted Knowledge Studio server and static HTML; no website, no cloud
- **CLI is the product** — `dashboard`, `sources`, `settings`, `knowledge` commands added; `studio` removed
- **MIT License** — replaced all paid tiers, EULA, Personal/Professional/Enterprise licenses
- **Removed commercial docs** — deleted `licenses/`, `docs/commercial/`, tier pricing configs
- **Updated product configs** — `require_license` checks root `LICENSE` instead of EULA files

## [4.8.0] - 2026-07-08

### Added — Coltex V1 product

- **Tagline:** The AI Knowledge Platform for Modern Organizations
- **Knowledge Studio V1 UI** — Dashboard, Knowledge, Sources, Search, Ask Knowledge, Analytics, Settings
- **Upload & process** — PDF, DOCX, MD, TXT, HTML, JSON via Studio or `runtime upload`
- **Ask Knowledge** — Q&A with sources, confidence, and explainability (`runtime ask`)
- **Universal Search** — one search bar across document types
- **V1 dashboard** — honest metrics: documents, sources, searches, AI queries, last sync, health
- **Settings** — workspace, AI provider, embedding model, chunk size
- Product spec: [docs/product/coltex-v1.md](docs/product/coltex-v1.md)

## [4.7.0] - 2026-07-07

### Added — Knowledge Studio, monitoring, explainability, proactive curator

- **Knowledge Studio** — `python3 -m runtime studio` web UI (Health, Curator, Monitor, Explorer, Search, Explain)
- **Runtime Monitor** — `python3 -m runtime monitor` (memory, docs, embeddings, events/sec, latency)
- **Explainability** — `python3 -m runtime explain` with similarity, graph, metadata, API match reasons
- **Proactive AI Curator** — actionable alerts; auto-runs after ingest pipeline
- **Filesystem + GitHub connectors** — `python3 -m runtime connector filesystem|github`
- **Plugin SDK** — `runtime/plugins/sdk.py` for connectors, processors, curators, search algorithms
- Expanded Memory Engine (5 tiers) and Knowledge Evolution (incl. deleted state)
- Knowledge Health: disconnected_graphs metric; honest README "Use today" table

## [4.6.0] - 2026-07-07

### Added — Coltex Runtime (live platform centerpiece)

- New `runtime/` package — Coltex Runtime orchestrates all platform engines
- Event Bus with full ingest pipeline cascade and `data/runtime/events.jsonl` logging
- Knowledge DNA schema (`config/knowledge-dna.yaml`) — objects not files
- Knowledge Evolution states (`config/knowledge-evolution.yaml`)
- AI Curator engine — merge, quality, disconnect, embedding regen recommendations
- Analytics engine — Knowledge Quality, Coverage, Graph Integrity, Duplicate Risk
- CLI: `python3 -m runtime status|health|curator|ingest|events|dna|search`
- Makefile targets: `runtime-status`, `runtime-health`, `runtime-curator`, `runtime-events`
- Marketplace manifest (`config/marketplace.yaml`)
- [docs/platform/runtime.md](docs/platform/runtime.md)
- README centered on Coltex Runtime, not dataset specification

## [4.5.0] - 2026-07-07

### Changed — Knowledge OS & intelligence-first architecture

- Repositioned as **The Knowledge Operating System for AI** (from infrastructure platform)
- Architecture centered on intelligence loop: Understand → Connect → Reason → Retrieve → Improve
- Added [docs/platform/knowledge-os.md](docs/platform/knowledge-os.md) and [docs/platform/intelligence-engine.md](docs/platform/intelligence-engine.md)
- Added config manifests: events, lifecycle, scheduler, governance, extensibility
- Expanded roadmap with Knowledge Intelligence Engine, Health, Memory, Reasoning Layer, Governance

## [4.4.0] - 2026-07-07

### Changed — Platform repositioning

- Repositioned Coltex as **AI Knowledge Infrastructure Platform** (not dataset-only)
- Rewrote README with platform components, available vs. roadmap status
- Added [docs/platform/overview.md](docs/platform/overview.md) and [docs/platform/roadmap.md](docs/platform/roadmap.md)
- Added [config/connectors.yaml](config/connectors.yaml) connector ecosystem manifest
- Updated commercial product overview for platform framing

## [4.3.4] - 2026-07-07

### Added — Coltex Enterprise License (Custom Quote)

- Added [ENTERPRISE-LICENSE.md](ENTERPRISE-LICENSE.md) for organization-wide enterprise deployment
- Includes Professional License rights plus multi-team deployment, private/on-prem cloud, and enterprise services
- Updated `config/product_enterprise.yaml` with `require_enterprise_license` and `license_path: ENTERPRISE-LICENSE.md`
- Four-tier licensing: Personal ($79) → Professional ($399) → Enterprise (custom quote) → Dataset EULA

## [4.3.3] - 2026-07-07

### Added — Coltex Professional License ($399)

- Added [PROFESSIONAL-LICENSE.md](PROFESSIONAL-LICENSE.md) for commercial use by one entity
- Includes Personal License rights plus commercial product/revenue rights
- Added `config/product_professional.yaml` and `make product-professional` build target
- Updated three-tier licensing: Personal ($79) → Professional ($399) → Enterprise EULA

## [4.3.2] - 2026-07-07

### Added — Coltex Personal License ($79)

- Added [PERSONAL-LICENSE.md](PERSONAL-LICENSE.md) for non-commercial personal use
- Added `config/product_personal.yaml` and `make product-personal` build target
- Updated SKU matrix, product-licensing docs, and README with Personal vs Commercial tiers

## [4.3.1] - 2026-07-07

### Changed — Commercial EULA

- Replaced Apache-2.0 dataset licensing with **Coltex End User License Agreement (EULA)**
- Added `EULA.md` (root) and `knowledge-base/EULA.md`
- Updated product configs, audit pipeline, and commercial docs for EULA compliance
- `knowledge-base/LICENSE` now points to EULA; engine third-party deps remain in `NOTICE`

## [4.3.0] - 2026-07-07

### Added — Enterprise RAG Vector Dataset (commercial tier)

- **`config/product_enterprise.yaml`** — Enterprise tier v3.0.0 (13,000+ documents)
- **`scripts/product/build_enterprise_product.py`** — Full enterprise build orchestrator
- **`make product-enterprise`** / **`make product-enterprise-fast`** — Commercial build targets
- **Commercial documentation** — `docs/commercial/product-overview.md`, `datasheet.md`, `sku-matrix.md`
- **`examples/load_dataset.py`** — Buyer inspection script
- **`knowledge-base/distributable/DATASET.md`** — Distributable package orientation

### Changed — Scale & polish

- Corpus expanded to **12,993 documents** across 63 domains (`make corpus-mega`)
- Enterprise build produces **83,612 vector chunks**, **52,490 graph edges**, **1,100+ benchmark pairs**
- Chunk deduplication scoped per document (preserves cross-doc coverage)
- Distribution validation allows ≤1% thin documents on large corpora
- Fixed manifest/audit crash when `generation_stats` path absent
- README repositioned as commercial **Enterprise RAG Vector Dataset** with SKU matrix

## [4.2.2] - 2026-07-07

### Changed — Enterprise terminology (Phase 4)

- Renamed corpus regions: `lobes/` → `clusters/`, `synapses/` → `graph-links/`, `pathways/` → `domain-routes/`, `reflexes/` → `quick-reference/`, `cortex/` → `processing-layers/`
- Renamed standalone regions: `hippocampus/` → `retention/`, `cerebellum/` → `automation/`, `brainstem/` → `operations/`, `thalamus/` → `routing/`, `amygdala/` → `priority/`
- Functional cluster slugs: `frontal` → `architecture`, `temporal` → `retrieval`, `parietal` → `data`, `occipital` → `observability`, `limbic` → `security`
- Processing layer slugs: `L1_sensory` → `L1_ingestion`, `L2_association` → `L2_metadata`, `L4_reasoning` → `L4_graph`, `L5_executive` → `L5_assembly`, `L6_meta` → `L6_governance`
- `brain/graph/neural_router.py` → `graph_router.py` (`NeuralRouter` → `GraphRouter`)
- `data/brain/neural-map.json` → `catalog-index.json`
- Generated artifact prefixes: `SYNAPSE-*` → `LINK-*`, `REFLEX-*` → `FAQ-*`, `PATHWAY-*` → `ROUTE-*`
- Doc types: `neural_pathway` → `domain_route`, `synapse_map` → `graph_link_map`
- Removed deprecated `brain pulse` CLI alias
- Makefile: `corpus-synapses` → `corpus-links`

## [4.2.1] - 2026-07-07

### Changed — Professional terminology

- Renamed `living-brain/` → `knowledge-corpus/`
- Renamed `scripts/living_brain.py` → `scripts/knowledge_corpus.py`
- Replaced "Living Brain" / "Hypercortex" wording with **Knowledge Corpus** / **Knowledge Architecture**
- Hub `coltex_living_brain` → `coltex_knowledge_core`
- CLI `brain pulse` → `brain report`
- Makefile targets: `corpus`, `corpus-advanced`, `corpus-grow`, `corpus-report`

## [4.2.0] - 2026-07-07

### Added — Knowledge Architecture v2

- **`config/brain_architecture.yaml`** — Master spec: 6 cortical layers, 10 lobes, 4 memory tiers, 18 hubs
- **`scripts/brain_architecture.py`** — Architecture loader and domain-to-lobe mapping
- **`brain/graph/neural_router.py`** — Region-aware GraphRAG with pathway/synapse score boosts
- **10 brain lobes** — frontal, temporal, parietal, occipital, limbic, cerebellum, hippocampus, thalamus, amygdala, brainstem
- **6 cortical layers** — L1-sensory through L6-meta
- **4 memory tiers** — working, episodic, semantic, procedural
- **Inter-lobe pathways** — excitatory, inhibitory, modulatory, associative, commissural
- **13 new neural hubs** — vector_store_cluster, agent_orchestrator, llm_inference_gateway, etc.
- **10 advanced GraphRAG edge types** — extends, validates, synthesizes, triggers, etc.
- **`data/brain/architecture-manifest.json`** — Live architecture registry
- **`docs/architecture/knowledge-architecture.md`** — Full architecture reference
- **`make corpus-advanced`** — Full architecture bootstrap command
- Enhanced `brain report` — architecture metrics (domains, clusters, pathways)

### Changed

- Graph routing: 4 hops, 16 max chunks, advanced_routing enabled by default
- `KNOWLEDGE_HUBS` expanded from 5 → 18
- `RELATIONSHIP_TYPES` expanded from 10 → 20

## [4.1.0] - 2026-07-07

### Added — Coltex Knowledge Corpus

- **`knowledge-base/knowledge-corpus/`** — Domain-organized folder tree
- **`scripts/knowledge_corpus.py`** — Bootstrap, grow, wire graph links, build catalog
- Makefile targets: `corpus`, `corpus-grow`, `corpus-mega`, `corpus-report`

### Changed

- README repositioned as **enterprise knowledge corpus** (not RAG-as-a-Service)
- `config/brain.yaml` indexes `knowledge-corpus/` paths

### Removed

- `coltex_platform/` RAG-as-a-Service API (out of scope)
- Docker/Kubernetes platform deployment, sales/API docs, platform tests

## [2.1.0] - 2026-07-07

### Added

- **`PREMIUM_CATEGORIES` (50) and `PREMIUM_DOC_TYPES` (20)** in `brain_schema.py` as single source of truth
- 8 new premium doc types: incident_report, design_document, migration_guide, release_notes, database_schema, deep_dive, comparison, case_study
- 28 additional categories covering RAG/AI, languages, databases, cloud, architecture, and tooling
- `config/categories_premium.yaml` reference list for premium tier builds
- 24 new corpus topic seeds (hybrid reranking, observability, vector stores, agentic patterns, and more)
- Doc-type-aware benchmark question templates with difficulty tiers and category stratification
- Multi-hop retrieval gold queries from knowledge hub graph links

### Changed

- Premium smoke build increased to **25,000 documents** (from 10,000) across **50 categories** and **20 doc types**
- Benchmark datasets increased to **250 FAQ pairs**, **270 retrieval gold**, **250 RAG eval** (from 20 each)
- Premium generator now round-robins topics for category diversity in bounded builds
- Premium document sections include concrete operational details and checklists
- Fixed Go/C++ code snippet template escaping for corpus generation
- Smoke builds skip embedding export by default (`--skip-embeddings`) for faster iteration

## [3.1.0] - 2026-07-06

### Changed

- Rebranded **Zypher** → **Coltex** across codebase, docs, and knowledge base
- Renamed `Zypher` class to `Coltex`; vector collection `zypher` → `coltex`

## [3.0.0] - 2026-07-06

### Removed (database-only focus)

- `zypher/` chatbot CLI and LLM provider
- `zypher_platform/` REST API, sessions, jobs, agents
- Fine-tuning scripts (`train.py`, `infer.py`, `prepare_advanced_dataset.py`)
- `config/llm.yaml`, `platform.yaml`, `zypher_xs.yaml`, `rag.yaml`
- Notebooks, Kubernetes/Docker hosting configs in knowledge-base
- Conversation memory module (chat-only)

### Changed

- Repository is now **Zypher** RAG database only (chatbot, API, and fine-tuning removed)
- Rebranded **Zypher Brain** → **Zypher** (`Zypher` class, `zypher` collection)
- Dropped **Mega** from product naming (README, NOTICE, CLI, docs)
- `python3 -m brain` CLI for index / retrieve / stats
- Slimmed `requirements.txt` to RAG dependencies only

## [2.0.0] - 2026-07-06

### Added

- **$1000+ Premium RAG Dataset** — hyper-scale distributable corpus
- `mega_multiplier: 100000000000` (100 billion× tier)
- Streaming generation: `scripts/product/stream_premium_corpus.py`
- Premium content generator with 6+ sections, code examples, graph edges per document
- `make product-premium-smoke`, `make product-premium`, `make product-hyper`
- Catalog.jsonl metadata index for billion-scale document tracking
- Estimated 604+ trillion unique document combinations (procedural)

## [1.1.0] - 2026-07-06

### Added

- Commercial distribution compliance: `NOTICE`, `knowledge-base/LICENSE`, `PROVENANCE.md`
- Distribution audit (`make audit-distribution`) — scans for third-party content, forbidden markers
- Quarantined 54 non-distributable placeholder stubs to `_excluded_from_distribution/`
- `.dockerignore` excludes generated and quarantined content from releases

### Changed

- Product build excludes `_excluded_from_distribution/` from commercial package
- Documentation updated with honest content origin and licensing requirements

## [1.0.0] - 2026-07-06

### Added

- **Product pipeline** (`make product`) — curated knowledge package build
- Vector-ready chunks with accurate metadata (`data/product/chunks/`)
- Embedding generation script (`scripts/product/export_embeddings.py`)
- Graph relationship export (`data/product/graph/edges.jsonl`)
- Deduplication pipeline (max 5% duplicate ratio)
- Quality validation gates (`scripts/product/validate_quality.py`)
- Benchmark datasets: FAQ pairs, retrieval gold, RAG eval (`benchmarks/`)
- RAG evaluation with evidence report (`benchmarks/evaluation_report.json`)
- Product manifest with SHA-256 checksums (`data/product/manifest.json`)
- Curated brain config (`config/brain_curated.yaml`) — CHUNK docs only
- Example applications (`examples/rag_query.py`, `brain_retrieve.py`, `api_client.py`)
- Documentation: setup guide, quality standards, evaluation guide, licensing
- Coltex EULA

### Design

- Value over volume: curated `CHUNK-*.md` documents, not synthetic mega corpus
- Quality gates enforce metadata accuracy, minimal duplication, and retrieval evidence
- Brain = knowledge; LLM = reasoning engine (unchanged architecture)
