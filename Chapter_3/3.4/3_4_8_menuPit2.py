import itertools


def solution(*args):
    m = args[0]
    s = args[1]
    n = args[2]
    for i in range(n):
        print(*[x for x in itertools.islice(s, i % m, i % m + 1)])


def main():
    m = int(input())
    s = []
    for i in range(m):
        s.append(input())
    n = int(input())
    solution(m, s, n)


if __name__ == '__main__':
    main()
