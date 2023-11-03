from requests import get


def main():
    s = input()
    su = 0
    while (c := int(get('http://' + s).content.decode())) != 0:
        su += c
    print(su)


if __name__ == '__main__':
    main()
