def solution(x: float, y: float):
    if x ** 2 + y ** 2 > 100:
        print('Вы вышли в море и рискуете быть съеденным акулой!')
    else:
        q1 = (x >= 0 and y >= 0 and x ** 2 + y ** 2 <= 25)
        q2 = (-7 <= x <= 5 and y <= 0 and (y >= 0.25 * x ** 2 + 0.5 * x - 35 / 4))
        q3 = (y <= 5 / 3 * x + 35 / 3 and -7 <= x <= -4)
        q4 = ((-4 <= x <= 0) and (0 <= y <= 5))
        if q1 or q2 or q3 or q4:
            print('Опасность! Покиньте зону как можно скорее!')
        else:
            print('Зона безопасна. Продолжайте работу.')


def main():
    a = float(input())
    b = float(input())
    solution(a, b)


if __name__ == '__main__':
    main()
