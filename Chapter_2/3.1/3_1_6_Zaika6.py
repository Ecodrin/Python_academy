def solution(*args):
    s = args[0]
    k = 0
    for i in range(len(s)):
        k += s[i].count('зайка')
    print(k)


def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    solution(s)


if __name__ == '__main__':
    main()
