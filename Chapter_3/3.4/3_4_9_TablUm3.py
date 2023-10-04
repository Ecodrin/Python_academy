import itertools


def solution(x):
    g = [i for i in range(1, x + 1)]
    r = itertools.product(g, g)
    itog = [i * j for i, j in r]
    for i in range(0, len(itog)):
        print(itog[i], end=' ')
        if (i + 1) % x == 0:
            print()


def main():
    x = int(input())
    solution(x)


if __name__ == '__main__':
    main()
