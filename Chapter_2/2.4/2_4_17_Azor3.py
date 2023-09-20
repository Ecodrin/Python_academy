def pal(s: str):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


def solution(*args):
    s = args[0]
    print(sum([1 for i in range(len(s)) if pal(s[i])]))


def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    solution(s)


if __name__ == '__main__':
    main()
