class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def __str__(self):
        return f'Rectangle: {self.x}, {self.y}, {self.width}, {self.height}'

    def get_rect_area(self):
        return self.width * self.height

rect_1 = Rect(5, 10, 50, 100)

print(str(rect_1))
print(rect_1.get_rect_area())
