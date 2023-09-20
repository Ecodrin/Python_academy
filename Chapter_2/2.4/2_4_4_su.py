def solution(*args):
    m = args[0]
    su = 0
    for i in range(len(m)):
        su += sum([int(i) for i in str(m[i])])
    print(su)


def main():
    n = int(input())
    s = []
    for i in range(n):
        x = int(input())
        s.append(x)
    solution(s)


if __name__ == '__main__':
    main()
