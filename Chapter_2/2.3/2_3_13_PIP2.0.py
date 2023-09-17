def solution(*args):
    m = args[0]
    n = m[0]
    ss = 'я' * 100
    for i in range(1, n + 1):
        if m[i] < ss:
            ss = m[i]
    print(ss)


def main():
    n = int(input())
    s = [n]
    for i in range(n):
        s.append(input())
    solution(s)


if __name__ == '__main__':
    main()
