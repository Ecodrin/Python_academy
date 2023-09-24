def solution(*args):
    m = args[0]
    fl = True
    for i in range(len(m)):
        m[i] = m[i].capitalize()
        if not(m[i][0] == 'А' or m[i][0] == 'Б' or m[i][0] == 'В'):
            fl = False
    if fl:
        print('YES')
    else:
        print('NO')


def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    solution(s)


if __name__ == '__main__':
    main()
