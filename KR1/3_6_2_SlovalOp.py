def solution(sl):
    for key in sl.keys():
        print(key, end=' "')
        s = ''
        for j in sorted(set(sl[key])):
            s += j + '. '
        print(s[:-2] + '"')


def main():
    sl = dict()
    while (s := input()) != '':
        s = s.split()
        for j in range(len(s)):
            ind = len(s[j]) // 2
            if len(s[j]) % 2 == 0:
                ind -= 1
            if s[j][ind].lower() in sl:
                sl[s[j][ind].lower()].append(s[j].upper())
                sl[s[j][ind].lower()] = sorted(sl[s[j][ind].lower()])
            else:
                sl[s[j][ind].lower()] = [s[j].upper()]
    solution(sl)


if __name__ == '__main__':
    main()
