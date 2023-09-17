def solution(start: int, end: int):
    for i in range(start, end + 1):
        print(i, end=' ')


def main():
    a = int(input())
    b = int(input())
    solution(a, b)


if __name__ == '__main__':
    main()
