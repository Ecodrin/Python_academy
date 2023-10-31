import numpy as np


def stairs(vector):
    matrix = np.array([list(vector)[-i:] + list(vector)[:-i] for i in range(len(vector))], dtype='int16')
    return matrix


print(stairs(np.arange(5)))
