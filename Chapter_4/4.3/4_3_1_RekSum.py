def recursive_sum(*args):
    if not args:
        return 0
    return args[-1] + recursive_sum(*args[:-1])


print(recursive_sum(1, 2, 3))
