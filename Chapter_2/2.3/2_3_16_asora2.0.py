def solution(s: str):
    fl = True
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            fl = False
    match fl:
        case True:
            print('YES')
        case False:
            print('NO')


def main():
    s = input()
    solution(s)


if __name__ == '__main__':
    main()
