def solution(*args):
    s = args[0]
    st = args[1]
    for i in range(len(s)):
        print(s[i] ** st)


def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(int(input()))
    st = int(input())
    solution(s, st)


if __name__ == '__main__':
    main()
