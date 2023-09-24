def solution(n: int):
    s = {
        0: 'Манная',
        1: 'Гречневая',
        2: 'Пшённая',
        3: 'Овсяная',
        4: 'Рисовая'
    }
    for i in range(n):
        print(s[i % 5])


def main():
    n = int(input())
    solution(n)


if __name__ == '__main__':
    main()
