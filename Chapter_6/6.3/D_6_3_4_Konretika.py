from requests import get
import json


def main():
    url = input()
    key = input()
    s = json.loads(get(f'http://{url}').content)
    if key in s:
        print(s[key])
    else:
        print("No data")


if __name__ == '__main__':
    main()
