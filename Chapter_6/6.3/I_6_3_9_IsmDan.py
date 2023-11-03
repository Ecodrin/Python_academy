import json

from requests import put, get
from sys import stdin


def main():
    val = input()
    idh = int(input())
    url = f'http://{val}/users/{idh}'
    req = {}
    for string in stdin:
        key, value = string.rstrip('\n').split('=')
        req[key] = value
    put(url, json.dumps(req))


if __name__ == '__main__':
    main()
