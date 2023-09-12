import calendar


def solution(n: int):
    if calendar.isleap(n):
        print('YES')
    else:
        print('NO')


def main():
    n = int(input())
    solution(n)


if __name__ == '__main__':
    main()
