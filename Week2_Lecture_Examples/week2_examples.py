# Examples from CS1527 - Lecture 2.2

# New object classes can be easily defined:
class Student:
    """ A class representing a student """
    def __init__(self, na , ag): #initialises objects (instances) created in the class
        self.full_name = na #self - a special parameter which refrences the object being created
        self.age = ag

    def get_age(self): #method - returns value of age attribute
        return self.age

class Car:
    all_cars = []
    """ A simple Car class example """

    """ Initialising """
    def __init__(self,ma,mo,yr):
        self.make = ma
        self.model = mo
        self.year = yr
        self.odometer_reading = 0
        Car.all_cars.append(self)
    
    @classmethod
    def print_inventory(cls):
        for item in cls.all_cars:
            print(item.get_fullname())
    
    def get_fullname(self):
        """ Return a neatly formatted descriptive name """
        long_name = str(self.year) + ' ' + self.make + \
            ' ' + self.model
        return long_name.title()

    def get_car_age(self, current_year = 2022):
        """ Return the age of the car in years """
        return current_year - self.year

    def increment_odometer(self, miles):
        self.odometer_reading += miles


#Students

john = Student('John Cleese', 78) #created Student object, held in variable john.

#print(john.full_name, john.age)

#Cars
vw_car_1 = Car('Volkswagen', 'Golf', 2019) #created Car object, held in variable car_1.
vw_car_2 = Car('Volkswagen', 'Tiguan', 2017)
au_car_1 = Car('Audi', 'RS4', 2014)
au_car_1 = Car('Audi', 'Q7', 2021)


Car.print_inventory()
