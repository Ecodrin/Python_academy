def solution(*args):
    s = args[0]
    sl = set()
    for i in range(len(s)):
        x = s[i].split()
        for j in range(len(x)):
            sl.add(x[j])
    for i in sl:
        print(i)


def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    solution(s)


if __name__ == '__main__':
    main()
