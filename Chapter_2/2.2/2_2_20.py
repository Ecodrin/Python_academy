def solution(s1: str, s2: str, s3: str):
    ss = 'яяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяя'
    if 'зайка' in s1 and ss > s1:
        ss = s1
    if 'зайка' in s2 and ss > s2:
        ss = s2
    if 'зайка' in s3 and ss > s3:
        ss = s3
    print(ss, len(ss), sep=' ')


def main():
    s1 = input()
    s2 = input()
    s3 = input()
    solution(s1, s2, s3)


if __name__ == '__main__':
    main()
