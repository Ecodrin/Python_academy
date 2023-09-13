def solution(s1: str, s2: str, s3: str):
    ss = ''
    minl = 10 ** 10
    if 'зайка' in s1 and minl >= len(s1):
        ss = s1
        minl = len(s1)
    if 'зайка' in s2 and minl >= len(s2):
        ss = s2
        minl = len(s2)
    if 'зайка' in s3 and minl >= len(s3):
        ss = s3
        minl = len(s3)
    print(ss, minl, sep=' ')


def main():
    s1 = input()
    s2 = input()
    s3 = input()
    solution(s1, s2, s3)


if __name__ == '__main__':
    main()
