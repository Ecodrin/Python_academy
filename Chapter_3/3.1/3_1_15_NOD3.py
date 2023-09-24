def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def solution(*args):
    s = args[0]
    n = s[0]
    for i in range(1, len(s)):
        n = get_nod(n, s[i])
    print(n)


def main():
    s = list(map(int, input().split()))
    solution(s)


if __name__ == '__main__':
    main()
