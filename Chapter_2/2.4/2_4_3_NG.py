def solution(x: int):
    y = 1
    k = 0
    for i in range(1, x + 1):
        k += 1
        if k == y:
            print(i, end='\n')
            k = 0
            y += 1
        else:

            print(i, end=' ')


def main():
    x = int(input())
    solution(x)


if __name__ == '__main__':
    main()
