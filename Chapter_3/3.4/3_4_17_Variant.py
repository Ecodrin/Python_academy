import itertools


def solution(s1: str, s2: str, s3: str):
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
    s = itertools.combinations(s, 3)
    fl = False
    for j in s:
        x, y, z = j
        x1, x2 = x
        y1, y2 = y
        z1, z2 = z
        kk = f'{x1} {x2}, {y1} {y2}, {z1} {z2}'
        if kk == s3 or fl:
            if fl and v in kk:
                print(kk)
                break
            fl = True


def main():
    s1 = input()
    s2 = input()
    s3 = input()
    solution(s1, s2, s3)


if __name__ == '__main__':
    main()
