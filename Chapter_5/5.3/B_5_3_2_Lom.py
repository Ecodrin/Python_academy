def func(a, b):
    return a + b


def main():
    try:
        func(0, None)
    except ValueError:
        print('Ура! Ошибка!')


if __name__ == '__main__':
    main()
