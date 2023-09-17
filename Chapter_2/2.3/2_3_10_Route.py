def solution(*args):
    m = args[0]
    x = 0
    y = 0
    for i in range(len(m)):
        match m[i][0]:
            case 'СЕВЕР':
                y += m[i][1]
            case 'ВОСТОК':
                x += m[i][1]
            case 'ЗАПАД':
                x -= m[i][1]
            case 'ЮГ':
                y -= m[i][1]
    print(y)
    print(x)


def main():
    m = []
    while (s := input()) != 'СТОП':
        n = int(input())
        m.append([s, n])
    solution(m)


if __name__ == '__main__':
    main()
