def main():
    n = int(input())
    p = int(input())
    s = []
    for _ in range(1, n):
        x = int(input())
        if x < p:
            s.append(x)
        p = x
    print(max(s))


if __name__ == '__main__':
    main()
