def solution(a: int, b: int, c: int):
    sl = {
        a: 'Петя',
        b: 'Вася',
        c: 'Толя'
    }
    print(f'{sl[max(sl.keys())]: ^24}')
    print(f'  {sl[a + b + c - max(sl.keys()) - min(sl.keys())]: <22}')
    print(f'{sl[min(sl.keys())]: >22}  ')
    print(f'   II{"": >6}I{"": <6}III   ')


def main():
    sr_p = int(input())
    sr_w = int(input())
    sr_t = int(input())
    solution(sr_p, sr_w, sr_t)


if __name__ == '__main__':
    main()
