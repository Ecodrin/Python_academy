def solution(*args):
    a = args[0]
    b = args[1]
    print(a + int(b, 2))


def main():
    a = int(input())
    b = input()
    solution(a, b)


if __name__ == '__main__':
    main()
