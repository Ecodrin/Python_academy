def solution(*args):
    ll = args[0]
    n = args[1]
    s = args[2]
    for i in range(n):
        if len(s[i]) > ll:
            print(s[i][:(ll - 3)] + '...')
        else:
            print(s[i])


def main():
    ll = int(input())
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    solution(ll, n, s)


if __name__ == '__main__':
    main()
