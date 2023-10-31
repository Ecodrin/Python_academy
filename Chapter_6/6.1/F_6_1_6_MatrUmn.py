import numpy as np


def multiplication_matrix(n: int):
    return np.array([[i * j for j in range(1, n + 1)] for i in range(1, n + 1)])


print(multiplication_matrix(5))
