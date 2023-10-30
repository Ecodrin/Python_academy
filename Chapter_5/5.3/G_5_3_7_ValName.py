class Errors(Exception):
    pass


class CyrillicError(Errors):
    pass


class CapitalError(Errors):
    pass


def checking_for_сyrillic(initials):
    alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    for c in initials:
        if c.lower() not in alf:
            raise CyrillicError
    return True


def checking_for_capital(initials):
    if initials[0].isupper() and all(initials[i].islower() for i in range(1, len(initials))):
        return True
    raise CapitalError


def name_validation(initials):
    if not isinstance(initials, str):
        raise TypeError
    if checking_for_сyrillic(initials) and checking_for_capital(initials):
        return initials
