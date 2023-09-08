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


# tests
test_car = Car("test", 142)
test_car.accelerate(60)
test_car.drive(1.5)
assert test_car.travelled_distance == 90
