def solution(s: str):
    su = 0
    for i in range(len(s)):
        su += int(s[i])
    print(su)


def main():
    s = input()
    solution(s)


if __name__ == '__main__':
    main()
