from random import randrange


class Elevator:
    def __init__(self, floor):
        self.floor = floor

    def go_to_floor(self, floor):
        # target = floor - self.floor
        if self.floor == floor:
            return
        if self.floor > floor:
            for _ in range(floor):
                self.floor_down()
        else:
            for _ in range(floor):
                self.floor_up()

        self.floor = floor

    def floor_up(self):
        self.floor += 1

    def floor_down(self):
        self.floor += -1

    def __repr__(self) -> str:
        return f""" 
Current floor: {self.floor}
"""


class Building:
    def __init__(self, top_floor, bottom_floor, how_many_elevators):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        elevators = []
        for i in range(how_many_elevators):
            elevators.append(Elevator(bottom_floor))
        self.elevators = elevators

    def run_elevator(self, elevator_number, destination_floor):
        assert (
            destination_floor <= self.top_floor
        ), "destination floor bigger than possible"
        assert (
            destination_floor >= self.bottom_floor
        ), "destination floor bigger than possible"
        self.elevators[elevator_number].go_to_floor(destination_floor)

    def __repr__(self) -> str:
        elevator_floors = []
        for e in self.elevators:
            elevator_floors.append(e.floor)
        return f"""
Building has {len(self.elevators)} elevators.
Positions of elevators: {elevator_floors}
    """

    def fire_alarm(self):
        print("Bruh, we burnin!")
        print("Sending all elevators to bottom floor!")
        for e in self.elevators:
            e.floor = self.bottom_floor


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
Travelled Distance: {self.travelled_distance} km
"""


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
