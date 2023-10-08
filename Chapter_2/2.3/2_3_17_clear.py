def solution(s: str):
    ss = ''
    for i in range(len(s)):
        if int(s[i]) % 2:
            ss += s[i]
    print(ss)


def main():
    s = input()
    solution(s)


if __name__ == '__main__':
    main()
