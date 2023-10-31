from math import comb


def solution(n, m):
    print(comb(n, m) * m // n, comb(n, m))


def main():
    n, m = map(int, input().split())
    solution(n, m)


if __name__ == '__main__':
    main()
