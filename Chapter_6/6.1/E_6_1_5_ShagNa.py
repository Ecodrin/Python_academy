import math


def solution(x1, y1, x2, y2):
    print(math.dist((x1, y1), (x2, y2)))


def main():
    x1, y1 = map(float, input().split())
    ro, fi = map(float, input().split())
    '''fi = math.degrees(fi)'''
    solution(x1, y1, ro * math.cos(fi), ro * math.sin(fi))


if __name__ == '__main__':
    main()
