def main():
    m = int(input())
    n = int(input())
    print(*[i for i in range(n, m + 1, (n - m) % 10)], sep=', ')


if __name__ == '__main__':
    main()
