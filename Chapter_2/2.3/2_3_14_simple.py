from math import sqrt


def solution(x: int):
    fl = True
    for i in range(2, round(sqrt(x)) + 1):
        if x % i == 0:
            fl = False
            print('NO')
            break
    if x == 1:
        print('NO')
    elif fl:
        print('YES')


def main():
    n = int(input())
    solution(n)


if __name__ == '__main__':
    main()
