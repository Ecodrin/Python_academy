def solution(n: int):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f'{j} * {i} = {i * j}')


def main():
    x = int(input())
    solution(x)


if __name__ == '__main__':
    main()
