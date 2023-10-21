def solution(n, s):
    for i in range(n):
        string = s[i]
        start = int(string[string.index('^') + 1:string.rindex('^')])
        end = int(string[string.rindex('^') + 1:])
        string = string[:string.index('^')]
        step = (len(string) % 4)
        print(string[start:end:step])


def main():
    s = []
    n = int(input())
    for i in range(n):
        s.append(input())
    solution(n, s)


if __name__ == '__main__':
    main()
