def solution(p: int):
    s1 = str(int(str(p)[-1]) + int(str(p)[-2]))
    s2 = str(int(str(p)[0]) + int(str(p)[1]))
    if int(s1) <= int(s2):
        print(s2 + s1)
    else:
        print(s1 + s2)


def main():
    pw = int(input())
    solution(pw)


if __name__ == '__main__':
    main()
