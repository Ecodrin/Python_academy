def solution(n: int, m: int):
    ml = len(str(n * m))
    k = 0
    r = 0
    for i in range(n):
        k += 1
        r = k
        for j in range(m):
            print(f'{r: >{ml}}', end=' ')
            r += n
        print()


def main():
    n = int(input())
    m = int(input())
    solution(n, m)


if __name__ == '__main__':
    main()
