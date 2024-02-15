import mii
"""
client = mii.serve(
    "TheBloke/Mixtral-8x7B-Instruct-v0.1-GPTQ",
    deployment_name="generate",
    enable_restful_api=True
)
"""
pipe = mii.pipeline("mistralai/Mistral-7B-v0.1")
response = pipe([
    "[INST] Как получать в логах только нужные поля при использовании обработчика loguru с параметром serialize=True [/INST]",
    "Как получать в логах только нужные поля при использовании обработчика loguru с параметром serialize=True"
    ], max_new_tokens=1500)
print(response)