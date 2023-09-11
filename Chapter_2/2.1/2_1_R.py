def solution(*args):
    a = args[0]
    b = args[1]
    print(b - int(a, 2))


def main():
    a = input()
    b = int(input())
    solution(a, b)


if __name__ == '__main__':
    main()
