import mii
pipe = mii.pipeline("mistralai/Mistral-7B-Instruct-v0.2", tensor_parallel=2, max_length=1000)
response = pipe(["[INST] Как получать в логах только нужные поля при использовании обработчика loguru с параметром serialize=True [/INST]", "Как получать в логах только нужные поля при использовании обработчика loguru с параметром serialize=True"], max_new_tokens=2000)
print(response)