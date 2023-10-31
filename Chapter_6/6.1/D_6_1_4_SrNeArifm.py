from math import sqrt, prod


def solution(numbers):
    print(prod(numbers) ** (1 / len(numbers)))


def main():
    solution(list(map(float, input().split())))


if __name__ == '__main__':
    main()
