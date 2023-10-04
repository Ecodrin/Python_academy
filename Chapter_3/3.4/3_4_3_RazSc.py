import itertools


def solution(x, y, z):
    for val in itertools.count(x, z):
        if val <= y:
            print(f'{val:.2f}')
        else:
            break


def main():
    x, y, z = map(float, input().split())
    solution(x, y, z)


if __name__ == '__main__':
    main()
