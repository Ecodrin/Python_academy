import itertools


def solution(s: list[str]):
    for i, j in itertools.combinations(s, 2):
        print(i, j, sep=' - ')


def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    solution(s)


if __name__ == '__main__':
    main()
