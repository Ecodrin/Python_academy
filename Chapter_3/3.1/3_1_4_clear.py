def solution(*args):
    s = args[0]
    for i in range(len(s)):
        if s[i][-3:] == '@@@':
            continue
        elif s[i][:2] == '##':
            print(s[i][2:])
        else:
            print(s[i])


def main():
    s = []
    while (m := input()) != '':
        s.append(m)
    solution(s)


if __name__ == '__main__':
    main()
