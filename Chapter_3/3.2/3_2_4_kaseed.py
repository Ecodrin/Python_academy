def solution(*args):
    k_m = args[0]
    k_o = args[1]
    ll = k_m & k_o
    if len(ll) == 0:
        print('Таких нет')
    else:
        print(len(ll))


def main():
    n = int(input())
    m = int(input())
    k_m = set()
    k_o = set()
    for i in range(n):
        k_m.add(input())
    for j in range(m):
        k_o.add(input())
    solution(k_m, k_o)


if __name__ == '__main__':
    main()
