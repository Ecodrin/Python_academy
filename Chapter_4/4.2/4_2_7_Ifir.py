def enter_results(*numbers):
    global res
    if res is None:
        res = []
    res += [[numbers[i], numbers[i + 1]] for i in range(0, len(numbers), 2)]


def get_sum():
    global res
    left_sum = sum(res[i][0] for i in range(len(res)))
    right_sum = sum(res[i][1] for i in range(len(res)))
    return round(left_sum, 2), round(right_sum, 2)


def get_average():
    global res
    left_z = sum(res[i][0] for i in range(len(res))) / len(res)
    right_z = sum(res[i][1] for i in range(len(res))) / len(res)
    return round(left_z, 2), round(right_z, 2)

#больше выкупал условие, чем решал
res = []
enter_results(3.5, 2.14, 45.2, 37.99)
print(get_sum(), get_average())
enter_results(5.2, 7.3)
print(get_sum(), get_average())
enter_results(1.23, 4.56, 3.14, 2.71, 0, 0)
print(get_sum(), get_average())