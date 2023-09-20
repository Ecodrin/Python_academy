def solution(n: int):
    for i in range(1, n + 1):
        s = [i * j for j in range(1, n + 1)]
        print(*s)


def main():
    x = int(input())
    solution(x)


if __name__ == '__main__':
    main()
