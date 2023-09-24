def solution(*args):
    products = args[0]
    d = sorted(args[1])
    fl_gold = False
    for i in range(len(d)):
        name = d[i][0]
        k = d[i][1]
        fl = True
        for j in range(2, k + 2):
            if d[i][j] not in products:
                fl = False
                break
        if fl:
            print(name)
            fl_gold = fl
    if not fl_gold:
        print('Готовить нечего')


def main():
    n = int(input())
    products = set()
    for i in range(n):
        products.add(input())
    mm = int(input())
    d = []
    for i in range(mm):
        s = input()
        m = int(input())
        x = [s, m]
        for j in range(m):
            x.append(input())
        d.append(x)
    solution(products, d)


if __name__ == '__main__':
    main()
