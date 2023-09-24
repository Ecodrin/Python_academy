def solution(s: str):
    x, y = map(int, s.split())
    print(x + y)


def main():
    s = input()
    solution(s)


if __name__ == '__main__':
    main()
