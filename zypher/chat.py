#!/usr/bin/env python3
"""Zypher final chatbot CLI — Enterprise RAG + Zypher XS."""

from __future__ import annotations

import argparse

from zypher.backend import ZypherBackend


def main() -> None:
    parser = argparse.ArgumentParser(description="Zypher enterprise chatbot")
    parser.add_argument("--xs-config", default="config/zypher_xs.yaml")
    parser.add_argument("--rag-config", default="config/rag.yaml")
    parser.add_argument("--reindex", action="store_true", help="Rebuild vector index")
    parser.add_argument("--index-only", action="store_true", help="Index KB and exit")
    parser.add_argument("--question", default=None, help="Single question (non-interactive)")
    args = parser.parse_args()

    from zypher.config import load_config

    config = load_config(args.xs_config, args.rag_config)
    backend = ZypherBackend(config)

    print(f"Knowledge base: {len(backend.kb)} documents")
    if args.reindex or args.index_only or backend.vector_store._collection is None:
        n = backend.index_knowledge_base()
        print(f"Indexed {n} documents into vector store")

    if args.index_only:
        return

    if args.question:
        print(backend.chat(args.question))
        return

    print("Zypher Chatbot (Enterprise RAG + Zypher XS). Type 'quit' to exit.\n")
    while True:
        user = input("You: ").strip()
        if user.lower() in {"quit", "exit"}:
            break
        print(f"Zypher: {backend.chat(user)}\n")


if __name__ == "__main__":
    main()
