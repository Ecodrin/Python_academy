import numpy as np


def rotate(matrix, angle):
    for _ in range(angle % 360 // 90):
        matrix = np.rot90(matrix, -1)
    return matrix


print(rotate(np.arange(12).reshape(3, 4), 90))
