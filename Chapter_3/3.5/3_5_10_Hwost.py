def solution(name, c):
    with open(name, 'r', encoding='UTF-8') as file:
        itog = file.readlines()
    [print(i.rstrip('\n')) for i in itog[-c:]]


def main():
    name = input()
    c = int(input())
    solution(name, c)


if __name__ == '__main__':
    main()
