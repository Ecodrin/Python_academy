import json


def solution(name1, name2):
    with open(name1, 'r', encoding='UTF-8') as f1:
        s1 = json.load(f1)
    with open(name2, 'r', encoding='UTF-8') as f2:
        s2 = json.load(f2)
    sl = dict()
    for i in s1:
        x = dict()
        for j in i:
            if j == "name":
                name = i[j]
            else:
                x[j] = i[j]
        sl[name] = x
    for i in s2:
        for j in i:
            if j == 'name':
                name = i[j]
            else:
                if sl[name].get(j, -1) == -1:
                    sl[name][j] = i[j]
                else:
                    sl[name][j] = max(i[j], sl[name][j])
    with open(name1, 'w', encoding='UTF-8') as f1:
        json.dump(sl, f1, ensure_ascii=False, indent=4)


def main():
    name1 = input()
    name2 = input()
    solution(name1, name2)


if __name__ == '__main__':
    main()
