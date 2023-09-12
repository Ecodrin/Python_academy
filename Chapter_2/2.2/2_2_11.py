def solution(p: str):
    s1 = int(p[0])
    s2 = int(p[1])
    s3 = int(p[2])
    if max(s1, s2, s3) + min(s1, s2, s3) == (s1 + s2 + s3 - max(s1, s2, s3) - min(s1, s2, s3)) * 2:
        print('YES')
    else:
        print('NO')


def main():
    pw = input()
    solution(pw)


if __name__ == '__main__':
    main()
