def solution(n: int):
    k = 3
    for i in range(n):
        for j in range(k):
            print(f'До старта {k - j} секунд(ы)')
        print(f'Старт {i + 1}!!!')
        k += 1


def main():
    n = int(input())
    solution(n)


if __name__ == '__main__':
    main()
