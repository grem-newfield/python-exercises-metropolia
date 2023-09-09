# 2. Extend the previosly written `Car` class by adding two subclasses:
# `ElectricCar` and `GasolineCar`. Electric cars have the capacity of the
# battery in kilowatt-hours as their property. Gasoline cars have the volume of
# the tank in liters as their property. Write initializers for the subclasses.
# For example, the initializer of electric cars receives the registration
# number, maximum speed and battery capacity as its parameter. It calls the
# initializer of the base class to set the first two properties and then sets
# its capacity. Write a main program where you create one electric car (ABC-15,
# 180
# km/h,
# 52.5
# kWh)
# and one gasoline car (ACD-123, 165 km/h, 32.3 l). Select speeds for both
# cars, make them drive for three hours and print out the values of their
# kilometer counters.

from random import randrange
from classes import ElectricCar, GasolineCar


def part2():
    e_car = ElectricCar("ABC-15", 180, 52.5)
    gas_car = GasolineCar("ACD-123", 165, 32.3)

    e_car.current_speed = randrange(100, 200)
    gas_car.current_speed = randrange(100, 200)

    print(e_car)
    print(gas_car)

    for _ in range(3):
        e_car.accelerate(randrange(-15, 15))
        gas_car.accelerate(randrange(-15, 15))
        e_car.drive(1)
        gas_car.drive(1)
    print("\n\nRan for 3h")

    print(e_car)
    print(gas_car)


if __name__ == "__main__":
    part2()
