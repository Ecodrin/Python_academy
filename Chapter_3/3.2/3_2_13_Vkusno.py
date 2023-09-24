def solution(*args):
    today = args[0]
    d = args[1]
    prasd = sorted(today - d)
    if len(prasd) == 0:
        print('Готовить нечего')
    else:
        for i in prasd:
            print(i)


def main():
    n = int(input())
    today = set()
    for i in range(n):
        today.add(input())
    m = int(input())
    d = set()
    for i in range(m):
        mm = int(input())
        for j in range(mm):
            d.add(input())
    solution(today, d)


if __name__ == '__main__':
    main()
