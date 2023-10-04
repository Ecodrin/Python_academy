import itertools


def solution(s: list[str]):
    s.sort()
    x = itertools.permutations(s, 3)
    for i in x:
        print(*list(i))


def main():
    n = int(input())
    s = []
    for i in range(n):
        s += input().split(', ')
    solution(s)


if __name__ == '__main__':
    main()
