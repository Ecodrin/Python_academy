def cycle(args):
    count = -1
    while True:
        count += 1
        yield args[count % len(args)]


print(*(x for _, x in zip(range(15), cycle([1, 2, 3, 4]))))
