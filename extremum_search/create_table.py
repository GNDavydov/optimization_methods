# Copyright 2021 GNDavydov

import pandas as pd


def create_table(table_values, table_name):
    '''
    Функция создает таблицу с указанными параметрами и названием

    :param table_values: Словарь значений, где в качестве ключа выступает название столбца,
    а в качестве строчек данные по этому ключу
    :param table_name: Название таблицы
    :return:
    '''

    pd.set_option('display.max_rows', None)
    table = pd.DataFrame(table_values)
    table.to_excel(table_name, index=False)
