def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n - 1) * n


def solution(s: str):
    s = s.split()
    n = []
    for i in range(len(s)):
        print(n)
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
            elif s[i] == '~':
                x = -n[-1]
                n = n[:-1]
                n.append(x)
            elif s[i] == '/':
                x = n[-2] // n[-1]
                n = n[:-2]
                n.append(x)
            elif s[i] == '!':
                x = fact(n[-1])
                n = n[:-1]
                n.append(x)
            elif s[i] == '#':
                x = n[-1]
                n = n[:-1]
                n.append(x)
                n.append(x)
            elif s[i] == '@':
                x = n[-3]
                y = n[-2]
                z = n[-1]
                n = n[:-3]
                n.append(y)
                n.append(z)
                n.append(x)
    print(n[0])


def main():
    s = input()
    solution(s)


if __name__ == '__main__':
    main()
