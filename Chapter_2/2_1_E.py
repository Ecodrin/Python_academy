

def solution(*args):
    print(args[2] - args[0] * args[1])


def main():
    c = int(input())
    w = int(input())
    m = int(input())
    solution(c, w, m)


if __name__ == '__main__':
    main()
