class Rectangle:

    def __init__(self, coordinate_1, coordinate_2):
        self.size = [abs(coordinate_1[0] - coordinate_2[0]), abs(coordinate_1[1] - coordinate_2[1])]
        self.cooradinate_centre = [min(coordinate_1[0], coordinate_2[0]) + self.size[0] / 2,
                                   min(coordinate_1[1], coordinate_2[1]) + self.size[1] / 2]

    def perimeter(self):
        return round(sum(self.size) * 2, 2)

    def area(self):
        return round(self.size[0] * self.size[1], 2)

    def get_pos(self):
        return (round(self.cooradinate_centre[0] - self.size[0] / 2, 2),
                round(self.cooradinate_centre[1] + self.size[1] / 2, 2))

    def get_size(self):
        return round(self.size[0], 2), round(self.size[1], 2)

    def move(self, dx, dy):
        self.cooradinate_centre[0] += dx
        self.cooradinate_centre[1] += dy

    def resize(self, wight, height):
        self.cooradinate_centre[0] = round(self.cooradinate_centre[0] - self.size[0] / 2 + wight / 2, 2)
        self.cooradinate_centre[1] = round(self.cooradinate_centre[1] + self.size[1] / 2 - height / 2, 2)
        self.size = [wight, height]

    def turn(self):
        self.size = self.size[::-1]

    def scale(self, factor):
        self.size[0], self.size[1] = [round(self.size[0] * factor, 2), round(self.size[1] * factor, 2)]


rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.scale(2.0)
print(rect.get_pos(), rect.get_size(), sep='\n')
