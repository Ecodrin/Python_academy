from sys import stdin


def solution(test):
    for i in test:
        if not i.startswith('#'):
            print(i[:i.find('#')])


def main():
    test = stdin.readlines()
    solution(test)


if __name__ == '__main__':
    main()
