import itertools


def main():
    s = input().split('; ')
    s = set(s)
    n = int(input())
    ss = []
    for x in itertools.permutations(s, r=n):
        ss.append(''.join(x))
    ss = sorted(ss)
    for j in ss:
        print(j)


if __name__ == '__main__':
    main()
