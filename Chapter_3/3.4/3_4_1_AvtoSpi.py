def solution(s: list[str]):
    s = list(zip([i for i in range(1, len(s) + 1)], s))
    for i, j in s:
        print(i, j, sep='. ')


def main():
    s = input().split()
    solution(s)


if __name__ == '__main__':
    main()
