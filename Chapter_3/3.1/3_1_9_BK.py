def solution(*args):
    s = args[0]
    for i in range(len(s)):
        x = s[i].find('#')
        if x == 0:
            continue
        if x == -1:
            print(s[i])
        else:
            print(s[i][:x])


def main():
    s = []
    while (n := input()) != '':
        s.append(n)
    solution(s)


if __name__ == '__main__':
    main()
