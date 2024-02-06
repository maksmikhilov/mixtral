from model_request.general.const_values import data_types, column_relations, formulas, get_unique_values, get_first_rows, get_columns
import utils


def get_prompt(df, request_analysis_result):
    prompt = f"""Ты Python программист с опытом 20 лет.

Твоя задача — написать код по техническому заданию от аналитика данных. Техническое задание описывает как правильно исполнить запрос к таблице. Ниже предоставлена иформация о таблице:

1. Таблица имеет следующие столбцы и типы данных в них:
<data_types>
{data_types}
</data_types>

2. Ключевые связи между столбцами таблицы:
<column_relations>
{column_relations}
</column_relations>

3. Первые три строки этой таблицы:
<first_rows>
{get_first_rows(df)}
</first_rows>

4. Столбцы с уникальными значениями:
<unique_values>
{get_unique_values(df)}
</unique_values>

5. Ключевые формулы для вычислений:
<formulas>
{formulas}
</formulas>

Напиши код на Python, СТРОГО СОБЛЮДАЯ техническое задание:
'''
{request_analysis_result}

Требования к коду:
1) Таблица уже находится в переменной df;
2) Результат помести в переменную code_result;
'''

Формат твоего ответа:
```python
<код>
```
"""
    return prompt
    
    
def get_response(llm, params, df, request, request_analysis_result):
    prompt = get_prompt(df, request, request_analysis_result)
    outputs = llm.generate([prompt], params)
    for output in outputs:
        generated_text = output.outputs[0].text
    utils.text_alert(generated_text)
    return generated_text