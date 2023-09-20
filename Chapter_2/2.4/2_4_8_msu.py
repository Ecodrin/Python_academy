def solution(*args):
    s = args[0]
    maxc = -1
    name_p = 0
    for j in range(len(s)):
        if s[j][1] >= maxc:
            maxc = s[j][1]
            name_p = s[j][0]
    print(name_p)


def main():
    n = int(input())
    s = []
    for i in range(n):
        name = input()
        su = sum([int(j) for j in input()])
        s.append([name, su])
    solution(s)


if __name__ == '__main__':
    main()
