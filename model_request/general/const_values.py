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
        
data_types = """
1. dt - дата. Формат данных - дата;
2. region_key - признак. Формат данных - строка;
3. region_name - признак. Формат данных - строка;
4. business_unit - признак. Формат данных - строка;
5. macroregion_name - признак. Формат данных - строка;
6. name_prnt_segm_level_1 - признак. Формат данных - строка;
7. business_service_name - признак. Формат данных - строка;
8. service_name - признак. Формат данных - строка;
9. tech - признак. Формат данных - строка;
10. macro_tech - признак. Формат данных - строка;
11. service_detail - признак. Формат данных - строка;
12. macro_kpi - признак. Формат данных - строка;
13. unit - признак. Формат данных - строка;
14. kpi_value - показатель. Формат данных - число с плавающей точкой;
"""

column_relations = """
1. macro_kpi - ключ, а kpi_value - его значение;
2. business_service_name - категория, а service_name - его подкатегория;
3. kpi_value - значение, а unit - его единица измерения;
"""

formulas = """
1. Абоненты на конец периода = SUM(kpi_value) при macro_kpi == 'Абонентская на конец периода';
2. Абоненты на начало периода = SUM(kpi_value) при macro_kpi == 'Абонентская на начало периода';
3. Отток = SUM(kpi_value) при macro_kpi == 'Отток';
4. Доходы = SUM(kpi_value) при macro_kpi == 'Доходы';
5. Трафик СПД = SUM(kpi_value) при macro_kpi == 'Трафик СПД';
6. Голосовой трафик = SUM(kpi_value) при macro_kpi == 'Голосовой трафик';
7. Абоненты на конец периода ШПД = SUM(kpi_value) при macro_kpi == 'Абонентская на конец периода' и service_name == 'ШПД';
8. Абоненты на начало периода ШПД = SUM(kpi_value) при macro_kpi == 'Абонентская на начало периода' и service_name == 'ШПД';
9. Абоненты на конец периода Телефонии = SUM(kpi_value) при macro_kpi == 'Абонентская на конец периода' и business_service_name == 'Телефония (фиксированная)';
10. Абоненты на начало периода Телефонии = SUM(kpi_value) при macro_kpi == 'Абонентская на начало периода' и business_service_name == 'Телефония (фиксированная)';
11. Средняя абонентская база = (Абоненты на конец периода + Абоненты на начало периода) / 2;
12. Churn rate = Отток / Средняя абонентская база;
13. ARPU = Доходы / Средняя абонентская база;
14. GBOU = Трафик СПД / Средняя абонентская база ШПД;
15. MOU = Голосовой трафик / Средняя абонентская юаза Телефонии;
16. Средняя абонентская база ШПД = (Абоненты на конец периода ШПД + Абоненты на начало периода ШПД) / 2;
17. Средняя абонентская база Телефонии = (Абоненты на конец периода Телефонии + Абоненты на начало периода Телефонии) / 2;
"""