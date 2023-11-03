import json
from requests import post


def main():
    url = input()
    username = input()
    last_name = input()
    first_name = input()
    email = input()
    req = json.dumps({"username": username,
                      "last_name": last_name,
                      "first_name": first_name,
                      "email": email})
    post(f'http://{url}/users', req)


if __name__ == '__main__':
    main()
