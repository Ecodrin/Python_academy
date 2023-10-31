import numpy as np


def make_board(n):
    man_x = [[1 if (i % 2 and j % 2 or i % 2 == 0 and j % 2 == 0)
              else 0 for j in range(1, n + 1)] for i in range(1, n + 1)]
    board = np.array(man_x, dtype='int8')
    return board


print(make_board(4))
