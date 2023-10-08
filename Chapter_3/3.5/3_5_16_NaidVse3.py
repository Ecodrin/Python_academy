from sys import stdin


def solution(sent, file_names):
    fl = False
    for file in file_names:
        with open(file, 'r', encoding='UTF-8') as f:
            file_text = ' '.join(f.read().lower().split())
            if sent in file_text:
                fl = True
                print(file)
    if not fl:
        print('404. Not Found')


def main():
    sent = ' '.join(input().strip().lower().split())
    file_names = []
    for name in stdin:
        file_names.append(name.rstrip('\n'))
    solution(sent, file_names)


if __name__ == '__main__':
    main()
