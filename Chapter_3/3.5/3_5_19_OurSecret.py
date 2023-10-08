def solution(n: int):
    with open('public.txt', 'r', encoding='UTF-8') as file_input:
        text = file_input.read()
    text_itog = ''
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].islower():
                text_itog += chr(((ord(text[i]) - 97 + n) % 26) + 97)
            else:
                text_itog += chr(((ord(text[i]) - 65 + n) % 26) + 65)
        else:
            text_itog += text[i]
    print(text_itog)
    with open('private.txt', 'w', encoding='UTF-8') as file_output:
        file_output.write(text_itog)


def main():
    n = int(input())
    solution(n)


if __name__ == '__main__':
    main()
