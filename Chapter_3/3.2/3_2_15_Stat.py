def solution(x: list[int]):
    r = []
    for i in x:
        a = bin(i)[2:]
        d = len(a)
        units = a.count('1')
        zero = a.count('0')
        r.append({"digits": d, "units": units, "zeros": zero})
    print(r)


def main():
    y = list(map(int, input().split()))
    solution(y)


if __name__ == '__main__':
    main()
