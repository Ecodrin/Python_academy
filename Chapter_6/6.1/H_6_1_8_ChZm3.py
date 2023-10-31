import numpy as np


def snake(m, n, direction="H"):
    fl = False
    if direction == "V":
        fl = True
        n, m = m, n
    mas = []
    k = 1
    for i in range(n):
        mm = []
        for j in range(m):
            mm.append(k)
            k += 1
        if i % 2 == 0:
            mas.append(mm)
        else:
            mas.append(mm[::-1])
    a = np.array(mas, dtype='int16')
    if fl:
        a = a.transpose()
    return a


print(snake(5, 3))

