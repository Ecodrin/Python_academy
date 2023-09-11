def solution(*args):
    print('Привет, ' + args[0])


def main():
    arguments = input('Как Вас зовут?\n')
    solution(arguments)


if __name__ == '__main__':
    main()
