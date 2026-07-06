#!/usr/bin/env python3
"""Validate repo setup, Zypher dataset, and Zypher XS adapter."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def check(name: str, ok: bool, detail: str = "") -> bool:
    status = "OK" if ok else "FAIL"
    line = f"[{status}] {name}"
    if detail:
        line += f" — {detail}"
    print(line)
    return ok


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate Zypher training pipeline")
    parser.add_argument(
        "--require-adapter",
        action="store_true",
        help="Fail if Zypher XS adapter is missing",
    )
    args = parser.parse_args()

    root = Path(".")
    all_ok = True

    for pkg in ("torch", "yaml", "transformers"):
        try:
            __import__(pkg if pkg != "yaml" else "yaml")
            check(f"import {pkg}", True)
        except ImportError:
            all_ok = check(f"import {pkg}", False, "run: pip install -r requirements.txt")

    for path in (
        "config/zypher_xs.yaml",
        "config/rag.yaml",
        "config/corpus_generation.yaml",
        "requirements.txt",
    ):
        all_ok = check(f"file {path}", (root / path).exists()) and all_ok

    data_files = {
        "data/zypher/train.jsonl": "Run: make prepare",
        "data/zypher/val.jsonl": "Run: make prepare",
    }
    for path, hint in data_files.items():
        p = root / path
        ok = p.exists() and p.stat().st_size > 0
        all_ok = check(f"data {path}", ok, hint if not ok else f"{p.stat().st_size:,} bytes") and all_ok

    stats_path = root / "data/zypher/dataset_stats.json"
    if stats_path.exists():
        stats = json.loads(stats_path.read_text(encoding="utf-8"))
        all_ok = check(
            "training examples",
            stats.get("total_examples", 0) > 0,
            str(stats.get("total_examples")),
        ) and all_ok

    adapter = root / "outputs/zypher-xs/final/adapter_config.json"
    adapter_ok = adapter.exists()
    if args.require_adapter:
        all_ok = check("Zypher XS adapter", adapter_ok, str(adapter)) and all_ok
    else:
        check(
            "Zypher XS adapter",
            adapter_ok,
            "Run: make train-xs" if not adapter_ok else str(adapter.parent),
        )

    kb_count = len(list((root / "knowledge-base").rglob("CHUNK-*.md"))) if (root / "knowledge-base").exists() else 0
    all_ok = check("seed knowledge-base chunks", kb_count > 0, f"{kb_count} files") and all_ok

    zypher_pkg = root / "zypher/backend.py"
    all_ok = check("zypher package", zypher_pkg.exists()) and all_ok

    if not all_ok:
        print("\nValidation failed. Fix the items above before training.")
        sys.exit(1)

    print("\nValidation passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
