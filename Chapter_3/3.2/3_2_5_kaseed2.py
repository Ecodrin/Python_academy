def solution(*args):
    s = args[0]
    ll = len(s) - (len(s) - len(set(s))) * 2
    if ll == 0:
        print('Таких нет')
    else:
        print(ll)


def main():
    n = int(input())
    m = int(input())
    s = []
    for i in range(m + n):
        s.append(input())
    solution(s)


if __name__ == '__main__':
    main()
