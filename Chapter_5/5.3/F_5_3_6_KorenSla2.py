from math import sqrt


class Errors(Exception):
    pass


class NoSolutionsError(Errors):
    pass


class InfiniteSolutionsError(Errors):
    pass


def find_roots(a: float, b: float, c: float):
    if not (isinstance(a, float | int) and isinstance(a, float | int) and isinstance(a, float | int)):
        raise TypeError
    if a == 0:
        if b == 0 and c == 0:
            raise InfiniteSolutionsError
        elif b == 0:
            raise NoSolutionsError
        elif c == 0:
            return 0, 0
        else:
            return -c / b, -c / b
    else:
        d = b ** 2 - 4 * a * c
        if d < 0:
            raise NoSolutionsError
        elif d == 0:
            return -b / (2 * a), -b / (2 * a)
        else:
            d = sqrt(d)
            x = (-b + d) / (2 * a)
            y = (-b - d) / (2 * a)
            return min(x, y), max(x, y)


print(find_roots(1, 2, 1))
