class Car:
    """Car class"""
    def __init__(self, na, mk, ag=0, mi=0):
        """Car class initializer."""
        self.car_name = na
        self.car_model = mk
        self.car_age = ag
        self.car_milage = mi

    def get_car_name(self):
        return self.car_name

    def get_car_model(self):
        return self.car_model

    def get_car_age(self):
        return self.car_age

    def get_car_milage(self):
        return self.car_milage

# Driver code
if __name__ == '__main__':

    # Object Code
    # variable = class(name, model, year, milage)
    car1 = Car('Ford', 'Fiesta', 2012, 36000)
    car2 = Car('Toyota', 'Celica', 2008, 108000)
    car3 = Car('Ferrari', 'Enzo', 2005, 20000)
    car4 = Car('BMW', '318i', 2020, 12000)
    car5 = Car('Volkswagen', 'Tiguan', 2022, 20)

# Displays inventory.
print('\nCurrent inventory available:')
print('------------------------------\n')

print('Car Make:', car1.get_car_name(), car1.get_car_model())
print('Year:', car1.get_car_age())
print('Milage:', car1.get_car_milage(),'\n')

print('Car Make:', car2.get_car_name(), car2.get_car_model())
print('Year:', car2.get_car_age())
print('Milage:', car2.get_car_milage(),'\n')

print('Car Make:', car3.get_car_name(), car3.get_car_model())
print('Year:', car3.get_car_age())
print('Milage:', car3.get_car_milage(),'\n')

print('Car Make:', car4.get_car_name(), car4.get_car_model())
print('Year:', car4.get_car_age())
print('Milage:', car4.get_car_milage(),'\n')

print('Car Make:', car5.get_car_name(), car5.get_car_model())
print('Year:', car5.get_car_age())
print('Milage:', car5.get_car_milage(),'\n')