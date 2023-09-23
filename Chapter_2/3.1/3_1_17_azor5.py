def solution(s: str):
    s = s.lower()
    s = s.split()
    s = ''.join(s)
    n = len(s)
    if s[:n // 2] == (s[n // 2 + n % 2:])[::-1]:
        print('YES')
    else:
        print('NO')


def main():
    s = input()
    solution(s)


if __name__ == '__main__':
    main()
