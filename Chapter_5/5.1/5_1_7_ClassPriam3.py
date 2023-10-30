class Rectangle:

    def __init__(self, coordinate_1, coordinate_2):
        self.x1, self.y1 = coordinate_1
        self.x2, self.y2 = coordinate_2
        self.por()

    def por(self):
        print(self.x1, self.y1, self.x2, self.y2)
        self.x1, self.y1, self.x2, self.y2 = (min(self.x1, self.x2), max(self.y1, self.y2),
                                              max(self.x1, self.x2), min(self.y1, self.y2))

    def perimeter(self):
        return round(abs(self.x1 - self.x2) * 2 + abs(self.y1 - self.y2) * 2, 2)

    def area(self):
        return round(abs(self.x1 - self.x2) * abs(self.y1 - self.y2), 2)

    def get_pos(self):
        self.por()
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
        wight, height = self.get_size()
        x_centre = self.x1 + wight / 2
        y_centre = self.y1 - height / 2
        t = self.x1
        self.x1 = x_centre - (self.y1 - y_centre)
        self.y1 = y_centre + (t - x_centre)
        self.x2 = self.x1 + height
        self.y2 = self.y1 + wight
        self.por()

    def scale(self, factor):
        self.por()
        wight, height = self.get_size()
        self.x1 = self.x1 - (factor * wight - wight) / 2
        self.y1 = self.y1 + (factor * height - height) / 2
        self.x2 = wight * factor + self.x1
        self.y2 = self.y1 - height * factor
        '''x_centre = self.x1 + wight / 2
        y_centre = self.y1 - height / 2
        increase_x = (x_centre - self.x1) * factor
        increase_y = (self.y1 - y_centre) * factor
        self.x1 = x_centre - increase_x
        self.y1 = y_centre + increase_y
        self.x2 = x_centre + increase_x
        self.y2 = y_centre - increase_y'''
        self.por()


rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.turn()
print(rect.get_pos(), rect.get_size(), sep='\n')
print('----')

rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.scale(2.0)
print(rect.get_pos(), rect.get_size(), sep='\n')
