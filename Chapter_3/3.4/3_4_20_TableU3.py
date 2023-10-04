import itertools


def sk(s, b):
    p = 0
    for j in range(s.count(b)):
        i = s[p:].index(b) + p
        if ')' not in s[i - 1]:
            s[i - 1] = '(' + s[i - 1]
        else:
            k = s[i - 1].count(')')
            i -= 1
            while k != 0:
                if ')' in s[i] and s[i + 1] != b:
                    k += s[i].count(')')
                if '(' in s[i]:
                    k -= s[i].count('(')
                if k <= 0:
                    s[i] = '(' + s[i]
                    break
                i -= 1
        i = s[p:].index(b) + p
        p = i + 1
        if '(' not in s[i + 1]:
            s[i + 1] = s[i + 1] + ')'
        else:
            k = s[i + 1].count('(')
            i += 1
            while k != 0:
                if ')' in s[i]:
                    k -= s[i].count(')')
                if '(' in s[i] and s[i - 1] != b:
                    k += s[i].count('(')
                if k <= 0:
                    s[i] += ')'
                    break
                i += 1
    return s


def skobi_not(s):
    while 'not' in s:
        i = s.index('not')
        s[i] = '(' + 'not'
        if '(' not in s[i + 1]:
            s[i + 1] += ')'
        else:
            k = 1
            i += 1
            while k != 0:
                if ')' in s[i]:
                    k -= s[i].count(')')
                if '(' in s[i] and s[i - 1] != '(not':
                    k += s[i].count('(')
                if k == 0:
                    s[i] += ')'
                i += 1
    return s


def priority(s: str):
    s = s.replace('(not', '( not')
    s = s.split()
    s = skobi_not(s)
    s = sk(s, 'and')
    s = sk(s, '^')
    s = sk(s, 'or')
    s = sk(s, '<=')
    s = sk(s, '==')
    s = ' '.join(s)
    print(s)
    return s


def solution(s: str):
    sl = set()
    [sl.add(i) for i in s if i.isupper()]
    sl = sorted(sl)
    combo = itertools.product([0, 1], repeat=len(sl))
    s = s.replace('->', '<=')
    s = s.replace('~', '==')
    s = priority(s)
    [print(i, end=' ') for i in sl]
    print('F')
    for i in combo:
        print(*i, int(eval(s, dict(zip(sl, i)))))


def main():
    s = input()
    solution(s)


if __name__ == '__main__':
    main()
