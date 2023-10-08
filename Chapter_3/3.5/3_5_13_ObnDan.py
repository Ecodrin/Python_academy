import json
from sys import stdin


def solution(informations, name):
    with open(name, 'w', encoding='UTF-8') as file:
        json.dump(informations, file, ensure_ascii=False, indent=4)


def main():
    name = input()
    with open(name, 'r', encoding='UTF-8') as file:
        informations = json.load(file)
    for line in stdin:
        i_key, i_inf = line.split(' == ')
        informations[i_key] = i_inf.rstrip('\n')
    solution(informations, name)


if __name__ == '__main__':
    main()
