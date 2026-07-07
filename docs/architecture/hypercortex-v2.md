# Coltex Hypercortex v2 — Architecture Reference

Coltex is architected as a **biologically-inspired multi-layer neural knowledge system** — the largest connected RAG dataset with advanced GraphRAG routing.

## System overview

```mermaid
flowchart TB
    subgraph cortex [Cortical Layers L1-L6]
        L1[L1 Sensory]
        L2[L2 Association]
        L3[L3 Integration]
        L4[L4 Reasoning]
        L5[L5 Executive]
        L6[L6 Meta]
        L1 --> L2 --> L3 --> L4 --> L5 --> L6
    end

    subgraph lobes [Brain Lobes]
        F[Frontal]
        T[Temporal]
        P[Parietal]
        O[Occipital]
        L[Limbic]
    end

    subgraph infra [Subcortical]
        Hippo[Hippocampus]
        Cereb[Cerebellum]
        Stem[Brainstem]
        Thal[Thalamus]
        Amyg[Amygdala]
    end

    subgraph graph [Graph Layer]
        Domains[62+ Domains]
        Hubs[18 Neural Hubs]
        Syn[Synapses]
        Path[Pathways]
    end

    cortex --> lobes
    lobes --> infra
    infra --> graph
    graph --> Retrieve[Hybrid Retrieval]
```

## Cortical layers

| Layer | Path | Role | Latency |
|-------|------|------|---------|
| L1 Sensory | `cortex/L1-sensory` | Ingestion signals, chunk boundaries | 5ms |
| L2 Association | `cortex/L2-association` | Metadata, domain tagging | 15ms |
| L3 Integration | `cortex/L3-integration` | Hub assignment, cross-domain | 30ms |
| L4 Reasoning | `cortex/L4-reasoning` | Multi-hop GraphRAG | 80ms |
| L5 Executive | `cortex/L5-executive` | Context assembly, reranking | 120ms |
| L6 Meta | `cortex/L6-meta` | Brain identity, architecture | 200ms |

## Brain lobes

| Lobe | Domains | Function |
|------|---------|----------|
| Frontal | architecture, agentic, api_design, microservices | Planning, ADRs, agents |
| Temporal | rag, embeddings, fine_tuning, prompt_engineering | Language, vectors, LLM |
| Parietal | sql, postgresql, vector_stores, indexing | Data structures, indexing |
| Occipital | observability, performance, mlops | Signals, dashboards |
| Limbic | security, incidents, memory, data_quality | Priority, memory, trust |
| Cerebellum | ci_cd, docker, kubernetes, terraform | Automation, motor ops |
| Hippocampus | — | Long-term memory consolidation |
| Thalamus | graphrag, retrieval | Query routing relay |
| Amygdala | security, incidents | Alert & SLA routing |

## Memory tiers

| Tier | Path | Capacity | Role |
|------|------|----------|------|
| Working | `memory/working` | 1,000 | Active session context |
| Episodic | `memory/episodic` | 50,000 | Incidents, timelines |
| Semantic | `memory/semantic` | 500,000 | Stable facts, ADRs |
| Procedural | `memory/procedural` | 100,000 | Runbooks, tutorials |

## Neural hubs (18)

Each hub is a connected document cluster with typed edges:

- `auth_service`, `indexing_pipeline`, `graphrag_engine`
- `vector_store_cluster`, `embedding_service`, `agent_orchestrator`
- `observability_stack`, `rag_retrieval_core`, `security_operations`
- `data_pipeline`, `llm_inference_gateway`, `knowledge_graph_store`
- `incident_command`, `ml_training_pipeline`, `api_gateway`
- `payment_service`, `ci_cd_platform`, `coltex_living_brain`

## Graph edge types (20)

**Core:** related, depends_on, uses, implements, calls, see_also

**Advanced:** extends, validates, contradicts, synthesizes, triggers, inhibits, supersedes, derived_from, tested_by, deployed_via

## Neural routing

`brain/graph/neural_router.py` implements **region-aware GraphRAG**:

- Documents in `/synapses/` and `/pathways/` get +12–15% score boost
- Advanced edge types (`synthesizes`, `validates`) add hop bonus
- 4-hop BFS with 16 max expanded documents

Enable via `config/brain.yaml`:
```yaml
graph:
  advanced_routing: true
  max_hops: 4
  max_extra_chunks: 16
```

## Scale targets

| Metric | Target |
|--------|--------|
| Domains | 62 |
| Hubs | 18 |
| Lobes | 10 |
| Cortex layers | 6 |
| Memory tiers | 4 |
| Documents | 250,000 |
| Graph edges | 1,000,000 |

## Manifests

- `data/brain/neural-map.json` — live document counts per region
- `data/brain/architecture-manifest.json` — architecture registry
- `config/brain_architecture.yaml` — master architecture spec

## Bootstrap

```bash
make living-brain-advanced    # Full Hypercortex v2
python3 -m brain pulse        # Architecture vitals
```
