def solution(p: str):
    s1, s2, s3 = int(p[0]), int(p[1]), int(p[2])
    a = max(s1, s2, s3)
    b = min(s1, s2, s3)
    c = s1 + s2 + s3 - a - b
    if a + b == c * 2:
        print('YES')
    else:
        print('NO')


def main():
    pw = input()
    solution(pw)


if __name__ == '__main__':
    main()
