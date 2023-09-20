def solution(n: int, m: int):
    k = 0
    ml = len(str(m * n))
    s = ['' for _ in range(n)]
    for i in range(1, n * m + 1):
        if k < n - 1:
            s[k] += f'{i: >{ml}} '
            k += 1
        elif n < k < 2 * n - 1:
            s[n - k % n - 1] += f'{i: >{ml}} '
            k += 1
        elif k == n - 1 or k == n:
            s[n - 1] += f'{i: >{ml}} '
            k += 1
        elif k == 2 * n - 1:
            s[0] += f'{i: >{ml}} '
            k = 0
    for i in range(n):
        print(s[i])


def main():
    n = int(input())
    m = int(input())
    solution(n, m)


if __name__ == '__main__':
    main()
