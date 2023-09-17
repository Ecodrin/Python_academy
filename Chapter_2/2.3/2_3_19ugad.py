def solution():
    pass


def main():
    le = 1
    r = 1000
    while le <= r:
        sr = (le + r) // 2
        print(sr)
        s = input()
        if s == 'Угадал!':
            break
        else:
            if s == 'Больше':
                le = sr + 1
            else:
                r = sr - 1


if __name__ == '__main__':
    main()
