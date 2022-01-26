class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def circumference(self):
        return 2 * (self.x + self.y)

r1 = Rectangle(10, 30)
print(r1.area())
print(r1.circumference())