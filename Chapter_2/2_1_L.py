def solution(*args):
    s = ''
    a = args[0]
    b = args[1]
    while len(a) < 3:
        a = '0' + a
    while len(b) < 3:
        b = '0' + b
    for i in range(3):
        s += str((int(a[i]) + int(b[i])) % 10)
    if s[0] != '0':
        print(s)
    elif s[:2] == '00':
        print(s[-1])
    else:
        print(s[1:])


def main():
    a = input()
    b = input()
    solution(a, b)


if __name__ == '__main__':
    main()
