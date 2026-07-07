#!/usr/bin/env python3
"""
Coltex Living Brain — grow, organize, and wire the knowledge corpus.

Creates domain folders, neural hubs, synapse links, and a neural-map manifest
so Coltex behaves as a living, connected brain — not a flat file dump.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from brain_schema import CATEGORIES, KNOWLEDGE_HUBS
from corpus_templates import TOPICS
from expand_curated_kb import (
    CURATED_DOC_TYPES,
    _chunk_id,
    _existing_chunk_max,
    _format_chunk_markdown,
    _slugify,
    iter_curated_jobs,
)
from generate_corpus import build_document

LIVING_ROOT = ROOT / "knowledge-base" / "living-brain"
NEURAL_MAP_PATH = ROOT / "data" / "brain" / "neural-map.json"

DOMAIN_README = """# {name} Domain

Part of the **Coltex Living Brain** — `{category}` knowledge cluster.

Documents here are auto-generated, graph-linked, and indexed by the Coltex brain.
Each file carries typed metadata (`doc_type`, `hub`, `related`) for GraphRAG traversal.

## Stats
- Category: `{category}`
- Parent: `living-brain/domains/{category}/`

Query this domain:
```bash
python3 -m brain retrieve "your question about {category}"
```
"""

HUB_README = """# {title} Hub

Neural hub `{slug}` — a connected cluster of documents sharing `hub: {slug}` metadata.

## Components
{components}

## Linked doc types
{doc_types}
"""

SYNAPSE_TEMPLATE = """---
id: SYNAPSE-{synapse_id}
title: "Synapse: {source_hub} ↔ {target_hub}"
doc_type: deep_dive
category: graphrag
hub: coltex_living_brain
tags: [synapse, graph, {source_hub}, {target_hub}]
related: [{source_doc}, {target_doc}]
see_also: [{source_doc}, {target_doc}]
depends_on: [{source_doc}]
---

# Neural Synapse: {source_hub} → {target_hub}

Cross-domain connection in the Coltex Living Brain graph.

## Connection type
**{relation}** — documents in `{source_hub}` {relation_desc} `{target_hub}`.

## Source hub
- Hub: `{source_hub}`
- Anchor: `{source_doc}`

## Target hub
- Hub: `{target_hub}`
- Anchor: `{target_doc}`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
"""


def _ensure_structure() -> dict[str, Path]:
    """Create living-brain folder tree."""
    dirs: dict[str, Path] = {
        "root": LIVING_ROOT,
        "domains": LIVING_ROOT / "domains",
        "hubs": LIVING_ROOT / "hubs",
        "synapses": LIVING_ROOT / "synapses",
        "cortex": LIVING_ROOT / "cortex",
        "memory": LIVING_ROOT / "memory",
        "reflexes": LIVING_ROOT / "reflexes",
    }
    for key, path in dirs.items():
        path.mkdir(parents=True, exist_ok=True)

    # Domain folders from priority categories
    priority = [
        "rag", "graphrag", "agentic", "vector_stores", "embeddings", "retrieval",
        "python", "java", "javascript", "typescript", "go", "rust", "sql",
        "postgresql", "mongodb", "redis", "docker", "kubernetes",
        "aws", "azure", "gcp", "microservices", "security", "architecture",
        "api_design", "ci_cd", "testing", "observability", "performance",
        "fine_tuning", "data_quality", "incidents", "mlops",
    ]
    domain_paths: dict[str, Path] = {}
    for cat in priority:
        d = dirs["domains"] / cat
        d.mkdir(parents=True, exist_ok=True)
        readme = d / "README.md"
        if not readme.exists():
            readme.write_text(
                DOMAIN_README.format(name=cat.replace("_", " ").title(), category=cat),
                encoding="utf-8",
            )
        domain_paths[cat] = d

    # Hub folders
    hub_paths: dict[str, Path] = {}
    for hub in KNOWLEDGE_HUBS:
        h = dirs["hubs"] / hub.slug
        h.mkdir(parents=True, exist_ok=True)
        readme = h / "README.md"
        if not readme.exists():
            components = "\n".join(f"- {c}" for c in hub.components)
            doc_types = ", ".join(hub.doc_types)
            readme.write_text(
                HUB_README.format(
                    title=hub.title,
                    slug=hub.slug,
                    components=components,
                    doc_types=doc_types,
                ),
                encoding="utf-8",
            )
        hub_paths[hub.slug] = h

    # Cortex manifest (brain identity)
    cortex_manifest = dirs["cortex"] / "BRAIN_IDENTITY.md"
    if not cortex_manifest.exists():
        cortex_manifest.write_text(
            _cortex_identity(),
            encoding="utf-8",
        )

    root_readme = LIVING_ROOT / "README.md"
    if not root_readme.exists():
        root_readme.write_text(_living_brain_readme(), encoding="utf-8")

    dirs["domain_paths"] = domain_paths  # type: ignore
    dirs["hub_paths"] = hub_paths  # type: ignore
    return dirs


def _cortex_identity() -> str:
    return """---
id: CORTEX-00001
title: Coltex Living Brain Identity
doc_type: deep_dive
category: rag
hub: coltex_living_brain
tags: [cortex, identity, living-brain]
---

# Coltex Living Brain

The cortex is the meta-layer of Coltex — it defines what this brain *is*.

## Purpose
Coltex is a **living knowledge brain**: documents, synapses, hubs, and domains
that grow procedurally and connect via typed graph edges.

## Anatomy
| Region | Path | Role |
|--------|------|------|
| Domains | `domains/` | Category-organized knowledge (RAG, K8s, Python…) |
| Hubs | `hubs/` | Service-level clusters (auth, indexing, GraphRAG…) |
| Synapses | `synapses/` | Cross-hub neural links |
| Cortex | `cortex/` | Meta-reasoning and brain identity |
| Memory | `memory/` | Long-horizon episodic knowledge |
| Reflexes | `reflexes/` | Fast-path FAQs and runbooks |

## Pulse
```bash
python3 -m brain pulse
make living-brain-pulse
```
"""


def _living_brain_readme() -> str:
    return """# Coltex Living Brain

The largest connected RAG knowledge brain — domains, hubs, synapses, and graph-linked documents.

## Grow the brain
```bash
make living-brain              # scaffold folders + synapses + neural map
make living-brain-grow COUNT=500   # add 500 domain documents
make living-brain-mega         # 10,000 documents across all domains
```

## Query
```bash
make index
python3 -m brain retrieve "How does GraphRAG traverse synapses?" --context
python3 -m brain pulse
```

## Structure
```
living-brain/
├── domains/     # 30+ technology domains
├── hubs/        # Neural clusters (auth, GraphRAG, indexing…)
├── synapses/    # Cross-domain graph links
├── cortex/      # Brain meta-layer
├── memory/      # Episodic knowledge
└── reflexes/    # Fast-path operational docs
```
"""


def grow_domains(count: int, dry_run: bool = False) -> dict:
    """Generate documents into domain folders."""
    structure = _ensure_structure()
    domain_paths: dict[str, Path] = structure["domain_paths"]  # type: ignore

    start_num = _existing_chunk_max() + 1
    # Also scan living-brain for max chunk
    for path in LIVING_ROOT.rglob("CHUNK-*.md"):
        m = re.match(r"CHUNK-(\d+)", path.name)
        if m:
            start_num = max(start_num, int(m.group(1)) + 1)

    jobs = iter_curated_jobs(count, start_num)
    written = 0
    by_domain: dict[str, int] = {}

    for chunk_num, topic, doc_type, variant in jobs:
        body, metadata = build_document(topic, doc_type, variant, scale=1000)
        metadata["hub"] = metadata.get("hub") or topic.hub or f"domain_{topic.category}"
        related = [_chunk_id(chunk_num - i) for i in range(1, min(4, chunk_num - start_num + 1))]
        content = _format_chunk_markdown(chunk_num, body, metadata, related)

        domain_dir = domain_paths.get(topic.category) or (structure["domains"] / topic.category)
        domain_dir.mkdir(parents=True, exist_ok=True)

        slug = _slugify(metadata["title"])
        filename = f"CHUNK-{chunk_num:05d}-{slug}.md"
        path = domain_dir / filename

        if not dry_run:
            path.write_text(content, encoding="utf-8")
        written += 1
        by_domain[topic.category] = by_domain.get(topic.category, 0) + 1

    return {
        "documents_written": written,
        "start_chunk": start_num,
        "end_chunk": start_num + written - 1 if written else start_num,
        "domains_touched": len(by_domain),
        "by_domain": by_domain,
        "dry_run": dry_run,
    }


def wire_synapses(dry_run: bool = False) -> dict:
    """Create synapse documents linking knowledge hubs."""
    structure = _ensure_structure()
    synapse_dir: Path = structure["synapses"]
    hubs = KNOWLEDGE_HUBS
    written = 0
    synapse_ids: list[str] = []

    relations = [
        ("depends_on", "depends on"),
        ("see_also", "is related to"),
        ("calls", "calls into"),
        ("documents", "documents"),
    ]

    for i, source in enumerate(hubs):
        for j, target in enumerate(hubs):
            if source.slug == target.slug:
                continue
            relation, relation_desc = relations[(i + j) % len(relations)]
            synapse_num = i * len(hubs) + j
            synapse_id = f"{synapse_num:05d}"
            source_doc = f"HUB-{source.slug.upper().replace('-', '_')}"
            target_doc = f"HUB-{target.slug.upper().replace('-', '_')}"

            content = SYNAPSE_TEMPLATE.format(
                synapse_id=synapse_id,
                source_hub=source.slug,
                target_hub=target.slug,
                source_doc=source_doc,
                target_doc=target_doc,
                relation=relation,
                relation_desc=relation_desc,
            )
            path = synapse_dir / f"SYNAPSE-{synapse_id}-{source.slug}-to-{target.slug}.md"
            if not dry_run:
                path.write_text(content, encoding="utf-8")
            written += 1
            synapse_ids.append(f"SYNAPSE-{synapse_id}")

    return {"synapses_written": written, "synapse_ids": synapse_ids[:10], "dry_run": dry_run}


def seed_reflexes(dry_run: bool = False) -> dict:
    """Fast-path reflex documents (instant-recall FAQs)."""
    structure = _ensure_structure()
    reflex_dir: Path = structure["reflexes"]
    prompts = [
        ("What is Coltex?", "Coltex is a living RAG knowledge brain with hybrid retrieval."),
        ("What is GraphRAG?", "GraphRAG expands vector hits via typed document relationship edges."),
        ("How do I query the brain?", "python3 -m brain retrieve \"your question\" --context"),
        ("How do I grow the brain?", "make living-brain-grow COUNT=500"),
        ("What is a synapse?", "A cross-hub graph link in living-brain/synapses/."),
    ]
    written = 0
    for i, (q, a) in enumerate(prompts):
        content = f"""---
id: REFLEX-{i:05d}
title: "{q}"
doc_type: faq
category: rag
hub: coltex_living_brain
tags: [reflex, faq, instant-recall]
---

# {q}

{a}

## Reflex path
Reflexes are fast-recall nodes — optimized for common queries during brain pulse and retrieval.
"""
        path = reflex_dir / f"REFLEX-{i:05d}-{ _slugify(q) }.md"
        if not dry_run:
            path.write_text(content, encoding="utf-8")
        written += 1
    return {"reflexes_written": written, "dry_run": dry_run}


def build_neural_map() -> dict:
    """Scan entire knowledge base and write neural-map.json manifest."""
    kb_root = ROOT / "knowledge-base"
    domains: dict[str, int] = {}
    hubs: dict[str, int] = {}
    doc_types: dict[str, int] = {}
    total = 0
    synapses = 0
    reflexes = 0

    for path in kb_root.rglob("*.md"):
        if "_excluded" in path.parts or "_seed" in path.parts:
            continue
        total += 1
        if "synapses" in path.parts:
            synapses += 1
        if "reflexes" in path.parts:
            reflexes += 1
        if "domains" in path.parts:
            parts = path.parts
            idx = parts.index("domains")
            if idx + 1 < len(parts):
                cat = parts[idx + 1]
                domains[cat] = domains.get(cat, 0) + 1
        try:
            text = path.read_text(encoding="utf-8")[:2000]
            if "hub:" in text:
                for line in text.splitlines():
                    if line.strip().startswith("hub:"):
                        hub = line.split(":", 1)[1].strip().strip('"')
                        hubs[hub] = hubs.get(hub, 0) + 1
                        break
            if "doc_type:" in text:
                for line in text.splitlines():
                    if line.strip().startswith("doc_type:"):
                        dt = line.split(":", 1)[1].strip().strip('"')
                        doc_types[dt] = doc_types.get(dt, 0) + 1
                        break
        except OSError:
            pass

    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "brain": "coltex-living-brain",
        "total_documents": total,
        "domains": domains,
        "domain_count": len(domains),
        "hubs": hubs,
        "hub_count": len(hubs),
        "doc_types": doc_types,
        "synapses": synapses,
        "reflexes": reflexes,
        "categories_available": len(CATEGORIES),
        "topics_available": len(TOPICS),
    }

    NEURAL_MAP_PATH.parent.mkdir(parents=True, exist_ok=True)
    NEURAL_MAP_PATH.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest


def bootstrap(grow: int = 300, dry_run: bool = False) -> dict:
    """Full living brain bootstrap: structure + grow + synapses + reflexes + map."""
    _ensure_structure()
    grow_stats = grow_domains(grow, dry_run=dry_run) if grow > 0 else {}
    synapse_stats = wire_synapses(dry_run=dry_run)
    reflex_stats = seed_reflexes(dry_run=dry_run)
    neural_map = build_neural_map() if not dry_run else {}
    return {
        "bootstrap": True,
        "grow": grow_stats,
        "synapses": synapse_stats,
        "reflexes": reflex_stats,
        "neural_map": {
            "total_documents": neural_map.get("total_documents"),
            "domain_count": neural_map.get("domain_count"),
            "path": str(NEURAL_MAP_PATH),
        },
        "dry_run": dry_run,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Coltex Living Brain orchestrator")
    sub = parser.add_subparsers(dest="command", required=True)

    p_boot = sub.add_parser("bootstrap", help="Scaffold + grow + wire + neural map")
    p_boot.add_argument("--grow", type=int, default=300)
    p_boot.add_argument("--dry-run", action="store_true")

    p_grow = sub.add_parser("grow", help="Grow domain documents")
    p_grow.add_argument("--count", type=int, default=200)
    p_grow.add_argument("--dry-run", action="store_true")

    sub.add_parser("structure", help="Create folder tree only")
    sub.add_parser("synapses", help="Wire hub synapses")
    sub.add_parser("reflexes", help="Seed reflex FAQs")
    sub.add_parser("map", help="Rebuild neural-map.json")

    args = parser.parse_args()

    if args.command == "bootstrap":
        result = bootstrap(grow=args.grow, dry_run=args.dry_run)
    elif args.command == "grow":
        _ensure_structure()
        result = grow_domains(args.count, dry_run=args.dry_run)
        if not args.dry_run:
            result["neural_map"] = build_neural_map()
    elif args.command == "structure":
        result = {"structure": str(_ensure_structure()["root"])}
    elif args.command == "synapses":
        result = wire_synapses()
        result["neural_map"] = build_neural_map()
    elif args.command == "reflexes":
        result = seed_reflexes()
        result["neural_map"] = build_neural_map()
    elif args.command == "map":
        result = build_neural_map()
    else:
        result = {"error": "unknown command"}

    print(yaml.safe_dump(result, sort_keys=False))


if __name__ == "__main__":
    main()
