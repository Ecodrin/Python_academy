def summ(x, c):
    su = 0
    while x > 0:
        d = x % c
        su += d
        x //= c
    return su


def solution(x: int):
    maxs = 0
    cc = 0
    for i in range(2, 11):
        if summ(x, i) > maxs:
            maxs = summ(x, i)
            cc = i
    print(cc)


def main():
    x = int(input())
    solution(x)


if __name__ == '__main__':
    main()
