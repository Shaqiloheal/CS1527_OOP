# Author: Warren Spalding
# CS1527 - Object Orientated Programming
# Week 2 - Exercise 3c
# Changes to the Cylinder class which creates an instance of Circle as 
# the base of the cylinder.
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

class Shape:
    """Defines parent Class Shape with additional Point class to represent its centre"""

    def __init__(self, x, y, co):
        self._colour = co
        self._centrepoint = Point(x, y)

    def get_colour(self):
        return self._colour

class Rectangle(Shape):
    """Defines child Class Rectangle(Shape)"""

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

class Circle(Shape):
    """defines child class of Cylinder(Circle)"""

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

class Cylinder(Shape):
    """defines child class of Cylinder(Shape)"""

    def __init__(self, x, y, co, ra=2.5, he=5.0):
        self._height = he
        """ Creates instance of Circle as the base of the cylinder """
        self._base = Circle(x, y, co, ra)

    def get_area(self):
        """ Calculate the area of the Cylinder """
        """ Call to _base get_area() method """
        return (2 * math.pi * self._base._radius * self._height) + \
            (2 * self._base.get_area())

    def get_volume(self):
        """ Calculate the Cylinder volume """
        """ Note call to _base get_area() method"""
        return self._base.get_area() * self._height

    def __str__(self):
       return 'The cylinder radius of ' + str(self._radius) + \
           ', height ' + str(self._height) + ' & colour ' + str(self._colour) + \
               ' @ ' + str(self._centrepoint)

def test_shapes():
    
    cylinder_1 = Cylinder(1.0, 1.0, 'cyan', 2.5, 5)
    print(cylinder_1._base._centrepoint.dist_from_origin())

# test_shapes() altered as Cylinder class is no longer using inheritance
# due to centrepoint.dist_from_origin() no longer working. As class Cylinder
# is using its _base attribute (Circle):    

if __name__ == "__main__": 
    
    test_shapes()