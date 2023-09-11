def solution(*args):
    print(args[0] + args[2] + 1)


def main():
    c_r = int(input())
    c_g = int(input())
    c_b = int(input())
    solution(c_r, c_g, c_b)


if __name__ == '__main__':
    main()

