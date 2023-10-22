class Fraction:
    def __init__(self, *args):
        if len(args) == 1:
            self.our_numerator = int(args[0][:args[0].index('/')])
            self.our_denominator = int(args[0][args[0].index('/') + 1:])
        else:
            self.our_numerator = args[0]
            self.our_denominator = args[1]

    def using_nod(self):
        num = self.our_numerator
        dem = self.our_denominator
        while num % dem != 0:
            num, dem = dem, num % dem
        self.our_denominator //= dem
        self.our_numerator //= dem

    def denominator(self, number=None):
        if number is None:
            return abs(self.our_denominator)
        self.our_denominator = number
        self.using_nod()
        return abs(self.our_denominator)

    def numerator(self, number=None):
        if number is None:
            return abs(self.our_numerator)
        self.our_numerator = number
        self.using_nod()
        return abs(self.our_numerator)

    def __str__(self):
        self.using_nod()
        return f'{self.our_numerator}/{self.our_denominator}'

    def __repr__(self):
        self.using_nod()
        return f'Fraction({self.our_numerator}/{self.our_denominator})'

    def __neg__(self):
        self.using_nod()
        return Fraction(self.our_numerator * (-1), self.our_denominator)
