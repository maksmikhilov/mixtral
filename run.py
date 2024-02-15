import mii
pipe = mii.pipeline("mistralai/Mistral-7B-v0.2", tensor_parallel=4)
response = pipe(["[INST] Как получать в логах только нужные поля при использовании обработчика loguru с параметром serialize=True [/INST]", "Как получать в логах только нужные поля при использовании обработчика loguru с параметром serialize=True"], max_new_tokens=1000)
print(response)