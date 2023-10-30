class Errors(Exception):
    pass


class BadCharacterError(Errors):
    pass


class StartsWithDigitError(Errors):
    pass


def checking_character(name):
    alf = 'abcdefghijklmnopqrstuvwxyz'
    if all((i.isdigit() or i.lower() in alf or i == '_') for i in name):
        return True
    raise BadCharacterError


def checking_digits(name):
    if name[0].isdigit():
        raise StartsWithDigitError
    return True


def username_validation(*args):
    name = args[0]
    if not isinstance(name, str):
        raise TypeError
    if checking_character(name) and checking_digits(name):
        return name
