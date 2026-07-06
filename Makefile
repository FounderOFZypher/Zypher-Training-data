.PHONY: install validate generate prepare pipeline train-xs index chat infer clean

install:
	pip install -r requirements.txt

validate:
	python3 scripts/validate_pipeline.py

# Generate ~112k knowledge files at scale=1000 (use SCALE=10 for quick smoke test)
generate:
	python3 scripts/generate_corpus.py --scale $(or $(SCALE),1000)

generate-smoke:
	python3 scripts/generate_corpus.py --scale 1000 --max-files 2000

# Build Zypher training dataset → data/zypher/
prepare:
	python3 scripts/prepare_advanced_dataset.py

# Corpus → Zypher dataset
pipeline: generate-smoke prepare
	@echo "Pipeline complete. See data/zypher/dataset_stats.json"

# Fine-tune base model on Zypher dataset → Zypher XS adapter
train-xs:
	python3 scripts/train.py --config config/zypher_xs.yaml

# Index knowledge base for Enterprise RAG
index:
	python3 -m zypher.chat --reindex --index-only

# Final chatbot: Zypher XS + Enterprise RAG
chat:
	python3 -m zypher.chat

# Raw model inference (no RAG)
infer:
	python3 scripts/infer.py \
		--base-model poolside/Laguna-XS-2.1 \
		--adapter outputs/zypher-xs/final \
		--question "Explain GraphRAG for code architecture."

clean:
	rm -rf data/vector_store outputs/ knowledge-base/generated __pycache__ scripts/__pycache__ zypher/__pycache__
