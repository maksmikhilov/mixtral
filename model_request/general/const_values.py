import ast
def get_columns(df):
    columns = df.columns.tolist()
    return str(columns)

def get_unique_values(df):
    columns = ast.literal_eval(get_columns(df))
    unique_values = ''
    count_values = 0
    for i, column in enumerate(columns):
        if len(df[column].unique()) < 15:
            count_values += 1
            unique_values += f'{count_values}. Столбец [{column}] имеет следующие уникальные значения: {df[column].unique()}.\n'
    return unique_values

def get_first_rows(df):
    rows = str()
    enter = ''
    for i in range(3):
        if i:
            enter = '\n'
        rows += f'{enter}{df.iloc[i].to_dict()}'
    return rows
        


metrics = """
Средняя Абонентская База = (Абоненты на конец периода + Абоненты на начало периода) / 2;

Churn rate = Отток / Средняя Абонентская База;

ARPU = Доходы / Средняя Абонентская База;

GBOU = Трафик СПД / Средняя Абонентская База;

MOU = Голосовой трафик / Средняя Абонентская База Телефонии;
"""