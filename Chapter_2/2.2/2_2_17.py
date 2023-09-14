from math import sqrt


def solution(a: float, b: float, c: float):
    if a == 0:
        if b == 0 and c == 0:
            print('Infinite solutions')
        elif b == 0:
            print('No solution')
        elif c == 0:
            print(f'{0:.2f}')
        else:
            print(f'{-c / b:.2f}')
    else:
        d = b ** 2 - 4 * a * c
        if d < 0:
            print('No solution')
        elif d == 0:
            print(f'{-b / (2 * a):.2f}')
        else:
            d = sqrt(d)
            x = (-b + d) / (2 * a)
            y = (-b - d) / (2 * a)
            print(f'{min(x, y):.2f}', f'{max(x, y):.2f}')


def main():
    a = float(input())
    b = float(input())
    c = float(input())
    solution(a, b, c)


if __name__ == '__main__':
    main()
