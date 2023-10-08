def solution(line: list[str]):
    sl = {
        'А': 'A', 'Б': 'B', 'В': 'V',
        'Г': 'G', 'Д': 'D', 'Е': 'E',
        'Ё': 'E', 'Ж': 'ZH', 'З': 'Z',
        'И': 'I', 'Й': 'I', 'К': 'K',
        'Л': 'L', 'М': 'M', 'Н': 'N',
        'О': 'O', 'П': 'P', 'Р': 'R',
        'С': 'S', 'Т': 'T', 'У': 'U',
        'Ф': 'F', 'Х': 'KH', 'Ц': 'TC',
        'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
        'Ы': 'Y', 'Э': 'E', 'Ю': 'IU',
        'Я': 'IA', 'Ь': '', 'Ъ': ''
    }
    for i in range(len(line)):
        per = ''
        for j in range(len(line[i])):
            if line[i][j].upper() in sl.keys():
                if line[i][j].isupper():
                    per += sl[line[i][j]].capitalize()
                else:
                    per += sl[line[i][j].upper()].lower()
            else:
                per += line[i][j]
        line[i] = per
    with open('transliteration.txt', 'w', encoding='UTF-8') as output_file:
        output_file.writelines(line)


def main():
    with open('cyrillic.txt', 'r', encoding='UTF8') as file_input:
        s = file_input.readlines()
    solution(s)


if __name__ == '__main__':
    main()
