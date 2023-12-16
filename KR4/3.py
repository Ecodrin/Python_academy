'''def max_diff(*numbers, div=2):
    s = sum(numbers)
    if s % div == 0:
        return s
    ost = [1000000000 for i in range(div)]
    for i in range(len(numbers)):
        ost[numbers[i] % div] = min(ost[numbers[i] % div], numbers[i])
    return s - ost[s % div]
'''
def max_diff(*numbers, div=7):
    maxs = -9999999999
    for i in numbers:
        for j in numbers:
            if (i - j) % div == 0 and maxs < (i - j):
                maxs = i - j
    return maxs



numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = max_diff(*numbers)
print(result)