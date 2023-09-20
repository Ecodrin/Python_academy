from math import ceil


def solution(x: int):
    for i in range(1, x + 1):
        for j in range(1, x + 1):
            if j != 1 or x >= 19:
                r = min(i, j, x - j + 1, x - i + 1)
                print(f'{r: >{len(str(ceil(x / 2)))}}', end=' ')
            else:
                print(min(i, j, x - j + 1, x - i + 1), end=' ')
        print()


def main():
    x = int(input())
    solution(x)


if __name__ == '__main__':
    main()
