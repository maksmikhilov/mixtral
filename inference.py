from transformers import AutoTokenizer, BitsAndBytesConfig, AutoModelForCausalLM
import torch
from model_request.general import columns_analysis
from model_request.general import reformulation_request as reformulation_request_general
from model_request.general import request_analysis as request_analysis_general
from model_request.general import generate_code as generate_code_general
import requests
import pandas as pd
import utils

model_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16
)

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, quantization_config=quantization_config)
    
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
    model_params = {
        'tokenizer': tokenizer,
        'model': model
    }
    df = pd.read_excel('test.xlsx')
    
    # Переформулировка
    request = reformulation_request_general.get_response(df, request, model_params)
    text_alert(request)
    
    # Анализ колонок
    columns_analysis_result = columns_analysis.get_response(df, request, model_params)
    text_alert(columns_analysis_result)

    # Составление плана 
    request_analysis_result = request_analysis_general.get_response(df, request, columns_analysis_result, model_params)
    text_alert(request_analysis_result)
    
    # Генерация кода
    generate_code_result = generate_code_general.get_response(df, request, columns_analysis_result, request_analysis_result, model_params)
    text_alert(generate_code_result)
    
    code_result = utils.exec_code(generate_code_result, df)

    if code_result.get('err'):
        text_alert(code_result['err'])
    else:
        text_alert(code_result['code_result'])
    