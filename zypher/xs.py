from __future__ import annotations

from pathlib import Path

import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

from zypher.config import ZypherConfig


class ZypherXS:
    """Fine-tuned Zypher XS model (base: poolside/Laguna-XS-2.1 + LoRA adapter)."""

    def __init__(self, config: ZypherConfig):
        self.config = config
        inf = config.xs.get("inference", {})
        self.max_new_tokens = int(inf.get("max_new_tokens", 1024))
        self.temperature = float(inf.get("temperature", 0.7))
        self.top_p = float(inf.get("top_p", 0.9))

        adapter = config.adapter_path
        if not (adapter / "adapter_config.json").exists():
            raise FileNotFoundError(
                f"Zypher XS adapter not found at {adapter}. "
                "Run `make train-xs` to fine-tune on the Zypher dataset first."
            )

        base = config.base_model
        trust = config.xs["model"].get("trust_remote_code", True)

        tok_src = adapter if (adapter / "tokenizer_config.json").exists() else base
        self.tokenizer = AutoTokenizer.from_pretrained(tok_src, trust_remote_code=trust)
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        quant = None
        if torch.cuda.is_available() and config.xs["model"].get("load_in_4bit", True):
            quant = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_quant_type="nf4",
                bnb_4bit_compute_dtype=torch.bfloat16,
                bnb_4bit_use_double_quant=True,
            )

        self.model = AutoModelForCausalLM.from_pretrained(
            base,
            quantization_config=quant,
            device_map="auto",
            trust_remote_code=trust,
            torch_dtype=torch.bfloat16 if torch.cuda.is_available() else torch.float32,
        )
        self.model = PeftModel.from_pretrained(self.model, str(adapter))
        self.model.eval()

    def generate(self, messages: list[dict[str, str]]) -> str:
        if hasattr(self.tokenizer, "apply_chat_template") and self.tokenizer.chat_template:
            prompt = self.tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True
            )
        else:
            parts = [f"{m['role']}: {m['content']}" for m in messages]
            prompt = "\n".join(parts) + "\nassistant:"

        inputs = self.tokenizer(prompt, return_tensors="pt")
        if torch.cuda.is_available():
            inputs = {k: v.to(self.model.device) for k, v in inputs.items()}

        with torch.no_grad():
            out = self.model.generate(
                **inputs,
                max_new_tokens=self.max_new_tokens,
                do_sample=True,
                temperature=self.temperature,
                top_p=self.top_p,
                pad_token_id=self.tokenizer.eos_token_id,
            )
        new_ids = out[0][inputs["input_ids"].shape[1] :]
        return self.tokenizer.decode(new_ids, skip_special_tokens=True).strip()
