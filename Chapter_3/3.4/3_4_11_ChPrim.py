import itertools


def solution(n, m):
    x = n * m
    max_l = len(str(x))
    for x, y in itertools.product([i for i in range(n)], [i for i in range(1, m + 1)]):
        print(f'{x * m + y: >{max_l}}', end=' ')
        if y == m:
            print()


def main():
    n = int(input())
    m = int(input())
    solution(n, m)


if __name__ == '__main__':
    main()
