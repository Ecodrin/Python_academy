def can_eat(a, b):
    x1, y1 = a
    x2, y2 = b
    if ((abs(x2 - x1) == 1 and abs(y2 - y1) == 2) or
            (abs(x2 - x1) == 2 and abs(y2 - y1) == 1)):
        return True
    return False


print(can_eat((2, 1), (4, 2)))
