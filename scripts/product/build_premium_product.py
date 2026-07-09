#!/usr/bin/env python3
"""Build Coltex Mega RAG — commercial 100,000,000+ document corpus."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

PREMIUM_STEPS = [
    ("stream_premium_corpus", "Stream Mega RAG commercial corpus"),
    ("build_marketplace_packs", "Build sellable marketplace pack catalog"),
    ("validate_quality", "Validate quality gates"),
    ("build_benchmarks", "Build benchmark datasets"),
    ("build_manifest", "Build product manifest"),
    ("audit_distribution", "Audit distribution compliance"),
]


def run_step(script: str, config: Path, extra: list[str] | None = None) -> None:
    cmd = [sys.executable, str(Path(__file__).parent / f"{script}.py"), "--config", str(config)]
    if extra:
        cmd.extend(extra)
    print(f"\n=== {script} ===")
    subprocess.run(cmd, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build Coltex Mega RAG commercial dataset (100M+)")
    parser.add_argument("--config", type=Path, default=Path("config/product_mega.yaml"))
    parser.add_argument("--max-files", type=int, default=None)
    parser.add_argument("--skip-embeddings", action="store_true")
    parser.add_argument("--skip-eval", action="store_true", default=True)
    parser.add_argument("--skip-marketplace", action="store_true")
    args = parser.parse_args()

    extra = []
    if args.max_files is not None:
        extra = ["--max-files", str(args.max_files)]

    run_step("stream_premium_corpus", args.config, extra or None)

    for script, _ in PREMIUM_STEPS[1:]:
        if args.skip_marketplace and script == "build_marketplace_packs":
            continue
        run_step(script, args.config)

    if not args.skip_embeddings:
        run_step("export_embeddings", args.config)

    if not args.skip_eval:
        run_step("evaluate_rag", args.config)

    print("\nColtex Mega RAG commercial build complete (target: 100,000,000+ documents).")


if __name__ == "__main__":
    main()
