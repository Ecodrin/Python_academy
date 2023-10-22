import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x_change, y_change):
        self.x += x_change
        self.y += y_change

    def length(self, second_point_in):
        x_2, y_2 = second_point_in.x, second_point_in.y
        return round(math.sqrt((self.x - x_2) ** 2 + (self.y - y_2) ** 2), 2)


class PatchedPoint(Point):

    def __init__(self, *args):
        if not args:
            super().__init__(0, 0)
        elif len(args) == 1:
            super().__init__(*args[0])
        else:
            super().__init__(*args)

    def __add__(self, coord_range):
        return PatchedPoint(self.x + coord_range[0], self.y + coord_range[1])

    def __iadd__(self, coord_range):
        self.x += coord_range[0]
        self.y += coord_range[1]
        return self

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f"PatchedPoint({self.x}, {self.y})"


first_point = second_point = PatchedPoint((2, -7))
first_point += (7, 3)
print(first_point, second_point, first_point is second_point)
