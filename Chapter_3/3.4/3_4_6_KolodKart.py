import itertools


def solution(s):
    x = list(itertools.product(['2', '3', '4', '5', '6', '7', '8', '9',
                                '10', 'валет', 'дама', 'король', 'туз'],
                               ['пик', 'треф', 'бубен', 'червей']))
    for i, j in x:
        if j != s:
            print(i, j)


def main():
    s = input()
    solution(s)


if __name__ == '__main__':
    main()
