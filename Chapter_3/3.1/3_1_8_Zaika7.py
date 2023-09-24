def solution(*args):
    s = args[0]
    for i in range(len(s)):
        if s[i].find('зайка') + 1 > 0:
            print(s[i].find('зайка') + 1)
        else:
            print('Заек нет =(')


def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    solution(s)


if __name__ == '__main__':
    main()
