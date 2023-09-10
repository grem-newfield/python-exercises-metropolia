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
