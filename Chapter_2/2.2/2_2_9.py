def solution(n1: str, n2: str, n3: str):
    if n1[0] < n2[0] and n1[0] < n3[0]:
        print(n1)
    elif n2[0] < n1[0] and n2[0] < n3[0]:
        print(n2)
    else:
        print(n3)


def main():
    name1 = input()
    name2 = input()
    name3 = input()
    solution(name1, name2, name3)


if __name__ == '__main__':
    main()
