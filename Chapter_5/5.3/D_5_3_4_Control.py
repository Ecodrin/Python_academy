class Numbers(Exception):
    pass


class Ch(Numbers):
    pass


class ChPol(Numbers):
    pass


def ch(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return True
    raise Ch("TypeError")


def chpol(a, b):
    if isinstance(a, int) and isinstance(b, int) and a > 0 and b > 0 and a % 2 == 0 and b % 2 == 0:
        return True
    raise ChPol("ValueError")


def only_positive_even_sum(a, b):
    try:
        if ch(a, b) and chpol(a, b):
            return a + b
    except Numbers as e:
        return f"Вызвано исключение {e}"


print(only_positive_even_sum(1.2, 2))