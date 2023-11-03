from requests import get
import json


def main():
    s = input()
    a = json.loads(get('http://' + s).content)
    su = 0
    for i in a:
        if isinstance(i, int):
            su += i
    print(su)


if __name__ == '__main__':
    main()
