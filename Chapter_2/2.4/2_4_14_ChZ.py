def solution(n: int, m: int):
    ml = len(str(m * n))
    k = 0
    for i in range(n):
        s = ''
        for j in range(m):
            k += 1
            if i % 2 == 0:
                s += f'{k: >{ml}} '
            else:
                s = f'{k: >{ml}} ' + s
        print(s)


def main():
    n = int(input())
    m = int(input())
    solution(n, m)


if __name__ == '__main__':
    main()
