def solution(*args):
    print(args[1] // args[0])
    print(args[1] % args[0])


def main():
    k = int(input())
    s = int(input())
    solution(k, s)


if __name__ == '__main__':
    main()
