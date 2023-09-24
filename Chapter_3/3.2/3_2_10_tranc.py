def solution(s: str):
    sl = {
        'А': 'A', 'Б': 'B', 'В': 'V',
        'Г': 'G', 'Д': 'D', 'Е': 'E',
        'Ё': 'E', 'Ж': 'Zh', 'З': 'Z',
        'И': 'I', 'Й': 'I', 'К': 'K',
        'Л': 'L', 'М': 'M', 'Н': 'N',
        'О': 'O', 'П': 'P', 'Р': 'R',
        'С': 'S', 'Т': 'T', 'У': 'U',
        'Ф': 'F', 'Х': 'Kh', 'Ц': 'Tc',
        'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch',
        'Ы': 'Y', 'Э': 'E', 'Ю': 'Iu',
        'Я': 'Ia', 'Ь': '', 'Ъ': ''
    }
    s_itog = ''
    for i in range(len(s)):
        if s[i].upper() in sl.keys():
            if s[i].islower():
                s_itog += sl[s[i].upper()].lower()
            elif s[i].isupper():
                s_itog += sl[s[i]].capitalize()
        else:
            s_itog += s[i]
    print(s_itog)


def main():
    s = input()
    solution(s)


if __name__ == '__main__':
    main()
