def merge(a, b):
    try:
        _ = iter(a)
        _ = iter(b)
    except TypeError:
        raise StopIteration
    if not (all(isinstance(a[i], type(a[0])) for i in range(len(a))) and
            all(isinstance(b[i], type(a[0])) for i in range(len(b)))):
        raise TypeError
    if sorted(a) != list(a) or sorted(b) != list(b):
        raise ValueError
    return tuple(sorted(list(a) + list(b)))


print(*merge([], [1, 2, 3]))
