def solution(s: str):
    ss = ''
    for i in range(len(s)):
        if s[i] in '13579':
            ss += s[i]
    print(ss)


def main():
    s = input()
    solution(s)


if __name__ == '__main__':
    main()
