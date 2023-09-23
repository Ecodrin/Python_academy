def solution(*args):
    s = args[0][:-1]
    p = args[0][-1]
    for i in range(len(s)):
        if p.lower() in s[i].lower():
            print(s[i])


def main():
    n = int(input())
    s = []
    for i in range(n + 1):
        s.append(input())
    solution(s)


if __name__ == '__main__':
    main()
