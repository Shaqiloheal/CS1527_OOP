# Examples from CS1527 - Lecture 2.2 - 2.6

class Car:
    """ A simple Car class example """
    all_cars = []
    

    """ Initialising """
    def __init__(self,ma,mo,yr):
        self.make = ma
        self.model = mo
        self.year = yr
        """_odometer_reading should only be
        accessed/modified via internal methods"""
        self._odometer_reading = 0
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


#Cars
vw_car_1 = Car('Volkswagen', 'Golf', 2019) #created Car object, held in variable car_1.
vw_car_2 = Car('Volkswagen', 'Tiguan', 2017)
au_car_1 = Car('Audi', 'RS4', 2014)
au_car_1 = Car('Audi', 'Q7', 2021)


Car.print_inventory()
