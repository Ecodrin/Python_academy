from math import sqrt


def prost(n):
    for i in range(2, round(sqrt(n))):
        if n % i == 0:
            return False
    return True


def solution(x: int):
    m = []
    while x != 1:
        for i in range(2, x + 1):
            if prost(i) and x % i == 0:
                m.append(i)
                x //= i
                break
    print(*m, sep=' * ')


def main():
    s = int(input())
    solution(s)


if __name__ == '__main__':
    main()
