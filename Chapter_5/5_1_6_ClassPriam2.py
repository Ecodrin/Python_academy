class Rectangle:

    def __init__(self, coordinate_1, coordinate_2):
        x01, y01 = coordinate_1
        x02, y02 = coordinate_2
        self.x1 = round(min(x01, x02), 2)
        self.y1 = round(max(y01, y02), 2)
        self.x2 = round(max(x01, x02), 2)
        self.y2 = round(min(y01, y02), 2)

    def perimeter(self):
        return round(abs(self.x1 - self.x2) * 2 + abs(self.y1 - self.y2) * 2, 2)

    def area(self):
        return round(abs(self.x1 - self.x2) * abs(self.y1 - self.y2), 2)

    def get_pos(self):
        return tuple([round(self.x1, 2), round(self.y1, 2)])

    def get_size(self):
        return tuple([round(abs(self.x2 - self.x1), 2), round(abs(self.y1 - self.y2), 2)])

    def move(self, dx, dy):
        self.x1 += dx
        self.x2 += dx
        self.y1 += dy
        self.y2 += dy

    def resize(self, width, height):
        self.x2 = self.x1 + width
        self.y2 = self.y1 - height
