def solution(s: str):
    maxc = max([int(s[i]) for i in range(len(s))])
    print(maxc)


def main():
    s = input()
    solution(s)


if __name__ == '__main__':
    main()
