import hashlib


class Errors(Exception):
    pass


class MinLengthError(Errors):
    pass


class PossibleCharError(Errors):
    pass


class NeedCharError(Errors):
    pass


def password_validation(power,
                        min_length=8,
                        possible_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',
                        at_least_one=lambda x: x.isdigit()):
    if not isinstance(power, str):
        raise TypeError
    if len(power) < min_length:
        raise MinLengthError
    if not all(i in possible_chars for i in power):
        raise PossibleCharError
    if not any(at_least_one(i) for i in power):
        raise NeedCharError
    return hashlib.sha256(power.encode('UTF-8')).hexdigest()


print(password_validation("Hello12345"))

