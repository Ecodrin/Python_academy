from requests import get


def main():
    response = get("http://127.0.0.1:5000")
    print(response.content.decode())


if __name__ == '__main__':
    main()

