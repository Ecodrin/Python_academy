import math


def solution(number: float):
    x1 = math.log(math.pow(number, 3 / 16), 32)
    x2 = math.pow(number, math.cos(math.pi * number / (2 * math.e)))
    x3 = math.pow(math.sin(number / math.pi), 2)
    print(x1 + x2 - x3)


def main():
    number = float(input())
    solution(number)


if __name__ == '__main__':
    main()
