def solution(*args):
    name = args[0]
    c = args[1]
    w = args[2]
    m = args[3]
    print('================Чек================')
    print('Товар:' + ' ' * (35 - 6 - len(name)) + name)
    print('Цена:' + ' ' * (35 - 5 - 6 - 2 - len(str(c)) - len(str(w)) - 3) + str(w) + 'кг' + ' * ' + str(c) + 'руб/кг')
    print('Итого:' + ' ' * (35 - 6 - 3 - len(str(w * c))) + str(w * c) + 'руб')
    print('Внесено:' + ' ' * (35 - 8 - 3 - len(str(m))) + str(m) + 'руб')
    print('Сдача:' + ' ' * (35 - 6 - 3 - len(str(m - w * c))) + str(m - w * c) + 'руб')
    print('===================================')


def main():
    name = input()
    c = int(input())
    w = int(input())
    m = int(input())
    solution(name, c, w, m)


if __name__ == '__main__':
    main()
