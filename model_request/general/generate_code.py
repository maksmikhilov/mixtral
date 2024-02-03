from model_request.general.const_values import get_columns, get_unique_values, get_first_rows, metrics
from utils import model_request

    
def get_prompt(df, request, columns_analysis_result, request_analysis_result):
    prompt = f"""
Ты python программист с опытом 20 лет. Все 20 лет ты работаешь с одной таблицей и знаешь все её нюансы. Твоя работа заключается в том, чтобы писать код, который исполняет запрос Босса к таблице. 

Напомню тебе информацию о таблице, с которой ты работаешь.
<table_info>
    Таблица имеет столбцы: 
    <columns>
        {columns_analysis_result}
    </columns>

    Первые три строки из этой таблицы:
    <rows>
        {get_first_rows(df)}
    </rows>

    Ключевые столбцы имеют следующие уникальные значения:
    <unique_values>
        {get_unique_values(df)}
    </unique_values>

    Подсказки к таблице:
    <hints>
        {metrics}
    </hints>
</table_info>

Аналитик данных уже проанализировал запрос Босса и написал тебе пошаговую инструкцию со списком переменных. Я передам тебе инструкцию и список переменных от аналитика и запрос босса, а ты напишешь код, основываясь на этом. Внимательно соблюдай пункты инструкции и описания переменных. Аналитик иногда может упустить некоторые детали, поэтому буду надеяться на твой многолетний опыт.

К коду есть некоторые требования:
1) Таблица уже находится в переменной df;
2) Результат помести в переменную code_result;
3) Результат должен соответствовать типу данных, который обозначен в запросе Босса;
4) Код должен быть чистым, эффективным и без ошибок.

Вот запрос Босса:
'''
{request}
'''

Инструкция от аналитика:
'''
{request_analysis_result}
'''

Формат твоего ответа:
```python
<код>
```
    """
    return prompt
    

def get_response(df, request, columns_analysis_result, request_analysis_result, model_params):
    prompt = get_prompt(df, request, columns_analysis_result, request_analysis_result)

    print(prompt)
    gpt_response = model_request(
        prompt,
        model_params,
    )
    return gpt_response