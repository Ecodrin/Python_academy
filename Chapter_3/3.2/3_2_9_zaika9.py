def solution(*args):
    sl = args[0]
    for i in sl:
        print(i, sl[i])


def main():
    sl = {}
    while (b := input()) != '':
        for i in b.split():
            if i in sl:
                sl[i] += 1
            else:
                sl[i] = 1
    solution(sl)


if __name__ == '__main__':
    main()
