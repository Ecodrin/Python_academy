def solution(*args):
    print('Чек')
    print(args[0] + ' - ' + str(args[2]) + 'кг' + ' - ' + str(args[1]) + 'руб/кг')
    print('Итого: ' + str(args[1] * args[2]) + 'руб')
    print('Внесено: ' + str(args[3]) + 'руб')
    print('Сдача: ' + str(args[3] - args[1] * args[2]) + 'руб')


def main():
    name_product = input()
    c = int(input())
    w = int(input())
    m = int(input())
    solution(name_product, c, w, m)


if __name__ == '__main__':
    main()
