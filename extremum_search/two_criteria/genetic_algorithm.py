# Copyright 2021 GNDavydov

import numpy as np
from sortedcontainers import SortedDict

'''
Поиск экстремума функции от двух переменных, используя генетический алгоритм
'''


class GeneticAlgorithm:
    def __init__(self):
        self._fun = None
        self._x_min = None
        self._x_max = None
        self._y_min = None
        self._y_max = None
        self._generation = None

    def _generate_point(self):
        '''
            Функция генерации точки на заданных областях для x и y
            :return: точка с координатами (x, y)
        '''
        x = np.random.uniform(self._x_min, self._x_max)
        y = np.random.uniform(self._y_min, self._y_max)
        return x, y

    def _crossover(self):
        '''
           Скрещевание лучших родителей generation
           В качестве потомков выбрать результат
           скрещивания лучшего решения со вторым и третьим
           в порядке убывания значений функции приспособленности
           с последующей случайной мутацией обоих генов
           :return:
        '''

        def reproduction(point_1, point_2):
            '''
            Функция, скрещивающая две особи
            :param point_1: первая особь(точка)
            :param point_2: вторая особь(точка)
            :return: две новые особи: (x1, y2), (x2, y1)
            '''

            return (point_1[0], point_2[1]), (point_2[0], point_1[1])

        points = list(self._generation.values())
        new_points = reproduction(points[-1], points[-2]) + reproduction(points[-1], points[-3])
        for point in new_points:
            self._generation.update({self._fun(point[0], point[1]): point})

    def _selection(self):
        '''
            Функция отбора (элитарный отбор)
            Выборка 4 лучших особей из мутировавшего поколения родителей + потомков
        '''
        new_generation = SortedDict()
        items = list(self._generation.items())[-4:]
        for item in items:
            new_generation.update({item[0]: item[1]})
        self._generation = new_generation

    def _mutation(self):
        '''
            Функция которая вызывает мутирование у поколения generation
            Каждая точка подвержена мутации с вероятностью 25%
            :return:
        '''

        def probability_mutation():
            '''
            Функция возвращает вероятность мутации
            :return: вероятность мутации
            '''
            return np.random.uniform(0, 1)

        def mutation_individual(x, y):
            '''
            Функция вызывает мутирование точки. Случайно выбирает бит в числе, который изменяется
            в данном случае выбирается от 1 до 17
            :param x: координата по x
            :param y: координата по y
            :return: возвращает новые координаты точки
            '''

            mask = 2 ** np.random.randint(10, 17)
            new_x = (int(x * 100000) ^ mask) / 100000
            new_y = (int(y * 100000) ^ mask) / 100000

            new_x %= 2
            if new_y > 0:
                new_y %= 2
            else:
                new_y %= -2

            return new_x, new_y

        for individual in self._generation:
            if probability_mutation() > 0.75:
                point = self._generation[individual]
                point = mutation_individual(point[0], point[1])
                self._generation.pop(individual)
                self._generation.update({self._fun(point[0], point[1]): point})

    @staticmethod
    def _average_fit(generation):
        '''
        Подсчет среднего значения фитнес-функции
        '''
        fits = list(generation)
        return sum(fits) / len(fits)

    def genetic_algorithm(self, fun, x_min, x_max, y_min, y_max, n):
        '''
        Функция, выполняющая генетический алгоритм

        :param fun: функция приспособленности
        :param x_min: минимальное значение для области определения для аргумента x
        :param x_max: максимальное значение для области определения для аргумента x
        :param y_min: минимальное значение для области определения для аргумента y
        :param y_max: максимальное значение для области определения для аргумента y
        :param n: количество итераций
        :return:
        '''

        self._fun = fun
        self._x_min = x_min
        self._x_max = x_max
        self._y_min = y_min
        self._y_max = y_max
        self._generation = SortedDict()

        for i in range(4):
            point = self._generate_point()
            self._generation.update({fun(point[0], point[1]): point})

        for i in range(n):
            self._crossover()
            self._mutation()
            self._selection()
            print(f'{i + 1}: {list(self._generation)}, fit_avg = {self._average_fit(self._generation)}')

        return list(self._generation.keys())[-1]
