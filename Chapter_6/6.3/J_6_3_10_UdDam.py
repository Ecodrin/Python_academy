from requests import delete


def main():
    url = f'http://{input()}/users/{input()}'
    delete(url)


if __name__ == '__main__':
    main()
