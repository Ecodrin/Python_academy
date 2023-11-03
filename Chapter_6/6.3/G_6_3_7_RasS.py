from requests import get
import json
from sys import stdin


def main():
    url = input()
    idh = int(input())
    string = stdin.read()
    try:
        reqq = json.loads(get(f"http://{url}/users/{idh}").content)
        print(eval('f"""' + string + '"""', reqq))
    except ValueError:
        print('Пользователь не найден')


if __name__ == '__main__':
    main()
