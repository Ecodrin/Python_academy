def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        elif a < b:
            b -= a
    return a


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == '__main__':
    main()
