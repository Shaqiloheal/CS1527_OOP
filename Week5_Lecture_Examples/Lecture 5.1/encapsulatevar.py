class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return ((self.width * 2) + (self.height * 2))

r = Rectangle(3, 4)
print("area()" , r.area())
