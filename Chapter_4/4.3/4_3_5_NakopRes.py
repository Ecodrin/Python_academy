def result_accumulator(f):
    queue = []

    def decorated(*args, method='accumulate'):
        nonlocal queue
        if method == 'accumulate':
            queue.append(f(*args))
        else:
            queue.append(f(*args))
            q = queue
            queue = []
            return q
    return decorated


@result_accumulator
def get_letters(text: str) -> str:
    return ''.join(sorted(set(filter(str.isalpha, text.lower()))))


print(get_letters('Hello, world!'))
print(get_letters('Декораторы это круто =)'))
print(get_letters('Ехали медведи на велосипеде', method='drop'))
