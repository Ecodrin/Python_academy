def solution(*args):
    s = args[0]
    a = sorted(set(s))
    fl = False
    for i in a:
        if s.count(i) > 1:
            fl = True
            print(i, '-', s.count(i))
    if not fl:
        print('Однофамильцев нет')


def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    solution(s)


if __name__ == '__main__':
    main()
