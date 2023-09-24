def solution(*args):
    d = args[0]
    x = []
    for i in d:
        if d[i] == 1:
            x.append(i)
    x.sort()
    for i in x:
        print(i)


def main():
    n = int(input())
    d = dict()
    for i in range(n):
        x = input().split()
        x = [i[:-1] if i[-1] == ',' else i for i in x]
        x = x[1:]
        x = list(set(x))
        for j in range(len(x)):
            if x[j] in d:
                d[x[j]] += 1
            else:
                d[x[j]] = 1
    solution(d)


if __name__ == '__main__':
    main()
