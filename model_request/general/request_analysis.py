from model_request.general.const_values import data_types, column_relations, formulas, get_unique_values, get_first_rows, get_columns
import utils

def get_prompt(df, request):
    prompt = f"""
Ты аналитик данных с опытом 20 лет.

Твоя задача — составить детальное техническое задание по исполнению запроса к таблице. Результат должен соответствовать типу данных, который обозначен в запросе. Ниже предоставлена информация о таблице:

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

Примечания:
1) Используй для вычислений столбцы с типом "Показатель".
2) ОБЯЗАТЕЛЬНО учитывай связи между столбцами из блока <column_relations> при составлении формул!

Ответ пиши ТОЛЬКО по этому шаблону:
'''
1. Вычислить [Значение] для [Фильтр] [Группировка], [Фильтр]:
    1.1 Выбрать данные по [Фильтр] и исключить данные по [Фильтр];
    1.2 Сгруппировать данные по [Группировка];
    1.3 Рассчитать [Значение], где
        1.3.1 [Параметр] = [Операция (Столбец)] при [Фильтр] и [Фильтр];
        1.3.2 [Параметр] = ([Значение 1] + [Значение 2]) / 2, где:
            1.3.2.1 [Значение 1] = [Операция (Столбец)] при [Фильтр] и [Фильтр];
            1.3.2.2 [Значение 2] = [Операция (Столбец)] при [Фильтр] и [Фильтр];

Формат вывода - <формат вывода из запроса Босса>.            
'''


Вот запрос Босса:
{request}"""
    return prompt
    
def get_response(llm, params, df, request):
    prompt = get_prompt(df, request)
    outputs = llm.generate([prompt], params)
    for output in outputs:
        generated_text = output.outputs[0].text
    utils.text_alert(generated_text)
    return generated_text