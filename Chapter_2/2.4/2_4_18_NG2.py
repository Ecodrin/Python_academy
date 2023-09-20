def maxl(n):
    y = 1
    k = 0
    s = ''
    ll = -1
    for i in range(1, n + 1):
        k += 1
        if k == y or i == n:
            s += str(i)
            k = 0
            y += 1
            ll = max(ll, len(s))
            s = ''
        else:
            s += str(i) + ' '
    return ll


def solution(x: int):
    y = 1
    k = 0
    s = ''
    for i in range(1, x + 1):
        k += 1
        if k == y or i == x:
            s += str(i)
            y += 1
            print(f'{s: ^{maxl(x)}}')
            k = 0
            s = ''
        else:
            s += str(i) + ' '


def main():
    x = int(input())
    solution(x)


if __name__ == '__main__':
    main()
