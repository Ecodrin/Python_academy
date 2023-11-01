import pandas as pd
import numpy as np


def values(func, start, end, step):
    mas = np.arange(start, end + step, step)
    a = pd.Series([func(x) for x in mas], index=[x for x in mas])
    return a


def max_extremum(dataf: pd.Series):
    maxs = 0
    ind = -1
    for i, s in dataf.items():
        if s > maxs:
            maxs = s
            ind = i
    return ind


def min_extremum(dataf: pd.Series):
    mins = 10e10
    ind = -1
    for i, s in dataf.items():
        if s < mins:
            mins = s
            ind = i
    return ind


data = values(lambda x: x ** 2 + 2 * x + 1, -1.5, 1.7, 0.1)
print(data)
print(min_extremum(data))
print(max_extremum(data))
