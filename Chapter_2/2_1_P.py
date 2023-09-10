def solution(*args):
    a = args[0]
    b = args[1]
    c = args[2]
    print(f"{((b - a) / c):.2f}")


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    solution(a, b, c)


if __name__ == '__main__':
    main()
