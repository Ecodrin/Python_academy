def ch(n):
    k = 0
    for i in str(n):
        if i in '02468':
            k += 1
    return k


def solution(name1, name2, name3, name4):
    f1 = open(name1, 'r', encoding='UTF-8')
    f2 = open(name2, 'w', encoding='UTF-8')
    f3 = open(name3, 'w', encoding='UTF-8')
    f4 = open(name4, 'w', encoding='UTF-8')
    for line in f1:
        numbers = line.split()
        numbersC = []
        numbersNC = []
        numbersCNC = []
        for i in numbers:
            c = ch(i)
            nc = len(str(i)) - c
            if c > nc:
                numbersC.append(i)
            elif c < nc:
                numbersNC.append(i)
            else:
                numbersCNC.append(i)
        f2.write(' '.join(numbersC) + '\n')
        f3.write(' '.join(numbersNC) + '\n')
        f4.write(' '.join(numbersCNC) + '\n')
    f1.close()
    f2.close()
    f3.close()
    f4.close()


def main():
    name1 = input()
    name2 = input()
    name3 = input()
    name4 = input()
    solution(name1, name2, name3, name4)


if __name__ == '__main__':
    main()
