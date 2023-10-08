from sys import stdin


def solution(s):
    request = s.pop(-1)
    [print(i) for i in s if request.lower() in i.lower()]


def main():
    lines = []
    for i in stdin:
        lines.append(i.rstrip('\n'))
    solution(lines)


if __name__ == '__main__':
    main()
