def solution(a: str, b: str):
    a = set(list(a))
    b = set(list(b))
    print(''.join(a & b))


def main():
    a = input()
    b = input()
    solution(a, b)


if __name__ == '__main__':
    main()
