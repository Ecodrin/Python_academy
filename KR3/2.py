def main():
    s = input()
    a = int(input())
    b = int(input())
    if 'sum' in s:
        print(a + b)
    if 'sub' in s:
        print(a - b)
    if 'mult' in s:
        print(a * b)
    if 'div' in s:
        print(a // b)


if __name__ == '__main__':
    main()
