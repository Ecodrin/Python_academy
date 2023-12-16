ss = []


def rabbit(start, finish, lenght):
    rabbit_1(start, finish, lenght)
    return ss


def rabbit_1(start, finish, lenght, s=''):
    if start == finish and lenght == 0:
        global ss
        otv = list(map(int, (s + str(finish)).split(' | ')))
        if len(otv) == len(set(otv)):
            ss.append(otv)
        s = []
        return 1
    if lenght < 0:
        s = []
        return 0
    s += f'{start} | '
    return (rabbit_1(start + 1, finish, lenght - 1, s) + rabbit_1(start + 2, finish, lenght - 1, s)
            + rabbit_1(start - 1, finish, lenght - 1, s) + rabbit_1(start - 2, finish, lenght - 1, s))


result = rabbit(13, 17, 4)
print(*result, sep="\n")



'''all_hops = []


def bunny(*args):
    real_bunny(*args)
    return all_hops


def real_bunny(start, finish, length, hops=''):
    if start == finish and length == 0:
        global all_hops
        all_hops.append(list(map(int, (hops + str(finish)).split(' | '))))
        return 1
    if length <= 0 or start == finish:
        return 0
    hops += f'{start} | '
    return (bunny(start + 1, finish, length - 1, hops) + bunny(start + 3, finish, length - 1, hops) +
            bunny(start - 1, finish, length - 1, hops) + bunny(start - 3, finish, length - 1, hops))'''


'''
from itertools import product


def grasshopper(start, finish, length):
    paths, all_paths = list(), range(start - 2, finish + 3)
    for way in product(all_paths, repeat=(length + 1)):
        if way.count(finish) == 1 and way[length] == finish and way[0] == start:
            for j in range(length):
                if not abs(way[j + 1] - way[j]) == 1 and not abs(way[j + 1] - way[j]) == 2:
                    break
            else:
                paths.append(list(way))
    return paths
'''