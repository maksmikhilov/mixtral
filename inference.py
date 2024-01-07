from transformers import AutoTokenizer, BitsAndBytesConfig, AutoModelForCausalLM
import torch
from get_prompt import get_prompt

device = "cuda"
model_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16
)

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, quantization_config=quantization_config)
prompt = get_prompt('Вычисли GBOU для Урала за каждый месяц 2020 года и выведи значения в виде таблицы.')

inputs = tokenizer(prompt, return_tensors="pt").to(device)
output = model.generate(
    **inputs,
    max_new_tokens=2048,
    temperature=0.1,
    do_sample=True,
    pad_token_id=tokenizer.eos_token_id
    )
print(tokenizer.decode(output[0], skip_special_tokens=True))