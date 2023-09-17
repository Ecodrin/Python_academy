def solution(*args):
    k = 0
    for i in range(len(args[0])):
        s = args[0][i]
        if 'зайка' in s:
            k += 1
    print(k)


def main():
    m = []
    while (s := input()) != 'Приехали!':
        m.append(s)
    solution(m)


if __name__ == '__main__':
    main()
