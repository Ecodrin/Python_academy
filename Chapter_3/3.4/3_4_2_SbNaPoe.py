def solution(*args):
    s1 = args[0]
    s2 = args[1]
    s = list(zip(s1, s2))
    for i, j in s:
        print(i, j, sep=' - ')


def main():
    s1 = input().split(', ')
    s2 = input().split(', ')
    solution(s1, s2)


if __name__ == '__main__':
    main()
