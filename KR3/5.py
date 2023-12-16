def main():
    n = int(input())
    m = []
    for i in range(n):
        s = []
        while (x := input()) != 'next':
            s.append(int(x))
        m.append(sum(s) / len(s))
    print(f"{max(m):.2f}")


if __name__ == '__main__':
    main()
