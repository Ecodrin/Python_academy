def solution(n: int, m: int):
    match (7 - 3 + 2 + n > 6 + 3 + m):
        case True:
            print('Петя')
        case False:
            print('Вася')


def main():
    n = int(input())
    m = int(input())
    solution(n, m)


if __name__ == '__main__':
    main()
