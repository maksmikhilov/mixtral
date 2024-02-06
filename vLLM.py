from vllm import LLM, SamplingParams
import torch
prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

llm = LLM(
    model="TheBloke/Mixtral-8x7B-Instruct-v0.1-GPTQ",
    quantization="gptq",
    dtype=torch.float16,
    revision="main",
    gpu_memory_utilization=0.75,
    disable_custom_all_reduce=True,
    enforce_eager=True,
    download_dir='/home/ubuntu/models_weight',
    )

outputs = llm.generate(prompts, sampling_params)

for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")