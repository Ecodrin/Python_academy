def solution(*args):
    s = args[0]
    m = set()
    for i in range(len(s)):
        x = s[i].split()
        for j in range(len(x)):
            if x[j] == 'зайка':
                if 1 < j < len(x) - 1:
                    m.add(x[j - 1])
                    m.add(x[j + 1])
                elif j >= 1:
                    m.add(x[j - 1])
                elif j < len(x) - 1:
                    m.add(x[j + 1])
    for i in m:
        print(i)


def main():
    s = []
    while (b := input()) != '':
        s.append(b)
    solution(s)


if __name__ == '__main__':
    main()
