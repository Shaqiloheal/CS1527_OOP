class Car:
    all_cars = []

    def __init__(self, ma, mo, yr):
        self.make = ma
        self.model = mo
        self.year =yr
        self.odometer_reading = (0) # setting defualt value not passed through initializer.
        Car.all_cars.append(self)

    def get_fullname(self):
        """Return a neatly formatted descriptive name."""
        long_name = self.make + ' ' + self.model
        return long_name.title()

    def get_car_age(self, current_year=2022):
        """Return the age of the car in years."""
        if self.year == current_year:
            return 'Current year model.'
        else:
            return current_year - self.year

    @classmethod
    def print_inventory(cls):
        for item in cls.all_cars:
            print(item.get_fullname())



# Driver code
if __name__ == '__main__':

    my_car1 = Car('Audi', 'Q7', 2020)
    my_car2 = Car('Skoda', 'Karoq', 2022)
    my_car3 = Car('Volkswagen', 'Golf', 2019)
    my_car4 = Car('Volkswagen', 'Golf', 2019)

    #print(my_car1.get_fullname())
    #print(my_car1.get_car_age(),'\n')

    my_car1.all_cars = 'NONE'
    
    #print(Car.all_cars)
    #print(my_car1.__class__.all_cars)
    #print(my_car1.all_cars)          # NONE

    Car.print_inventory() #Prints the whole inventory


    


    
