def solution():
    pass


def main():
    with open('secret.txt', 'r', encoding='UTF-8') as f:
        text = f.read()
    for i in text:
        print(chr(ord(i) & 255), end='')


if __name__ == '__main__':
    main()
