def solution(s: str):
    if s != 'Три!':
        print('Режим ожидания...')
    else:
        print('Ёлочка, гори!')
    

def main():
    s = input()
    while s != 'Три!':
        solution(s)
        s = input()
    solution(s)


if __name__ == '__main__':
    main()
