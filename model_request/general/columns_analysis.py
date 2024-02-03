from model_request.general.const_values import metrics, get_columns, get_unique_values, get_first_rows
from utils import model_request

model = 'gpt-3.5-turbo-1106'

    
def get_prompt(df, request):
    prompt = f"""
Ты аналитик данных с опытом 20 лет. 
За качественно выполненную работу тебе дадут 200$.

Информация о таблице:
<table_info>
    Таблица имеет столбцы: 
    <columns>
        {get_columns(df)}
    </columns>

    Первые три строки из этой таблицы:
    <rows>
        {get_first_rows(df)}
    </rows>
    
    Ключевые столбцы имеют следующие уникальные значения:
    {get_unique_values(df)}

    Подсказки к таблице:
    <hints>
        {metrics}
    </hints>
</table_info>

<task>
ВАЖНО! От тебя требуется выявить ВСЕ группы столбцов, которые имеют между собой связь, используя <table_info>. Шаблон для твоего ответа:
<template>
1. <первая группа связанных между собой столбцов> — <кто, с кем и как связан>. <как использовать эту связь>
2. <вторая группа связанных между собой столбцов> — <кто, с кем и как связан>. <как использовать эту связь>
</template>
Групп может быть сколь угодно много,
</task>

Вот запрос в контексте которого ты должен провести углубленный анализ столбцов таблицы:
<request>
  {request}
</request>
    """
    return prompt
    
def get_response(df, request, model_params):
    prompt = get_prompt(df, request)
    print(prompt)
    gpt_response = model_request(
        prompt,
        model_params
    )
    print(gpt_response)
    return gpt_response