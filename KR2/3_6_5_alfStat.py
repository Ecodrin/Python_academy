from sys import stdin
import json


def main():
    sl = {}
    for string in stdin:
        string = string.rstrip('\n')
        for i in range(len(string)):
            if i % 2 == 1:
                if string[i] in sl.keys():
                    sl[string[i]].append(string.lower())
                    sl[string[i]] = sorted(set(sl[string[i]]))
                else:
                    sl[string[i]] = [string.lower()]
    with open('result.json', 'w', encoding='UTF-8') as f:
        json.dump(sl, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
