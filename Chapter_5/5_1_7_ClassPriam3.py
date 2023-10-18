class Rectangle:

    def __init__(self, coordinate_1, coordinate_2):
        self.x1, self.y1 = coordinate_1
        self.x2, self.y2 = coordinate_2
        self.por()

    def por(self):

        if self.x1 >= self.x2:
            self.x1, self.x2 = self.x2, self.x1
        if self.y1 <= self.y2:
            self.y1, self.y2 = self.y2, self.y1

    def perimeter(self):
        return round(abs(self.x1 - self.x2) * 2 + abs(self.y1 - self.y2) * 2, 2)

    def area(self):
        return round(abs(self.x1 - self.x2) * abs(self.y1 - self.y2), 2)

    def get_pos(self):
        return tuple([round(self.x1, 2), round(self.y1, 2)])

    def get_size(self):
        return tuple([round(abs(self.x2 - self.x1), 2), round(abs(self.y1 - self.y2), 2)])

    def move(self, dx, dy):
        self.por()
        self.x1 += dx
        self.x2 += dx
        self.y1 += dy
        self.y2 += dy

    def resize(self, width, height):
        self.por()
        self.x2 = self.x1 + width
        self.y2 = self.y1 - height

    def turn(self):
        self.por()
        self.x1, self.y1 = self.y1, self.x1
        self.x2, self.y2 = self.y2, self.x2
        self.por()

    def scale(self, factor):
        self.por()
        length, height = self.get_size()
        self.x1 -= (factor * length - length) / 2
        self.y1 += (factor * height - height) / 2
        self.x2 += (factor * length - length) / 2
        self.y2 -= (factor * height - height) / 2
        self.por()


rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.scale(2.0)
print(rect.get_pos(), rect.get_size(), sep='\n')

