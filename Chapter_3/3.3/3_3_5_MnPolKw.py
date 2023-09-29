numbers = [1, 2, 3, 4, 5]
print(set([i for i in set(numbers) if int(i ** 0.5) ** 2 == i]))