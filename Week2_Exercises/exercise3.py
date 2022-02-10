# Author: Warren Spalding
# CS1527 - Object Orientated Programming
# Week 2 - Exercise 2
# Program that defines Superclass 'Shape' into subclasses 'Rectangle' and 'Circle'.  The 'Circle' subclass has a subclass for 
# a 3 dimensional shape called "Cylinder"
import math

"""Defines parent Class Shape"""
class Shape:

    def __init__(self, co):
        self._colour = co

    def get_colour(self):
        return self._colour

"""Defines child Class Rectangle(Shape)"""
class Rectangle(Shape):

    def __init__(self, co, wi=2.0, le=3.0):
        self._width = wi
        self._length = le
        super().__init__(co)

    def get_area(self):
        """ Calculate the area of the rectangle """
        return self._width * self._length

    def get_perimeter(self):
        """ Calculates the permiter of the rectangle """
        return (self._width * 2) + (self._length * 2)

    def __str__(self):
        return "Your rectangle of width " + str(self._width) + \
            ', length ' + str(self._length) + ' & colour ' + str(self._colour)


"""Defines child Class Circle(Shape)"""
class Circle(Shape):

    def __init__(self, co, ra=1.0):
        self._radius = ra
        super().__init__(co)
        

    def get_area(self):
        """ Calculates the area of the circle """
        return math.pi * self._radius * self._radius

    def get_radius(self):
        """ Returns the radius of the circle """
        return self._radius

    def __str__(self):
        return 'Circle of radius: ' + str(self._radius) + \
            ' & colour ' + str(self._colour)

"""defines child class of Cylinder(Circle)"""
class Cylinder(Circle):

    def __init__(self, co, ra=2.5, he=5.0):
        self._height = he
        super().__init__(co, ra)

    def get_area(self):
        """ Calculate the area of the Cylinder """
        return (2 * math.pi * self._radius * self._height) + \
            (2 * super().get_area())

    def get_volume(self):
        """ Calculate the Cylinder volume """
        return (super().get_area()) * self._height

    def __str__(self):
       return 'The cylinder radius of ' + str(self._radius) + \
           ', height ' + str(self._height) + ' & colour ' + str(self._colour)

def test_shapes():
    rectangle_1 = Rectangle('green', 4.5, 2.3)
    print(rectangle_1)
    print(rectangle_1.get_area())
    print(rectangle_1.get_perimeter())
    
    circle_1 = Circle('yellow', 2.5)
    print(circle_1)
    print(circle_1.get_radius())
    print(circle_1.get_area())
    
    cylinder_1 = Cylinder('cyan', 2.5, 5)
    print(cylinder_1)
    print(cylinder_1.get_area())
    print(cylinder_1.get_volume())

test_shapes()








