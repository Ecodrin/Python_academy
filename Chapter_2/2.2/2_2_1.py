def solution(ill: str):
    match ill:
        case 'хорошо':
            print('Я за вас рада!')
        case 'плохо':
            print('Всё наладится!')


def main():
    name = input('Как Вас зовут?\n')
    ill = input(f'Здравствуйте, {name}!\nКак дела?\n')
    solution(ill)


if __name__ == '__main__':
    main()
