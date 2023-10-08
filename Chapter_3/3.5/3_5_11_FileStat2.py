import json


def solution(numbers: list[int], name_output):
    stats = {
        "count": len(numbers),
        "positive_count": sum([1 for i in numbers if i > 0]),
        "min": min(numbers),
        "max": max(numbers),
        "sum": sum(numbers),
        "average": float(f'{sum(numbers) / len(numbers):.2f}')
    }
    with open(name_output, 'w', encoding='UTF-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=4)


def main():
    name1 = input()
    name2 = input()
    with open(name1, 'r', encoding='UTF-8') as file_input:
        numbers = list(map(int, file_input.read().split()))
    solution(numbers, name2)


if __name__ == '__main__':
    main()
