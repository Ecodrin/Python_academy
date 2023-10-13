def same_type(f):

    def decorated(*args, **kwargs):
        if all(isinstance(item, type(args[0])) for item in args):
            return f(*args)
        else:
            print('Обнаружены различные типы данных')
    return decorated


@same_type
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5.2) or 'Fail')
print(a_plus_b(7, '9') or 'Fail')
print(a_plus_b(-3, 5) or 'Fail')

