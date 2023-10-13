def make_linear(args):
    print(args, 'вход')
    lenght = len(args)
    indexs = index_array(args)
    if not indexs:
        return args
    for index in range(len(args)):
        if index in indexs:
            print(index, indexs, args[len(args) - lenght + index], 'Проверка', sep='--')
            args = (args[:len(args) - lenght + index]
                    + make_linear(args[len(args) - lenght + index]) + args[len(args) - lenght + index + 1:])
            print(args, 'выход')
    return args


def index_array(args):
    indexs = []
    for i in range(len(args)):
        if isinstance(args[i], list):
            indexs.append(i)
    return indexs


result = make_linear([[1], 2, [[3], [4, 5]], [6], [7]])

print(result)
