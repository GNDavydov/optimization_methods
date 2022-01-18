# Copyright 2021 GNDavydov

import numpy as np

from extremum_search.create_table import create_table

'''
Методы поиска экстремума унимодальной функции одного переменного

Включает:
 1) метод пассивного поиска
 2) метод золотого сечения
 3) поиск методом Фибоначчи
'''


def passive_search(a, b, e, fun, table_name='passive_search.xlsx'):
    '''
    Функция, осуществляющая оптимальный пассивный поиск экстремума функции fun(x) на отрезке [a, b]

    :param a: Начальная граница отрезка
    :param b: Конечная граница отрезка
    :param e: Максимальная длина интервала неопределенности
    :param fun: Исходная функция
    :param table_name: Название таблицы, куда будет сохранен поиск
    :return: минимум функции f(x)
    '''
    n = np.ceil(2 * (b - a) / e).astype(int) - 1
    delta = (b - a) / (n + 1)

    table_params = {
        'N': list(range(1, n + 1)),
        'x_array': list(),
        'fun_array': list()
    }

    for i in range(1, n + 1):
        x_i = a + i * delta

        table_params['x_array'].append(x_i)
        table_params['fun_array'].append(fun(x_i))

    fun_min = np.min(table_params['fun_array'])
    x_min = table_params['x_array'][table_params['fun_array'].index(fun_min)]

    create_table(table_params, table_name)
    return x_min


def golden_ratio(a, b, e, fun, table_name='golden_ratio.xlsx'):
    '''
    Функция, осуществляющая последовательный поиск экстремума функции fun(x) на отрезке [a, b]
    с помощью метода золотого сечения

    :param a: Начальная граница отрезка
    :param b: Конечная граница отрезка
    :param e: Максимальная длина интервала неопределенности
    :param fun: Исходная функция
    :param table_name: Название таблицы, куда будет сохранен поиск
    :return: минимум функции f(x)
    '''

    phi = (1 + np.sqrt(5)) / 2
    length = b - a
    x1 = b - length / phi
    x2 = a + length / phi

    table_params = {
        'a': list(),
        'b': list(),
        'x1': list(),
        'x2': list(),
        'f(x1) >= f(x2)': list(),
        'a*': list(),
        'b*': list(),
    }

    while length > e:
        table_params['a'].append(a)
        table_params['b'].append(b)
        table_params['x1'].append(x1)
        table_params['x2'].append(x2)

        if fun(x1) >= fun(x2):
            table_params['f(x1) >= f(x2)'].append('YES')
            a = x1
            length = b - a
            x1 = x2
            x2 = a + length / phi
        else:
            table_params['f(x1) >= f(x2)'].append('NO')
            b = x2
            length = b - a
            x2 = x1
            x1 = b - length / phi

        table_params['a*'].append(a)
        table_params['b*'].append(b)

    x_min = (a + b) / 2

    create_table(table_params, table_name)
    return x_min


def fibonacci_numbers(n):
    '''
    Функция для нахождения числа Фибоначчи

    :param n: (int) натуральное число
    :return: число фибоначчи для заданного n
    '''
    if n > 2:
        return fibonacci_numbers(n - 1) + fibonacci_numbers(n - 2)
    return 1


def method_fibonacci(a, b, e, fun, table_name="fibonacci.xlsx"):
    '''
    Функция реализует метод Фибоначчи
    для нахождения минимума функции func
    на интервале [a,b] с точностью e

    :param a: начало заданного интервала
    :param b: конец заданного интервала
    :param e: точность, с которой надо найти минимум
    :param fun: исходная функция
    :param table_name: Название таблицы, куда будет сохранен поиск
    :return: минимум функции f(x)
    '''
    n = 1
    len0 = b - a
    while fibonacci_numbers(n) < (b - a) / e:
        n += 1

    table_params = {
        "x": list(),
        "func(x)": list(),
        "left": list(),
        "right": list(),
        "func(left)": list(),
        "func(right)": list(),
        "func(left) > func(right)": list(),
        "epsilon": list()
    }

    x1 = a + (b - a) * fibonacci_numbers(n - 1) / fibonacci_numbers(n + 1)
    x2 = a + (b - a) * fibonacci_numbers(n) / fibonacci_numbers(n + 1)

    table_params["left"].append(x1)
    table_params["func(left)"].append(fun(x1))
    table_params["right"].append(x2)
    table_params["func(right)"].append(fun(x2))
    table_params["x"].append((x2 + x1) / 2)
    table_params["func(x)"].append(fun((x2 + x1) / 2))
    table_params["epsilon"].append((b - a) / 2)

    for i in range(2, n):
        if fun(x1) > fun(x2):
            table_params["func(left) > func(right)"].append("YES")
            a = x1
            x1 = x2
            x2 = a + len0 * fibonacci_numbers(n - i + 1) / fibonacci_numbers(n + 1)
        else:
            table_params["func(left) > func(right)"].append("NO")
            b = x2
            x2 = x1
            x1 = a + len0 * fibonacci_numbers(n - i) / fibonacci_numbers(n + 1)
        table_params["left"].append(x1)
        table_params["func(left)"].append(fun(x1))
        table_params["right"].append(x2)
        table_params["func(right)"].append(fun(x2))
        table_params["x"].append((x2 + x1) / 2)
        table_params["func(x)"].append(fun((x2 + x1) / 2))
        table_params["epsilon"].append((b - a) / 2)
    table_params["func(left) > func(right)"].append("-")

    x_min = (a + b) / 2
    create_table(table_params, table_name)
    return x_min
