def solution(n: int):
    print([[j * i for j in range(1, n + 1)] for i in range(1, n + 1)])


def main():
    n = int(input())
    solution(n)


if __name__ == '__main__':
    main()
