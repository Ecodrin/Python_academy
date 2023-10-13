def recursive_digit_sum(x):
    if x // 10 == 0:
        return x % 10
    return x % 10 + recursive_digit_sum(x // 10)


result = recursive_digit_sum(7321346)
print(result)
