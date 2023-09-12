def solution(*args):
    name = args[0]
    c = args[1]
    w = args[2]
    m = args[3]
    print(f'{"Чек":=^35}')
    print(f'Товар:{name: >29}')
    print(f'Цена:{(str(w) + "кг * " + str(c)): >24}руб/кг')
    print(f'Итого:{w * c: >26}руб')
    print(f'Внесено:{m: >24}руб')
    print(f'Сдача:{m - w * c: > 26}руб')
    print(f'{"":=^35}')


def main():
    name = input()
    c = int(input())
    w = int(input())
    m = int(input())
    solution(name, c, w, m)


if __name__ == '__main__':
    main()
