import itertools


def solution(s: str):
    sl = set()
    for i in s:
        if i.isupper():
            sl.add(i)
    sl = sorted(sl)
    [print(i, end=' ') for i in sl]
    print('F')
    x = itertools.product([0, 1], repeat=len(sl))
    for i in x:
        xx = dict(zip(sl, i))
        print(*i, int(eval(s, xx)))


def main():
    s = input()
    solution(s)


if __name__ == '__main__':
    main()
