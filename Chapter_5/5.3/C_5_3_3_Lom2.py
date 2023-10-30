def func(a, b, c):
    return ''.join(map(str, (a, b, c)))


class Error:
    def __repr__(self):
        raise Exception


try:
    Error1 = Error()
    func(Error1)

except Exception:
    print('Ура! Ошибка!')
