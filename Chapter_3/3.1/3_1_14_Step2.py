def solution(*args):
    s = args[0]
    p = args[1]
    for i in range(len(s)):
        print(s[i] ** p, end=' ')


def main():
    s = list(map(int, input().split()))
    p = int(input())
    solution(s, p)


if __name__ == '__main__':
    main()
