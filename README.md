# Zypher — Enterprise AI Coding Assistant

Fine-tune **poolside/Laguna-XS-2.1** on the Zypher dataset, then deploy with **Enterprise RAG** for the final chatbot.

**Data clarification:** The seed knowledge base (`knowledge-base/`, ~167 curated files) is expanded by a corpus generator that produces a large synthetic corpus from structured templates. At `SCALE=1000`, the generator creates ~112k templated documents; training examples (~650k–800k+) are derived via multi-task dataset preparation. This is **volume expansion through structured generation**, not 1000× more unique human-authored knowledge.

## Architecture

```
Base Model (poolside/Laguna-XS-2.1)
      │
      ▼
Fine-Tune on Zypher Dataset
      │
      ▼
Zypher XS
      │
      ▼
+
Enterprise RAG
      │
      ▼
Final Chatbot
```

| Stage | What it is | Output |
|-------|------------|--------|
| **Base Model** | Poolside Laguna XS 2.1 — 33B MoE coding model (3B active/token) | `poolside/Laguna-XS-2.1` |
| **Zypher Dataset** | Multi-task SFT data from seed + generated corpus | `data/zypher/train.jsonl` |
| **Zypher XS** | QLoRA adapter fine-tuned on Zypher data | `outputs/zypher-xs/final` |
| **Enterprise RAG** | ChromaDB + embeddings + GraphRAG over `knowledge-base/` | `data/vector_store/` |
| **Final Chatbot** | Zypher XS + retrieval + memory | `python -m zypher.chat` |

### Data pipeline (feeds fine-tuning)

```
┌─────────────────────────────────────────────────────────────────┐
│                     SEED KNOWLEDGE BASE                         │
│          knowledge-base/  (~167 curated markdown files)          │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                     CORPUS GENERATOR                            │
│              scripts/generate_corpus.py  (SCALE)                │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                     ZYPHER DATASET BUILDER                      │
│           scripts/prepare_advanced_dataset.py                   │
│   train.jsonl · val.jsonl · test.jsonl → data/zypher/           │
└─────────────────────────────────────────────────────────────────┘
```

## What makes Zypher unique

| Differentiator | Description |
|----------------|-------------|
| **Code-native RAG** | Knowledge spans RAG, GraphRAG, AST-based chunking, and retrieval APIs — designed for internal codebases. |
| **GraphRAG reasoning** | Documents cover knowledge graphs, dependency traversal, and architectural reasoning over code structure. |
| **Agentic workflows** | Training data includes tool-calling patterns, multi-step debugging, and incident triage flows. |
| **Enterprise operations** | Runbooks, ADRs, incident reports, and security practices reflect production constraints. |
| **Zypher XS** | Domain-tuned coding assistant built on Laguna XS 2.1, not a generic base model. |
| **Multi-task SFT** | 8+ task types: multi-turn dialogue, chain-of-thought, RAG-with-context, code review, and more. |

## Quick start

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
huggingface-cli login          # accept Laguna license on HF first

make generate-smoke            # optional: expand corpus
make prepare                   # → data/zypher/
make train-xs                  # → outputs/zypher-xs/final (GPU required)
make index                     # build Enterprise RAG index
make chat                      # Final Chatbot
```

## Google Colab (fine-tune Zypher XS)

1. Accept the [Laguna XS 2.1 license](https://huggingface.co/poolside/Laguna-XS-2.1) on Hugging Face
2. Open **[notebooks/finetune_zypher_xs_colab.ipynb](notebooks/finetune_zypher_xs_colab.ipynb)**
3. Runtime → **A100** or **L4** (24 GB+ VRAM)
4. Run all cells

```
https://colab.research.google.com/github/FOUNDEROF-AIRIES-AGENT/Zypher-Training-data/blob/cursor/llm-finetune-ready-da1e/notebooks/finetune_zypher_xs_colab.ipynb
```

After training, download the adapter and run locally:

```bash
make index
make chat
```

## Project structure

```
.
├── zypher/                       # Final chatbot (Enterprise RAG + Zypher XS)
│   ├── backend.py                # RAG orchestration
│   ├── xs.py                     # Zypher XS model wrapper
│   ├── vector_store.py           # ChromaDB semantic search
│   ├── graphrag.py               # Graph-linked retrieval expansion
│   ├── knowledge_base.py         # Markdown KB loader
│   ├── memory.py                 # Conversation memory
│   └── chat.py                   # CLI entry point
├── knowledge-base/               # Seed corpus (~167 curated files)
│   └── generated/                # Synthetic corpus (~112k at scale=1000)
├── scripts/
│   ├── generate_corpus.py        # Synthetic corpus generator
│   ├── prepare_advanced_dataset.py  # Zypher dataset builder
│   ├── train.py                  # QLoRA fine-tune → Zypher XS
│   ├── infer.py                  # Raw model inference (no RAG)
│   └── validate_pipeline.py      # Pre-flight checks
├── config/
│   ├── zypher_xs.yaml            # Fine-tune: Laguna → Zypher XS
│   ├── rag.yaml                  # Enterprise RAG settings
│   └── corpus_generation.yaml    # Corpus scale & categories
└── data/zypher/                  # Training data (gitignored)
```

## Example conversation

```
User:
Explain GraphRAG.

Zypher:
GraphRAG combines graph traversal with retrieval-augmented generation. Instead of
retrieving isolated text chunks, Zypher builds a knowledge graph from your codebase
where nodes represent entities (functions, classes, modules) and edges represent
relationships (calls, imports, inheritance).

This enables multi-hop architectural reasoning — for example, tracing what breaks
if you change the auth middleware, across services rather than returning a single snippet.
```

## Current results (v0.1)

**Not yet trained** — benchmark targets for the first run. Update after Colab training.

| Metric | Target |
|--------|--------|
| FAQ accuracy (seed set) | > 70% |
| Validation loss (SFT) | < 2.0 |
| RAG faithfulness | > 80% |
| Multi-turn coherence | > 75% |
| GraphRAG concept accuracy | > 75% |
| Code review score | > 70% |

## Corpus scale

| `SCALE` | Synthetic files | Training examples (approx.) |
|---------|-----------------|------------------------------|
| 10 | ~1,125 | ~8,000 |
| 100 | ~11,250 | ~80,000 |
| 1000 | ~112,500 | ~650,000–800,000+ |

```bash
SCALE=1000 make generate
make prepare
```

## Training task types

| Task type | Description |
|-----------|-------------|
| `faq` / `documentation` | Single-turn Q&A |
| `multi_turn_dialogue` | Follow-up conversations |
| `chain_of_thought` | Reasoning with `<|think|>` blocks |
| `tool_calling` | Simulated tool use |
| `rag_with_context` | Context-grounded answers |
| `code_generation` / `code_review` | Code tasks |

## Hardware

| Step | GPU | Notes |
|------|-----|-------|
| Zypher XS QLoRA | A100 40GB / L4 24GB | Recommended |
| Enterprise RAG index | CPU OK | `sentence-transformers/all-MiniLM-L6-v2` |
| Final chatbot | 24 GB+ VRAM | 4-bit Zypher XS + retrieval |

## Configuration

- **Fine-tune:** `config/zypher_xs.yaml` — base model, LoRA, output path
- **RAG:** `config/rag.yaml` — embeddings, ChromaDB, GraphRAG, memory
- **Corpus:** `config/corpus_generation.yaml` — scale and categories

## Limitations

| Limitation | Impact |
|------------|--------|
| **Synthetic corpus dominance** | At full scale, most text is templated — models may repeat phrasing patterns. |
| **Laguna license** | Must accept Poolside license on Hugging Face before training. |
| **GPU required for Zypher XS** | QLoRA fine-tune and inference need 24 GB+ VRAM for practical use. |
| **Tool calling is simulated** | Training includes tool patterns; live execution is limited. |
| **No RLHF / DPO** | Alignment relies on SFT only. |

## Roadmap

| Phase | Status | Deliverables |
|-------|--------|--------------|
| **v1.0 — Zypher XS** | Done | Dataset prep, QLoRA training, Enterprise RAG chatbot |
| **v1.1 — Evaluation** | Planned | Benchmark scripts on seed FAQ/RAG/code tasks |
| **v1.2 — Live tools** | Planned | Metrics, search, lint tools beyond simulated training |
| **v2.0 — GraphRAG runtime** | Planned | Code graph builder wired to live retrieval |
