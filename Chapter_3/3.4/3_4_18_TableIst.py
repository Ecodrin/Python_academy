import itertools


def solution(s: str):
    print('a b c f')
    x = itertools.product([0, 1], repeat=3)
    for a, b, c in x:
        print(a, b, c, int(eval(s)))


def main():
    s = input()
    solution(s)


if __name__ == '__main__':
    main()
