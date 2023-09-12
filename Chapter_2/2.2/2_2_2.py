def solution(s1: int, s2: int):
    match (s1 < s2):
        case True:
            print('Вася')
        case False:
            print('Петя')


def main():
    sr_p = int(input())
    sr_w = int(input())
    solution(sr_p, sr_w)


if __name__ == '__main__':
    main()
