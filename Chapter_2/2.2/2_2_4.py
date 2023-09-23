def solution(s1: int, s2: int, s3: int):
    sl = {
        s1: 'Петя',
        s2: 'Вася',
        s3: 'Толя'
    }
    print(f'''1. {sl[max(sl.keys())]}\n2. {sl[s1 + s2 + s3 - min(sl.keys()) 
    - max(sl.keys())]}\n3. {sl[min(sl.keys())]}''')


def main():
    sr_p = int(input())
    sr_w = int(input())
    sr_t = int(input())
    solution(sr_p, sr_w, sr_t)


if __name__ == '__main__':
    main()
