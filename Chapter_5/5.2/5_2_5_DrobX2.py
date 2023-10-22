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
        print(self.our_numerator, self.our_denominator)

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
        self.our_numerator = number
        self.__usingnod()
        return self

    def __str__(self):
        self.__usingnod()
        return f'{self.our_numerator}/{self.our_denominator}'

    def __repr__(self):
        self.__usingnod()
        return f"Fraction('{self.our_numerator}/{self.our_denominator}')"

    def __neg__(self):
        self.__usingnod()
        return Fraction(self.our_numerator * (-1), self.our_denominator)


a = Fraction(-301, 769)
print(a, repr(a), a.our_numerator, a.our_denominator)


