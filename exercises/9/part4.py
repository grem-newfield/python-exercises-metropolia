from car import Car
from random import randrange


def part4():
    cars = []
    for i in range(10):
        cars.append(Car(f"ABC-{i+1}", randrange(100, 200)))
    print(cars)
    race_on = True
    while race_on:
        for car in cars:
            car.accelerate(randrange(-10, +15))
            car.drive(1)
            if car.travelled_distance >= 10_000.0:
                race_on = False

    print(cars)


if __name__ == "__main__":
    part4()


def __call__():
    part4()
