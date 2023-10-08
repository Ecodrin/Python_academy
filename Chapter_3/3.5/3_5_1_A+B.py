from sys import stdin


def solution(su):
    print(su)


def main():
    su = sum(map(int, stdin.read().split()))
    solution(su)


if __name__ == '__main__':
    main()
