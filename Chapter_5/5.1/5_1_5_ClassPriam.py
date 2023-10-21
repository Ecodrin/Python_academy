class Rectangle:

    def __init__(self, coordinate_1, coordinate_2):
        self.x1, self.y1 = coordinate_1
        self.x2, self.y2 = coordinate_2

    def perimeter(self):
        return round(abs(self.x1 - self.x2) * 2 + abs(self.y1 - self.y2) * 2, 2)

    def area(self):
        return round(abs(self.x1 - self.x2) * abs(self.y1 - self.y2), 2)


rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.perimeter())

rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.area())
