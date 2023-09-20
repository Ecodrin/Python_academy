from math import sqrt


def prost(x):
    for i in range(2, round(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(*args):
    m = args[0]
    print(sum([1 for i in range(len(m)) if (prost(m[i]) and m[i] != 2)]))


def main():
    s = []
    n = int(input())
    for i in range(n):
        s.append(int(input()))
    solution(s)


if __name__ == '__main__':
    main()
