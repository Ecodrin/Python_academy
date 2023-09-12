def solution(a: str, b: str):
    m = list(a) + list(b)
    m = [int(m[i]) for i in range(len(m))]
    c = str(max(m)) + str((sum(m) - max(m) - min(m)) % 10) + str(min(m))
    print(c)


def main():
    a = input()
    b = input()
    solution(a, b)


if __name__ == '__main__':
    main()
