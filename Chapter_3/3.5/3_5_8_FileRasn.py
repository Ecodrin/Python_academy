def solution(*args):
    name_ouput = args[1]
    words = sorted(args[0])
    with open(name_ouput, 'w', encoding='UTF-8') as file3:
        file3.writelines(words)


def main():
    name1 = input()
    name2 = input()
    name3 = input()
    word1 = set()
    word2 = set()
    with open(name1, 'r', encoding='UTF-8') as file1:
        [word1.add(i + '\n') for i in file1.read().split()]
    with open(name2, 'r', encoding='UTf-8') as file2:
        [word2.add(i + '\n') for i in file2.read().split()]
    solution(word1 ^ word2, name3)


if __name__ == '__main__':
    main()
