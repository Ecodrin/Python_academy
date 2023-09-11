import datetime


def solution(*args):
    print(str(datetime.time((args[0] + (args[1] + args[2]) // 60) % 24, (args[1] + args[2]) % 60))[:-3])


def main():
    n = int(input())
    m = int(input())
    t = int(input())
    solution(n, m, t)


if __name__ == '__main__':
    main()
