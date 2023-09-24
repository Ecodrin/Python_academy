def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def solution(*args):
    x = args[0]
    d = args[1]
    n = len(x)
    for i in range(n):
        for j in range(n):
            if j != i and get_nod(x[i], x[j]) == 1:
                d[x[i]].append(x[j])
    for i in d:
        if len(d[i]) > 0:
            y = str(d[i])[1:-1]
            print(i, '-', y)


def main():
    x = list(set(map(int, input().split('; '))))
    d = dict()
    x = sorted(x)
    for i in range(len(x)):
        d[x[i]] = []
    solution(x, d)


if __name__ == '__main__':
    main()
