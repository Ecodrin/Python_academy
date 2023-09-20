def solution(n: int, m: int):
    for i in range(1, n + 1):
        for j in range(1, n):
            print(f'{i * j: ^{m}}', end='|')
        print(f'{i * n: ^{m}}')
        if i != n:
            print(f'{"":-^{m * n + (n - 1)}}')


def main():
    n = int(input())
    m = int(input())
    solution(n, m)


if __name__ == '__main__':
    main()
