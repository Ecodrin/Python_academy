def solution(*args):
    ll = args[0]
    n = args[1]
    s = args[2]
    k = 0
    for i in range(n):
        k += len(s[i])
        if k < ll:
            if ll - k <= 3:
                print(s[i][:len(s[i]) - (3 - ll + k)] + '...')
                break
            else:
                print(s[i])
        else:
            r = ll - 3 - k + len(s[i])
            print(s[i][:r] + '...')
            break


def main():
    lll = int(input())
    nnn = int(input())
    sss = []
    for i in range(nnn):
        sss.append(input())
    solution(lll, nnn, sss)


if __name__ == '__main__':
    main()
