def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def solution(*args):
    m = args[0]
    n = len(m)
    p_d = get_nod(m[0], m[1])
    for i in range(2, n):
        p_d = get_nod(p_d, m[i])
    print(p_d)


def main():
    n = int(input())
    s = []
    for _ in range(n):
        s.append(int(input()))
    solution(s)


if __name__ == '__main__':
    main()
