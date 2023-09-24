def solution(s: str):
    s = s.lower()
    s = s.split()
    s = ''.join(s)
    print(max(sorted(list(s)), key=s.count))


def main():
    s = ''
    while (b := input()) != 'ФИНИШ':
        s += b
    solution(s)


if __name__ == '__main__':
    main()
