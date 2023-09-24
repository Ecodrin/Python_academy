def solution(*args):
    sl = args[0]
    sl = dict(sorted(sl.items()))
    k = args[1]
    ll = sum([1 for i in sl if k in sl[i]])
    if ll == 0:
        print('Таких нет')
    else:
        for i in sl:
            if k in sl[i]:
                print(i)


def main():
    n = int(input())
    sl = dict()
    for i in range(n):
        ss = input().split()
        name, s = ss[0], ss[1:]
        sl[name] = s
    k = input()
    solution(sl, k)


if __name__ == '__main__':
    main()
