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


point = Point(3, 5)
print(point.x, point.y)


first_point = Point(2, -7)
second_point = Point(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))
