from gpt_request.const_values import get_columns, get_unique_values, get_first_rows
from gpt_request.utils import gpt_request


model = 'gpt-3.5-turbo-1106'

def get_prompt(df, request, table_analys_result, request_analys_result, classifier_request_result):
    prompt = f"""Твоя задача написать код на python на основе технического задания, который выполняет запрос к таблице. Вот формулировка этого запроса:
'''
{request}
'''

Вот техническое задание:
'''
Шаги по выполнению запроса:
{request_analys_result}

Формат данных результата исполнения запроса:
Таблица/массив данных на основе которых можно построить график {classifier_request_result}

Требования к коду:
1) Читать таблицу не надо, csv таблица уже находится в переменной df.
2) Результат должен находиться в переменной code_result и должен строго соответствовать указанному формату данных.
3) Код должен быть чистым, без ошибок и эффективным.
'''

Тебе предоставлено описание таблицы к котрой делается запрос:
'''
{table_analys_result}
'''

Таблица содержит следующие столбцы: {get_columns(df)}

Нижеперечисленные столбцы являются ключевыми и имеют уникальные значения:
'''
{get_unique_values(df)}
'''

Пример первых трех строк этой таблицы:
'''
{get_first_rows(df)}
'''

Формат ответа:
'''
```python
<код>
```
"""
    return prompt
    
async def get_response(df, request, table_analys_result, request_analys_result, classifier_request_result):
    prompt = get_prompt(request)
    print(prompt)
    gpt_response = await gpt_request(prompt, model, 0.3)
    return gpt_response