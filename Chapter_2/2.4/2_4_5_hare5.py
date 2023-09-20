def solution(*args):
    m = args[0]
    k = 0
    for i in range(len(m)):
        if 'зайка' in m[i]:
            k += 1
    print(k)


def main():
    n = int(input())
    m = []
    k = 0
    ss = ''
    while k < n:
        s = input()
        ss += s
        if s == 'ВСЁ':
            k += 1
            m.append(ss)
            ss = ''
    solution(m)


if __name__ == '__main__':
    main()
