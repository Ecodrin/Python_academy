def solution(n, m):
    x = n * m
    max_l = len(str(x))
    [print(f'{i: >{max_l}}', end=' ') if i % m != 0
        else print(f'{i: >{max_l}}')for i in range(1, n * m + 1)]


def main():
    n = int(input())
    m = int(input())
    solution(n, m)


if __name__ == '__main__':
    main()
