def solution():
    pass


def main():
    nums = [1, 2, 3, 2, 1, 0, -1, -2, -3, -2, -1, 0, 1]
    nums = sorted(nums, key=lambda x: x <= (max(nums) + min(nums)) / 2)
    print(nums)


if __name__ == '__main__':
    main()
