from sys import stdin


def solution(s: list[int]):
    print(round(sum(s) / len(s)))


def main():
    lines = []
    for line in stdin:
        s = line.split()
        lines.append(int(s[2]) - int(s[1]))
    solution(lines)


if __name__ == '__main__':
    main()
