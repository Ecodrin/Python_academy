def solution(a: int, b: int):
    m = 0
    i = max(a, b) + 1
    while True:
        if i % a == 0 and i % b == 0:
            print(i)
            break
        i += 1


def main():
    a = int(input())
    b = int(input())
    solution(a, b)


if __name__ == '__main__':
    main()
