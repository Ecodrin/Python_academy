def solution(a: int, b: int):
    print([i * i for i in range(a, b + 1)])


def main():
    a = int(input())
    b = int(input())
    solution(a, b)


if __name__ == '__main__':
    main()

