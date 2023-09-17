def solution(*args):
    m = args[0]
    s = 0
    for i in range(len(m)):
        if m[i] >= 500:
            s += m[i] * 0.9
        else:
            s += m[i]
    print(s)


def main():
    s = []
    while (x := float(input())) != 0:
        s.append(x)
    solution(s)


if __name__ == '__main__':
    main()
