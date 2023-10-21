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
            self.x, self.y = 0, 0
        elif len(args) == 1:
            self.x, self.y = args[0]
        else:
            self.x, self.y = args

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f"PatchedPoint({self.x}, {self.y})"


point = PatchedPoint()
print(point)
point.move(2, -3)
print(repr(point))
