def solution(*args):
    print('Группа №' + args[1][0] + '.')
    print(args[1][2] + '. ' + args[0] + '.')
    print('Шкафчик: ' + args[1] + '.')
    print('Кроватка: ' + args[1][1] + '.')


def main():
    name = input()
    x = input()
    solution(name, x)


if __name__ == '__main__':
    main()
