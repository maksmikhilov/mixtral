from transformers import AutoTokenizer, BitsAndBytesConfig, AutoModelForCausalLM
import torch

model_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16
)

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, quantization_config=quantization_config)
prompt = 'Как зовут В.В.Путина?'
inputs = tokenizer(prompt, return_tensors="pt").to(0)
output = model.generate(**inputs, max_new_tokens=50)
print(tokenizer.decode(output[0], skip_special_tokens=True))