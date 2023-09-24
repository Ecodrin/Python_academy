def solution(*args):
    s = args[0]
    ll = len(s) - (len(s) - len(set(s))) * 2
    if ll == 0:
        print('Таких нет')
    else:
        s = sorted(s)
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                print(s[i])


def main():
    n = int(input())
    m = int(input())
    s = []
    for i in range(m + n):
        s.append(input())
    solution(s)


if __name__ == '__main__':
    main()
