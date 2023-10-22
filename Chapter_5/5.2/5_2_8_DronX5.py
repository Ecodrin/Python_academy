def nod(num: int, dem: int):
    while num % dem != 0:
        num, dem = dem, num % dem
    return dem


def nok(dem_1: int, dem_2: int):
    return (dem_1 * dem_2) // nod(dem_1, dem_2)


class Fraction:

    def __init__(self, *args):
        if len(args) == 1:
            sila_x = args[0].split('/')
            self.our_numerator = int(sila_x[0])
            self.our_denominator = int(sila_x[1])
        else:
            self.our_numerator = args[0]
            self.our_denominator = args[1]

    def __using_nod(self):
        g = nod(self.our_numerator, self.our_denominator)
        self.our_numerator //= g
        self.our_denominator //= g

    def denominator(self, number=None):
        if number is None:
            return abs(self.our_denominator)
        self.our_denominator = number
        self.__using_nod()
        return self

    def numerator(self, number=None):
        if number is None:
            return abs(self.our_numerator)
        self.our_numerator = number
        self.__using_nod()
        return self

    def __str__(self):
        self.__using_nod()
        return f'{self.our_numerator}/{self.our_denominator}'

    def __repr__(self):
        self.__using_nod()
        return f"Fraction('{self.our_numerator}/{self.our_denominator}')"

    def __neg__(self):
        self.__using_nod()
        return Fraction(self.our_numerator * (-1), self.our_denominator)

    def __add__(self, other):
        numerator_2, denominator_2 = other.our_numerator, other.our_denominator
        our_nok = nok(denominator_2, self.our_denominator)
        return Fraction(self.our_numerator * our_nok // self.our_denominator
                        + numerator_2 * our_nok // denominator_2, our_nok)

    def __sub__(self, other):
        numerator_2, denominator_2 = other.our_numerator, other.our_denominator
        our_nok = nok(denominator_2, self.our_denominator)
        return Fraction(self.our_numerator * our_nok // self.our_denominator
                        - numerator_2 * our_nok // denominator_2, our_nok)

    def __iadd__(self, other):
        numerator_2, denominator_2 = other.our_numerator, other.our_denominator
        our_nok = nok(denominator_2, self.our_denominator)
        self.our_numerator = (self.our_numerator * our_nok // self.our_denominator
                              + numerator_2 * our_nok // denominator_2)
        self.our_denominator = our_nok
        self.__using_nod()
        return self

    def __isub__(self, other):
        numerator_2, denominator_2 = other.our_numerator, other.our_denominator
        our_nok = nok(denominator_2, self.our_denominator)
        self.our_numerator = (self.our_numerator * our_nok // self.our_denominator
                              - numerator_2 * our_nok // denominator_2)
        self.our_denominator = our_nok
        return self

    def __mul__(self, other):
        return Fraction(self.our_numerator * other.our_numerator,
                        self.our_denominator * other.our_denominator)

    def __truediv__(self, other):
        return Fraction(self.our_numerator * other.our_denominator,
                        self.our_denominator * other.our_numerator)

    def __imul__(self, other):
        self.our_numerator *= other.our_numerator
        self.our_denominator *= other.our_denominator
        self.__using_nod()
        return self

    def __itruediv__(self, other):
        self.our_numerator *= other.our_denominator
        self.our_denominator *= other.our_numerator
        self.__using_nod()
        return self

    def reverse(self):
        self.our_numerator, self.our_denominator = self.our_denominator, self.our_numerator
        return self

    def __lt__(self, other):
        return self.our_numerator / self.our_denominator < other.our_numerator / other.our_denominator

    def __le__(self, other):
        return self.our_numerator / self.our_denominator <= other.our_numerator / other.our_denominator

    def __eq__(self, other):
        return self.our_numerator / self.our_denominator == other.our_numerator / other.our_denominator

    def __ne__(self, other):
        return self.our_numerator / self.our_denominator != other.our_numerator / other.our_denominator

    def __gt__(self, other):
        return self.our_numerator / self.our_denominator > other.our_numerator / other.our_denominator

    def __ge__(self, other):
        return self.our_numerator / self.our_denominator >= other.our_numerator / other.our_denominator


a = Fraction(1, 3)
b = Fraction(1, 2)
print(a > b, a < b, a >= b, a <= b, a == b, a >= b)
