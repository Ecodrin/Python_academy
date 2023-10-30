def nod(num: int, dem: int):
    while num % dem != 0:
        num, dem = dem, num % dem
    return dem


class Fraction:

    def __init__(self, *args):
        if len(args) == 1:
            sila_x = args[0].split('/')
            self.our_numerator = int(sila_x[0])
            self.our_denominator = int(sila_x[1])
        else:
            self.our_numerator = args[0]
            self.our_denominator = args[1]
        self.__usingnod()

    def __usingnod(self):
        g = nod(self.our_numerator, self.our_denominator)
        self.our_numerator //= g
        self.our_denominator //= g

    def denominator(self, number=None):
        if number is None:
            return abs(self.our_denominator)
        self.our_denominator = number
        self.__usingnod()
        return self

    def numerator(self, number=None):
        if number is None:
            return abs(self.our_numerator)
        self.our_numerator = number * self.our_numerator // abs(self.our_numerator)
        self.__usingnod()
        return self

    def __str__(self):
        return f'{self.our_numerator}/{self.our_denominator}'

    def __repr__(self):
        return f"Fraction('{self.our_numerator}/{self.our_denominator}')"

    def __neg__(self):
        return Fraction(self.our_numerator * (-1), self.our_denominator)


fraction = Fraction(3, 9)
print(fraction, repr(fraction))
fraction = Fraction('7/14')
print(fraction, repr(fraction))
