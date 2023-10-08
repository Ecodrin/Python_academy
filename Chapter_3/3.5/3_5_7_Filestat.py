def solution(numbers: list[int]):
    print(len(numbers))
    print(sum([1 for i in numbers if i > 0]))
    print(min(numbers))
    print(max(numbers))
    print(sum(numbers))
    print(f'{sum(numbers) / len(numbers):.2f}')


def main():
    file_name = input()
    with open(file_name, 'r', encoding='UTF-8') as file_input:
        numbers = list(map(int, file_input.read().split()))
    solution(numbers)


if __name__ == '__main__':
    main()
