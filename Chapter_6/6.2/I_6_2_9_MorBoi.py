import pandas as pd


def solution(x1, y1, x2, y2):
    a = pd.read_csv("data.csv")
    b = a[(x1 <= a["x"]) & (a["x"] <= x2) & (a["y"] <= y1) & (y2 <= a["y"])]
    print(b)


def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    solution(x1, y1, x2, y2)


if __name__ == '__main__':
    main()
