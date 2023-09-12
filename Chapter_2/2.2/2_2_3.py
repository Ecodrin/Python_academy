def solution(s1: int, s2: int, s3: int):
    if s1 > s2 and s1 > s3:
        print('Петя')
    elif s2 > s1 and s2 > s3:
        print('Вася')
    else:
        print('Толя')


def main():
    sr_p = int(input())
    sr_w = int(input())
    sr_t = int(input())
    solution(sr_p, sr_w, sr_t)


if __name__ == '__main__':
    main()
