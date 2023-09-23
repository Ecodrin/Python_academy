def solution(s: str):
    k = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            k += 1
        else:
            k += 1
            print(s[i], k)
            k = 0
    k += 1
    print(s[-1], k)


def main():
    s = input()
    solution(s)


if __name__ == '__main__':
    main()
