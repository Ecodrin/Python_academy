def make_matrix(size, value  =0):
    matrix = []
    if isinstance(size, tuple):
        x, y = size
    else:
        x, y = size, size
    for i in range(y):
        matrix.append([value for _ in range(x)])
    return matrix


print(make_matrix(3))