import llama_cpp
from outlines import models
from vllm import LLM


def loadLlamaModel(
    repoId: str = "NousResearch/Hermes-2-Pro-Llama-3-8B-GGUF",
    fileName: str = "Hermes-2-Pro-Llama-3-8B-Q4_K_M.gguf",
    tokenizer: str = "NousResearch/Hermes-2-Pro-Llama-3-8B",
):
    model = models.llamacpp(
        repo_id=repoId,
        filename=fileName,
        tokenizer=llama_cpp.llama_tokenizer.LlamaHFTokenizer.from_pretrained(tokenizer),
        n_gpu_layers=-1,
        flash_attn=True,
        n_ctx=8192,
        verbose=False,
    )

    return model


# ! Either use the load model classes for both or perform inference via docker container
# ! docker run -p 8000:8000 outlinesdev/outlines --model="microsoft/Phi-3-mini-4k-instruct"


def loadLlamaModelvLLM(
    repoId: str = "NousResearch/Hermes-2-Pro-Llama-3-8B-GGUF",
    fileName: str = "Hermes-2-Pro-Llama-3-8B-Q4_K_M.gguf",
    tokenizer: str = "NousResearch/Hermes-2-Pro-Llama-3-8B",
):
    model = LLM(
        model=repoId,
        tokenizer=tokenizer,
        trust_remote_code=True,
        quantization="nf4",
        gpu_memory_utilization=0.8,
    )

    return model


def loadLocalModelvLLM(
    path: str,
):
    model = LLM(
        model=path,
        tokenizer_mode="auto",
        gpu_memory_utilization=0.8,
        quantization="nf4",
    )
    return model
