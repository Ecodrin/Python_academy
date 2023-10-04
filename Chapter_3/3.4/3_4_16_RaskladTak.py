import itertools


def solution(s1: str, s2: str):
    sl = {
        'буби': 'бубен',
        'пики': 'пик',
        'трефы': 'треф',
        'черви': 'червей'
    }
    x = ['10', '2', '3', '4', '5', '6', '7', '8', '9', 'валет', 'дама', 'король', 'туз']
    x.remove(s2)
    xx = ['бубен', 'пик', 'треф', 'червей']
    v = sl[s1]
    s = itertools.product(x, xx)
    s = itertools.permutations(s, 3)
    k = 0
    for j in s:
        x, y, z = j
        x1, x2 = x
        y1, y2 = y
        z1, z2 = z
        if k < 10 and (x2 == v or y2 == v or z2 == v):
            k += 1
            print(f'{x1} {x2}, {y1} {y2}, {z1} {z2}')


def main():
    s1 = input()
    s2 = input()
    solution(s1, s2)


if __name__ == '__main__':
    main()
