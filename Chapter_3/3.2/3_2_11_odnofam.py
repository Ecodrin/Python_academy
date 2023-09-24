def solution(*args):
    s = args[0]
    a = set(s)
    k = 0
    for i in a:
        if s.count(i) > 1:
            k += (s.count(i))
    print(k)


def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    solution(s)


if __name__ == '__main__':
    main()
