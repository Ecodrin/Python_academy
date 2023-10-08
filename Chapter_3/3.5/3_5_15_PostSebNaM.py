import json
from sys import stdin


def solution(s: list[int]):
    with open("scoring.json", "r", encoding="UTF-8") as f:
        table = json.load(f)
    k = 0
    su = 0
    for i in range(len(table)):
        points = table[i]["points"]
        tests = table[i]["tests"]
        for j in tests:
            if j["pattern"] == str(s[k]):
                su += points // len(tests)
            k += 1
    print(su)


def main():
    s = []
    for i in stdin:
        s.append(int(i.rstrip('\n')))
    solution(s)


if __name__ == '__main__':
    main()
