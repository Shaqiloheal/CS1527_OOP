class Boat:
    __doc__ = 'Simple Boat Class'

    """Represent boat characteristics."""

    def __init__(self, dis, blst, **kwargs):
        super().__init__(**kwargs)
        self._displacement = dis
        self._ballast = blst

    def __str__(self):
        return 'Boat: ' + self.get_fullname()

    def get_fullname(self):
        """Return an aquatic descriptive name."""
        long_name = "~~ " + str(self._displacement) + ", " + str(self._ballast) + " ~~"
        return long_name.title()

    def clean_hull(self):
        """Simple method on boat class that print a message."""
        print('Stripping barnacles...')


class Car:
    __doc__ = 'Luxury Car Class'

    """Class attribute to hold list of Cars created."""
    all_cars = []

    def __init__(self, ma, mo, yr, **kwargs):
        self._make = ma
        self._model = mo
        self._year =yr
        """_odometer_reading shoild only be
        accessed/modified via internal methods"""
        self.__odometer_reading = (0) # setting defualt value not passed through initializer.
        Car.all_cars.append(self)

    @classmethod
    def print_inventory(cls):
        for item in cls.all_cars:
            print(item.get_fullname())

    def __str__(self):
        return 'Car: ' + self.get_fullname()

    def __len__(self):
        return self.get_car_age()

    def __eq__(self, other):
        return (self._make == other._make and self._model == other._model)

    def get_fullname(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self._year) + ', ' + self._make + \
            ' ' + self._model
        return long_name.title()

    def get_car_age(self, current_year=2022):
        """Return the age of the car in years."""
        if self._year == current_year:
            return 'Current year model.'
        else:
            return current_year - self._year

    def increment_odometer(self, miles):
        self.__odometer_reading += miles


class AmphibiousVehicle(Car, Boat):
    __doc__ = 'Amphibious Vehicle Class'

    """Represent amphibious vehicle - using multiple inheritance."""

    def __init__(self, fp, **kwargs):
        """Initialize attributes of the parent classes."""
        super().__init__(**kwargs)
        """Initialize attributes specific to an amphibious vehicle."""
        self._snorkle = True
        self._folding_prop = fp

    def get_fullname(self):    # Uses inheritance of Superclass for cleaner code.
        """Return a amphibious descriptive name."""
        long_name = "~~ " + super().get_fullname() + " ~~"
        return long_name.title()

    def convert(self):
        """Convert the vehicle for travel in water."""
        if self._folding_prop:
            print('Waiting for propeller...')
        print('Preparing to sail...')

    def __str__(self):
        return str(self._snorkle)

    # No str() or get_fullname() defined here
    # Can we call print(<object>) on an AmphibiousVehicle instance?


class ElectricCar(Car): # Subclass of Superclass (Car)
    """Represents aspects specific to electric vehicles"""
    
    def __init__(self, ma, mo, yr, batt):
        """Initialize attributes of the parent class (Car)"""
        super().__init__(ma, mo, yr,) # Call to superclass __init__()
        
        """Initialize attributes specific to an electric car."""
        self.battery_size = Battery(batt)
        self._max_range = 300  # new attribute, specific to ElectricCar
        self.__battery_level = 100


    """Method overiding without using inheritance of the Superclass called method."""
    # def get_fullname(self):  # Overides get_fullname() method for ElectricCar 
    #     """Return a high voltage descriptive name."""
    #     long_name = "** " + str(self._year) + ", " + self._make + \
    #         " " + self._model + " **"
    #     return long_name.title()

    def get_fullname(self):    # Uses inheritance of Superclass for cleaner code.
        """Return a high voltage descriptive name."""
        long_name = "** " + super().get_fullname() + " **"
        return long_name.title()

    def report_battery(self):
        """Report private attribute holding battery level."""
        print(self.__battery_level)

    def charge_battery(self):
        """Increase __battery_level as charging"""
        if self.__battery_level < 100:
            self.__battery_level += 1
        else:
            print('Danger - overcharging!')

class Battery():
    """A simple battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        return "This car has a " + str(self.battery_size) + \
            "kWh battery."


# Driver code
if __name__ == '__main__':

    """Objects"""
    my_car1 = Car('Audi', 'Q7', 2020)
    my_car2 = Car('Skoda', 'Karoq', 2022)
    my_car3 = Car('Volkswagen', 'Golf', 2019)
    my_car4 = Car('Volkswagen', 'Golf', 2016)
    el_car1 = ElectricCar('Tesla', 'Model S', 2021, 85)
    el_car2 = ElectricCar('Volkswagen', 'E-Golf', 2020 , 90)
    boat1 = Boat(dis=200,blst=True)
    amph1 = AmphibiousVehicle(ma='Volkswagen',mo='Schwimmwagen',yr=1944,fp=True,dis=900,blst=True)


    #print(my_car1.get_fullname())
    #print(my_car1.get_car_age(),'\n')

    #my_car1.all_cars = 'NONE'
    
    #print(Car.all_cars)
    #print(my_car1.__class__.all_cars)
    #print(my_car1.all_cars)          # NONE

    #print(el_car1.get_fullname())

    #print(boat1)
    #print(amph1)
    #print(amph1.clean_hull())
    #print(boat1.clean_hull())
    #print(AmphibiousVehicle.mro())  # Mehod Resolution Order
    #print(Car.mro())
    #print(ElectricCar.mro())

    #print(el_car1)
    #print(el_car1.battery_size.describe_battery())
    
    """Prints the whole inventory"""
    Car.print_inventory()

    """Prints the odometer reading using name mangling"""
    #print(my_car1._make)
    #print(my_car1.__odometer_reading) # AttributeError: 'Car' object has no attribute
    #print(my_car1._Car__odometer_reading) # type: ignore # Unmangled with prefix _<classname> ('0')

    """Accessing Unknown Members"""
    #print(getattr(my_car1, '_make'))
    #print(getattr(my_car1,'get_fullname')) # Not this!
    # <bound method Car.get_fullname of <__main__.Car object at 0x0000018EAB634E20>>
    #print(getattr(my_car1,'get_fullname')())
    #print(hasattr(my_car1,'engine_size')) # False
    
    """__str__ method to turn an instance of the class into an 'informal'
    nicely printable string representation."""
    #print(my_car1) # Car: 2020, Audi Q7
    #print(el_car1) # Car: ** 2021, Tesla Model S **

    """Additional function calls"""
    #print(el_car1._max_range) # 300
    #print(my_car1._max_range) # AttributeError: 'Car' Object has no attribute '_max_range'
    #print(el_car1.report_battery())

"""Special Data Items"""
# __doc__ : The class's documentation string or None if undefined.
# __name__ : The class name.
# __dict__ : Dictionary containing the class's namespace.
# __module__ : Module name in which the class was defined.

"""Special Methods"""
# __init__() : The initializer for the class.
# __repr__() : Define how to compute the "offical" string representation of an object.
# Should be a valid Python expression that could recreate the object.
# __str__() : method to turn an instance of the class into an 'informal'
# nicely printable string representation.
# __len__() : Define how len(obj) works.
# __eq__() : Define how == behaves for objects.
    
