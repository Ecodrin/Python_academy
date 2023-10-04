def solution(s: list[str]):
    for i, j in zip([i for i in range(1, len(s) + 1)], s):
        print(i, j, sep='. ')


def main():
    n = int(input())
    s = []
    for i in range(n):
        s += input().split(', ')
    solution(sorted(s))


if __name__ == '__main__':
    main()
