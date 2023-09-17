def solution(a: int, b: int):
    m = 0
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            m = i
    print(m)


def main():
    a = int(input())
    b = int(input())
    solution(a, b)


if __name__ == '__main__':
    main()
