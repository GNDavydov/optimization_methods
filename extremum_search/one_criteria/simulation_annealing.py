# Copyright 2021 GNDavydov

import numpy as np

'''
Метод поиска экстремума унимодальной и мультимодальной функций от одного переменного, 
используя алгоритм имитации отжига

Включает:
 1) алгоритм поиска экстремума методом имитации отжига
'''


def simulated_annealing(a, b, fun, t_min, t_max, k):
    '''
    Функция, выполняющая поиск минимума методом имитации отжига функции fun на отрезке [a, b]

    :param a: Начальная граница отрезка
    :param b: Конечная граница отрезка
    :param fun: Исходная функция
    :param t_min: Заданная минимальная температура
    :param t_max: Заданная максимальная температура
    :param k: коэффициент убывания температуры
    :return: минимум функции f(x)
    '''

    x_min = np.random.uniform(a, b)
    fun_min = fun(x_min)
    t_i = t_max

    while t_i > t_min:
        x_i = np.random.uniform(a, b)
        fun_i = fun(x_i)
        delta = fun_i - fun_min

        if delta <= 0:
            x_min = x_i
            fun_min = fun_i
        else:
            p = np.exp(-delta / t_i)
            if p * 100 >= np.random.uniform(0, 100):
                x_min = x_i
                fun_min = fun_i

        t_i *= k

    return x_min
