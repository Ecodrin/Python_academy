def solution(*args):
    b = args[0]
    k = -1
    last_h = 0
    for i in range(len(b)):
        h = b[i] % 256
        r = b[i] // 256 % 256
        m = b[i] // 256 // 256
        r_h = (37 * (m + r + last_h)) % 256
        if r_h != h or r_h > 100:
            k = i
            break
        last_h = r_h
    print(k)


def main():
    n = int(input())
    b = []
    for i in range(n):
        b.append(int(input()))
    solution(b)


if __name__ == '__main__':
    main()
