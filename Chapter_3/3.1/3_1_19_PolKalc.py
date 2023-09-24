def solution(s: str):
    s = s.split()
    n = []
    for i in range(len(s)):
        if s[i].isdigit():
            n.append(int(s[i]))
        else:
            if s[i] == '*':
                x = n[-1] * n[-2]
                n = n[:-2]
                n.append(x)
            elif s[i] == '+':
                x = n[-1] + n[-2]
                n = n[:-2]
                n.append(x)
            elif s[i] == '-':
                x = n[-2] - n[-1]
                n = n[:-2]
                n.append(x)
    print(n[0])


def main():
    s = input()
    solution(s)


if __name__ == '__main__':
    main()
