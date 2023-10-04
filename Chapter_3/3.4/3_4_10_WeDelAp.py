import itertools


def solution(m: int):
    print('А Б В')
    b = itertools.product([i for i in range(1, m + 1)], repeat=3)
    a = [print(*[x, y, z]) for x, y, z in b if x + y + z == m]


def main():
    x = int(input())
    solution(x)


if __name__ == '__main__':
    main()
