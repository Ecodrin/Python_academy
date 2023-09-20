def solution(*args):
    m = args[0]
    c = ''
    for i in range(len(m)):
        c += str(max([int(j) for j in m[i]]))
    print(c)


def main():
    n = int(input())
    s = []
    for j in range(n):
        s.append(input())
    solution(s)


if __name__ == '__main__':
    main()
