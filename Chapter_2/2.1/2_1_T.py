def solution(*args):
    n = args[0]
    m = args[1]
    k1 = args[2]
    k2 = args[3]
    x = (m * n - n * k2) / (k1 - k2)
    y = n - x
    print(int(x), int(y), sep=' ')


def main():
    n = int(input())
    m = int(input())
    k1 = int(input())
    k2 = int(input())
    solution(n, m, k1, k2)


if __name__ == '__main__':
    main()
