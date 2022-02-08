# Examples from CS1527 - Lecture 2.2 - 2.6

class Car:
    """ A simple Car class example """
    __doc__ = 'Luxury Car Class'

    """ Class attribute to hold list of Cars created """
    all_cars = []
    

    """ Initialising """
    def __init__(self,ma,mo,yr):
        self._make = ma
        self._model = mo
        self._year = yr
        """_odometer_reading should only be
        accessed/modified via internal methods"""
        self.__odometer_reading = 0
        Car.all_cars.append(self)

    @classmethod
    def print_inventory(cls):
        for item in cls.all_cars:
            print(item.get_fullname())

    def __str__(self):
        return 'Car: ' + self._make + ' ' + self._model

    def __len__(self):
        return self.get_car_age()

    def __eq__(self, other):
        return (self._make == other._make and self._model == other._model)

    def get_fullname(self):
        """ Return a neatly formatted descriptive name """
        long_name = str(self._year) + ' ' + self._make + \
            ' ' + self._model
        return long_name.title()

    def get_car_age(self, current_year = 2022):
        """ Return the age of the car in years """
        return current_year - self._year

    def increment_odometer(self, miles):
        self.__odometer_reading += miles


#Cars
vw_car_1 = Car('Volkswagen', 'Golf', 2019) #created Car object, held in variable car_1.
vw_car_2 = Car('Volkswagen', 'Tiguan', 2017)
au_car_1 = Car('Audi', 'RS4', 2014)
au_car_1 = Car('Audi', 'Q7', 2021)


Car.print_inventory()
print(vw_car_1)
#print(getattr(vw_car_1, '_make'))
#print(getattr(vw_car_1,'get_fullname'))
#print(getattr(vw_car_1,'get_fullname')())
#print(hasattr(vw_car_1,'engine_size'))

