def solution(s: str):
    if s == s[::-1]:
        print('Yes')
    else:
        print('NO')


def main():
    s = input()
    solution(s)


if __name__ == '__main__':
    main()
