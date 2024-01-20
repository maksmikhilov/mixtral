from transformers import AutoTokenizer, BitsAndBytesConfig, AutoModelForCausalLM
import torch
from SheetsGPT_steps import table_analys, request_analys, generate_code
import requests
device = "cuda"
model_id = "mistralai/Mixtral-8x7B-v0.1"
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16
)

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, quantization_config=quantization_config, use_flash_attention_2=True)
def inference(prompt):
    prompt = tokenizer(prompt, return_tensors="pt").to(device)
    response = model.generate(
        **prompt,
        max_new_tokens=2048,
        temperature=0.1,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )
    return tokenizer.decode(response[0], skip_special_tokens=True)
    
def text_alert(text):
    base_url = 'https://mm-tradebot-2.ru/chat_gpt'
    text_data = {
        'text': text
    }
    requests.post(
        f'{base_url}/text_alert',
        json=text_data
        )
    
while True:
    request = input('Введите запрос')
    
    table_analys_prompt = table_analys.get_prompt()
    table_analys_result = inference(table_analys_prompt)
    text_alert(table_analys_result)
    
    request_analys_prompt = request_analys.get_prompt(request, table_analys_result)
    request_analys_result = inference(table_analys_prompt)
    text_alert(request_analys_result)
    
    generate_code_prompt = generate_code.get_prompt(table_analys_result, request_analys_result)
    generate_code_result = inference(generate_code_prompt)
    text_alert(generate_code_result)
    