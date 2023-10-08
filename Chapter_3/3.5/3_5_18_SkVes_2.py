from math import ceil
import os


def solution(name_file: str):
    weight = {'Б': 1, 'КБ': 2 ** 10, 'МБ': 2 ** 20, 'ГБ': 2 ** 30, 'ТБ': 2 ** 40}
    su = os.path.getsize(name_file)
    for translation, size in reversed(weight.items()):
        if su / size >= 1:
            print(ceil(su / size), translation, sep='')
            break


def main():
    name_file = input()
    solution(name_file)


if __name__ == '__main__':
    main()
