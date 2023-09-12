def solution(a: int, b: int, c: int):
    if max(a, b, c) < a + b + c - max(a, b, c):
        print('YES')
    else:
        print('NO')


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    solution(a, b, c)


if __name__ == '__main__':
    main()
