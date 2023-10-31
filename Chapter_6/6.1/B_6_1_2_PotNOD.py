from sys import stdin
from math import gcd


def main():
    for string in stdin:
        print(gcd(*list(map(int, string.split()))))


if __name__ == '__main__':
    main()
