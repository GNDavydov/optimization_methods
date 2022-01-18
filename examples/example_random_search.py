# Copyright 2021 GNDavydov

import numpy as np
import matplotlib.pyplot as plt

from extremum_search.one_criteria.random_search import random_search

# Начальные параметры
params = {
    'a': -2,
    'b': 4,
    'p': 0.95,
    'q': 0.005
}


# унимодальная функция
def fun1(x):
    return -np.cos(0.5 * x) - 1


# мультимодальная функция
def fun2(x):
    return fun1(x) * np.sin(5 * x)


print(random_search(params['a'], params['b'], fun1, params['p'], params['q']))
print(random_search(params['a'], params['b'], fun2, params['p'], params['q']))

X = np.arange(params['a'], params['b'], 0.01)

# Строим 1-ый график f(x)
y = fun1(X)
plt.plot(X, y)
plt.show()

# Строим 2-ой график f(x)*sin(5x)
y = fun2(X)
plt.plot(X, y)
plt.show()
