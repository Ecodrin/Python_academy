def solution(a: int, b: int, c: int):
    c1 = str(max(a, b, c)) + str(a + b + c - max(a, b, c) - min(a, b, c))
    if min(a, b, c) != 0:
        c2 = str(min(a, b, c)) + str(a + b + c - max(a, b, c) - min(a, b, c))
    else:
        c2 = str(a + b + c - max(a, b, c) - min(a, b, c)) + str(min(a, b, c))
    print(c2, c1, sep=' ')


def main():
    m = list(input())
    a, b, c = int(m[0]), int(m[1]), int(m[2])
    solution(a, b, c)


if __name__ == '__main__':
    main()
