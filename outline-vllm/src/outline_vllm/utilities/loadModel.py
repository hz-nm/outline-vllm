import llama_cpp
from outlines import generate, models

model = models.llamacpp("NousResearch/Hermes-2-Pro-Llama-3-8B-GGUF",
            "Hermes-2-Pro-Llama-3-8B-Q4_K_M.gguf",
            tokenizer=llama_cpp.llama_tokenizer.LlamaHFTokenizer.from_pretrained(
            "NousResearch/Hermes-2-Pro-Llama-3-8B"
            ),
            n_gpu_layers=-1,
            flash_attn=True,
            n_ctx=8192,
            verbose=False)