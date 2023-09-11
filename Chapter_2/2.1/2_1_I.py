def solution(*args):
    print(args[0] * args[1] // 2)


def main():
    n = int(input())
    m = int(input())
    solution(n, m)


if __name__ == '__main__':
    main()
