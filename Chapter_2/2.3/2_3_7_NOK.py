def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def solution(a: int, b: int):
    print(a * b // get_nod(a, b))


def main():
    a = int(input())
    b = int(input())
    solution(a, b)


if __name__ == '__main__':
    main()
