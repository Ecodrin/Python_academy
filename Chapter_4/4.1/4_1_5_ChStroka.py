def split_numbers(s: str):
    return tuple(list(map(int, s.split())))


print(split_numbers('1 2 3 4 5'))