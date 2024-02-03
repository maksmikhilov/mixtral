from model_request.general.const_values import metrics, get_unique_values, get_first_rows
from utils import model_request

    
def get_prompt(df, request, columns_analysis_result):
    prompt = f"""
Ты аналитик данных с опытом 20 лет. 
Все 20 лет ты анализируешь только одну таблицу, и знаешь все её нюансы.
За качественно выполненную работу тебе дадут премию.
Если ты облажаешься, тебя уволят.

Напомню тебе информацию о таблице, с которой ты работаешь.
<table_info>
    Анализ столбцов: 
    <columns_analysis>
        {columns_analysis_result}
    </columns_analysis>

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

<task>
    Твоя работа - составлять последовательное техническое задание (step by step) по получению данных из таблицы на основе запроса Босса, используя <table_info>
</task>

Шаблон твоего ответа:
<template>
1. <цель пункта>
  1.1. <подпункт по достижению цели и его подробное описание>
  1.2. <подпункт по достижению цели и его подробное описание>
  1.3. <подпункт по достижению цели и его подробное описание>
2. <цель пункта>
  2.1. <подпункт по достижению цели и его подробное описание>
  2.2. <подпункт по достижению цели и его подробное описание>
</template>

Вот запрос, на основе которого ты должен написать техническое задание:
<request>
  {request}
</request>
    """
    return prompt
    
def get_response(df, request, columns_analysis_result, model_params):
    prompt = get_prompt(df, request, columns_analysis_result)
    print(prompt)
    gpt_response = model_request(
        prompt,
        model_params
    )
    print(gpt_response)
    return gpt_response