from math import sqrt


def solution(a: float, b: float, c: float):
    if a == 0 and b != 0 and c != 0:
        print(f'{(-c / b):.2f}')
    elif a == 0 and b == 0 and c == 0:
        print('Infinite solutions')
    elif sqrt(b ** 2 - 4 * a * c) < 0:
        print('No solution')
    elif sqrt(b ** 2 - 4 * a * c) == 0:
        print(f'{-b / (2 * a):.2f}')
    else:
        d = sqrt(b ** 2 - 4 * a * c)
        aa = float(f'{(-b - d) / (2 * a):.2f}')
        bb = float(f'{(-b + d) / (2 * a):.2f}')
        print(min(aa, bb), max(aa, bb))


def main():
    a = float(input())
    b = float(input())
    c = float(input())
    solution(a, b, c)


if __name__ == '__main__':
    main()
