def solution(x: int):
    print('А Б В')
    for i in range(1, x):
        for j in range(1, x):
            for k in range(1, x):
                if i + j + k == x:
                    print(i, j, k)


def main():
    n = int(input())
    solution(n)


if __name__ == '__main__':
    main()
