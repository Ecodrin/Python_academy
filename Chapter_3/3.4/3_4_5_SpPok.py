def solution(s: list[str]):
    s = list(zip([i for i in range(1, len(s) + 1)], s))
    for i, j in s:
        print(i, j, sep='. ')


def main():
    s1 = input().split(', ')
    s2 = input().split(', ')
    s3 = input().split(', ')
    s = sorted(s1 + s2 + s3)
    solution(s)


if __name__ == '__main__':
    main()
