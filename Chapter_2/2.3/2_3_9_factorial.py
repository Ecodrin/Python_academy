def solution(x: int):
    s = 1
    for i in range(1, x + 1):
        s *= i
    print(s)


def main():
    n = int(input())
    solution(n)


if __name__ == '__main__':
    main()
