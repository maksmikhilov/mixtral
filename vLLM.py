from vllm import LLM, SamplingParams
from model_request.general import reformulation_request as reformulation_request_general
from model_request.general import request_analysis as request_analysis_general
from model_request.general import generate_code as generate_code_general
import torch
import pandas as pd
import utils
params = SamplingParams(temperature=0.8, top_p=0.95)

print('Загружаем модель')
llm = LLM(
    model="TheBloke/Mixtral-8x7B-Instruct-v0.1-GPTQ",
    quantization="gptq",
    tensor_parallel_size=2,
    dtype=torch.float16,
    revision="main",
    max_model_len=500,
    enforce_eager=True,
    download_dir='/home/ubuntu/models_weight',
    )
print('Загружаем таблицу')
df = pd.read_excel('test.xlsx')

request = """Вычислить ARPU для услуги 'Телефония (фиксированная)' отдельно по каждому макрорегиону без учёта ШПД"""

# Переформулировка
request = reformulation_request_general.get_response(llm, params, df, request)
print(request)

# Составление плана
request_analysis_result = request_analysis_general.get_response(llm, params, df, request)
print(request_analysis_result)

# Генерация кода
generate_code_result = generate_code_general.get_response(llm, params, df, request, request_analysis_result)
print(generate_code_result)
    
code_result = utils.exec_code(generate_code_result, df)

if code_result.get('err'):
    utils.text_alert(code_result['err'])
    print(code_result['err'])
else:
    utils.text_alert(code_result['code_result'])
    print(code_result['code_result'])