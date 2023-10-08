def solution(*args):
    name_output = args[1]
    m = args[0]
    itog = []
    for i in range(len(m)):
        x = ''
        for j in range(len(m[i])):
            if m[i][j] != '\t':
                if j >= 1 and x != '' and m[i][j] == ' ' and x[-1] != ' ':
                    x += m[i][j]
                elif m[i][j] != ' ':
                    x += m[i][j]
        if x != '' and x != '\n':
            itog.append(x)
    with open(name_output, 'w', encoding='UTF-8') as fil2:
        fil2.writelines(itog)


def main():
    name1 = input()
    name2 = input()
    with open(name1, 'r', encoding='UTF-8') as file1:
        s = file1.readlines()
    solution(s, name2)


if __name__ == '__main__':
    main()
