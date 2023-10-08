from sys import stdin


def solution(words):
    itog = set()
    [itog.add(i) for i in words if i.upper() == i[::-1].upper()]
    [print(i) for i in sorted(itog)]


def main():
    words = stdin.read().split()
    solution(words)


if __name__ == '__main__':
    main()
