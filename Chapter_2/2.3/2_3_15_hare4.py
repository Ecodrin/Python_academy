def solution(*args):
    n = args[0]
    m = args[1]
    k = 0
    for i in range(n):
        if 'зайка' in m[i]:
            k += 1
    print(k)


def main():
    n = int(input())
    s = [input() for _ in range(n)]
    solution(n, s)


if __name__ == '__main__':
    main()
