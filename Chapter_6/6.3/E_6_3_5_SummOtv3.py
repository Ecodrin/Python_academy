from requests import get
import json
from sys import stdin


def main():
    url = input()
    su = 0
    for param in stdin:
        param = param.rstrip('\n')
        for x in json.loads(get(f"http://{url}{param}").content):
            if isinstance(x, int):
                su += x
    print(su)


if __name__ == '__main__':
    main()
