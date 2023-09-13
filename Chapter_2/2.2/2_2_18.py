def solution(*args):
    a = min(args)
    b = max(args)
    c = sum(args) - a - b
    if a ** 2 + c ** 2 == b ** 2:
        print('100%')
    elif a ** 2 + c ** 2 < b ** 2:
        print('велика')
    else:
        print('крайне мала')


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    solution(a, b, c)


if __name__ == '__main__':
    main()
