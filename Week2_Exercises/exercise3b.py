# Author: Warren Spalding
# CS1527 - Object Orientated Programming
# Week 2 - Exercise 3b
# Introduces a Point class and the introduction into the class
# Includes other changes to various __init__() methods.
import math

class Point:
    """Creates a new Point, using x & y coordinates"""

    def __init__(self, x=0.0, y=0.0):
        """Create new Point, at x & y"""
        self._x = x
        self._y = y

    def get_xcoordinate(self):
        return self._x

    def get_ycoordinate(self):
        return self._y

    def dist_from_origin(self):
        """Calculates point from the origin"""
        return ((self._x ** 2) + (self._y ** 2)) ** 0.5

    def __str__(self):
        return "({0}, {1})".format(self._x, self._y)


"""Defines parent Class Shape with additional Point class to represent its centre"""
class Shape:

    def __init__(self, x, y, co):
        self._colour = co
        self._centrepoint = Point(x, y)

    def get_colour(self):
        return self._colour

"""Defines child Class Rectangle(Shape)"""
class Rectangle(Shape):

    def __init__(self, x, y, co, wi=2.0, le=3.0):
        self._width = wi
        self._length = le
        super().__init__(x, y, co)

    def get_area(self):
        """ Calculate the area of the rectangle """
        return self._width * self._length

    def get_perimeter(self):
        """ Calculates the permiter of the rectangle """
        return (self._width * 2) + (self._length * 2)

    def __str__(self):
        return "Your rectangle of width " + str(self._width) + \
            ', length ' + str(self._length) + ' & colour ' + str(self._colour) + \
                ' @ ' + str(self._centrepoint)


"""Defines child Class Circle(Shape)"""
class Circle(Shape):

    def __init__(self, x, y, co, ra=1.0):
        self._radius = ra
        super().__init__(x, y, co)
        
    def get_area(self):
        """ Calculates the area of the circle """
        return math.pi * self._radius * self._radius

    def get_radius(self):
        """ Returns the radius of the circle """
        return self._radius

    def __str__(self):
        return 'Circle of radius: ' + str(self._radius) + \
            ' & colour ' + str(self._colour) + ' @ ' + \
                str(self._centrepoint)

"""defines child class of Cylinder(Circle)"""
class Cylinder(Circle):

    def __init__(self, x, y, co, ra=2.5, he=5.0):
        self._height = he
        super().__init__(x, y, co, ra)

    def get_area(self):
        """ Calculate the area of the Cylinder """
        return (2 * math.pi * self._radius * self._height) + \
            (2 * super().get_area())

    def get_volume(self):
        """ Calculate the Cylinder volume """
        return (super().get_area()) * self._height

    def __str__(self):
       return 'The cylinder radius of ' + str(self._radius) + \
           ', height ' + str(self._height) + ' & colour ' + str(self._colour) + \
               ' @ ' + str(self._centrepoint)

def test_shapes():
    rectangle_1 = Rectangle(0.0, 0.0, 'green', 4.5, 2.3)
    print(rectangle_1)
    print(rectangle_1.get_area())
    print(rectangle_1.get_perimeter())
    print(rectangle_1._centrepoint.dist_from_origin())
    
    circle_1 = Circle(2.5, 4.0, 'yellow', 2.5)
    print(circle_1)
    print(circle_1.get_radius())
    print(circle_1.get_area())
    print(circle_1._centrepoint.dist_from_origin())
    
    cylinder_1 = Cylinder(1.0, 1.0, 'cyan', 2.5, 5)
    print(cylinder_1)
    print(cylinder_1.get_area())
    print(cylinder_1.get_volume())
    print(cylinder_1._centrepoint.dist_from_origin())

if __name__ == "__main__": test_shapes()