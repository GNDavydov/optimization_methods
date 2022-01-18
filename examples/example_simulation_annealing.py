# Copyright 2021 GNDavydov

import numpy as np
import matplotlib.pyplot as plt

from extremum_search.one_criteria.simulation_annealing import simulated_annealing

# Начальные параметры
params = {
    'a': 2,
    'b': 6,
    't_max': 10000,
    't_min': 0.1,
    'k': 0.95
}


# унимодальная функция
def fun1(x):
    return 5 * np.cos(x) + x + x ** 0.5


# мультимодальная функция
def fun2(x):
    return np.sin(5 * x) * fun1(x)


print(simulated_annealing(params['a'], params['b'], fun1, params['t_min'], params['t_max'], params['k']))
print(simulated_annealing(params['a'], params['b'], fun2, params['t_min'], params['t_max'], params['k']))

# Строим 1-ый график f(x)
X = np.arange(params['a'], params['b'], 0.01)
y = fun1(X)
plt.plot(X, y)
plt.show()

# Строим 2-ой график f(x)*sin(5x)
y = fun2(X)
plt.plot(X, y)
plt.show()
