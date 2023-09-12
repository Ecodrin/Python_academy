def solution(a: str, b: str, c: str):
    for i in range(len(a)):
        if a[i] in b and a[i] in c:
            print(a[i])
            break


def main():
    a = input()
    b = input()
    c = input()
    solution(a, b, c)


if __name__ == '__main__':
    main()
