import itertools


def solution(s: list[str]):
    x = itertools.permutations(sorted(s))
    for i in x:
        print(*list(i), sep=', ')


def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    solution(s)


if __name__ == '__main__':
    main()
