from random import randrange


class Publication:
    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"Name: {self.name}"


class Book(Publication):
    def __init__(self, name, author, page_count) -> None:
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def __repr__(self) -> str:
        return (
            super().__repr__()
            + f"\nAuthor: {self.author}\nPage count: {self.page_count}"
        )


class Magazine(Publication):
    def __init__(self, name, chief_editor) -> None:
        super().__init__(name)
        self.chief_editor = chief_editor

    def __repr__(self) -> str:
        return super().__repr__() + f"\nChief editor: {self.chief_editor}"


class Car:
    registration_number: int
    maximum_speed: float
    current_speed: float = 0.0
    travelled_distance: float = 0.0

    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours
        # print(f"{self.registration_number} travelled -> {self.travelled_distance}")

    def accelerate(self, acceleration):  # in km/h
        cur_speed = self.current_speed
        if acceleration >= self.maximum_speed:
            return
        cur_speed += acceleration
        if cur_speed > self.maximum_speed:
            cur_speed = self.maximum_speed
        if cur_speed < 0:
            cur_speed = 0
        self.current_speed = cur_speed
        # print(f"Input accel: {acceleration}\nChanged speed to {cur_speed}")

    def __repr__(self) -> str:
        return f"""
Registration Number: {self.registration_number}
Maximum speed: {self.maximum_speed} km/h
Current speed: {self.current_speed} km/h
Travelled Distance: {self.travelled_distance} km"""


class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, kilowatt_hours):
        super().__init__(registration_number, maximum_speed)
        self.kilowatt_hours = float(kilowatt_hours)

    def __repr__(self) -> str:
        return super().__repr__() + f"\nCharge: {self.kilowatt_hours} kWh"


class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, liters):
        super().__init__(registration_number, maximum_speed)
        self.liters = float(liters)

    def __repr__(self) -> str:
        return super().__repr__() + f"\nGasoline: {self.liters} l"


class Race:
    def __init__(self, name, track_length, cars) -> None:
        self.name: str = name
        self.track_length: int = track_length
        self.cars: set[Car] = cars

    def hour_passes(self) -> None:
        for car in self.cars:
            car.drive(1)

    def print_status(self) -> None:
        for car in self.cars:
            print(car)

    def accelerate_cars(self):
        for car in self.cars:
            car.accelerate(randrange(-15, +15))

    def finished(self) -> bool:
        for car in self.cars:
            if car.travelled_distance >= self.track_length:
                print(f"\n\nWinner of {self.name} is {car}")
                return True
        return False
