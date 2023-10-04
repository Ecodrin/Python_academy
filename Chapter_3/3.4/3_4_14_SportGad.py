import itertools


def solution(s: list[str]):
    a = itertools.permutations(sorted(s), r=3)
    for x in a:
        print(*list(x), sep=', ')


def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    solution(s)


if __name__ == '__main__':
    main()
