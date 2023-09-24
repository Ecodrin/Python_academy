def solution(*args):
    x = args[0]
    k = dict()
    for i in range(len(x)):
        x1, y1 = x[i][0] // 10, x[i][1] // 10
        if (x1, y1) in k:
            k[(x1, y1)] += 1
        else:
            k[(x1, y1)] = 1
    print(max(k.values()))


def main():
    n = int(input())
    x = []
    for i in range(n):
        x.append(list(map(int, input().split())))
    x.sort()
    solution(x)


if __name__ == '__main__':
    main()
