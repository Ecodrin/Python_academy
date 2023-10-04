import itertools


def solution(s: list[str]):
    for val in itertools.accumulate(s):
        print(f'{val} ')


def main():
    s = input().split()
    s = [s[i] + ' ' for i in range(len(s))]
    solution(s)


if __name__ == '__main__':
    main()
