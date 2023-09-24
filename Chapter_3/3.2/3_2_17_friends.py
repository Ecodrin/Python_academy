def solution(s: dict):
    for x1 in s:
        print(x1, end=': ')
        ss = []
        for x2 in s[x1]:
            for x3 in s[x2]:
                if x3 != x1 and x3 not in ss and x3 not in s[x1]:
                    ss.append(x3)
        print(*(sorted(ss)), sep=', ')


def main():
    s = dict()
    while (r := input()) != '':
        x = r.split()
        a, b = x[0], x[1]
        if s.get(a, 0) != 0:
            s[a].append(b)
        else:
            s[a] = [b]
        if s.get(b, 0) != 0:
            s[b].append(a)
        else:
            s[b] = [a]
    s = dict(sorted(s.items()))
    solution(s)


if __name__ == '__main__':
    main()
