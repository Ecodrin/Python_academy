def solution(n: int, m: int):
    k = 1
    ml = len(str(m * n))
    for i in range(n):
        for j in range(m):
            print(f'{k: >{ml}}', end=' ')
            k += 1
        print()


def main():
    n = int(input())
    m = int(input())
    solution(n, m)


if __name__ == '__main__':
    main()
