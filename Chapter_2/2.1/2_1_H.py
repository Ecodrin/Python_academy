def solution(*args):
    for i in range(args[0]):
        print(f'Я больше никогда не буду писать "{args[1]}"!')


def main():
    n = int(input())
    s = input()
    solution(n, s)


if __name__ == '__main__':
    main()
