# Copyright 2021 GNDavydov

import numpy as np
import matplotlib.pyplot as plt

from extremum_search.two_criteria.genetic_algorithm import GeneticAlgorithm

# Начальные параметры
params = {
    'x_min': 0,
    'x_max': 2,
    'y_min': -2,
    'y_max': 2,
}


def fun(x, y):
    return np.sin(x) * np.sin(y) / (1 + x ** 2 + y ** 2)


a = GeneticAlgorithm()
print(a.genetic_algorithm(fun, params['x_min'], params['x_max'], params['y_min'], params['y_max'], 20))

X, Y = np.meshgrid(np.arange(params['x_min'], params['x_max'], 0.005),
                   np.arange(params['y_min'], params['y_max'], 0.01))
Z = fun(X, Y)

fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
ax.plot_surface(X, Y, Z, cmap=plt.get_cmap('jet'))
plt.show()
