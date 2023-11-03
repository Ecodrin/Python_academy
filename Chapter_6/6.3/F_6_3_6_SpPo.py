from requests import get
import json


def main():
    url = input()
    reqs = json.loads(get(f"http://{url}/users").content)
    fam = []
    for req in reqs:
        fam.append([req["last_name"], req["first_name"]])
    for x, y in sorted(fam):
        print(x, y)


if __name__ == '__main__':
    main()
