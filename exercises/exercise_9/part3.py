from classes import Car


def part3():
    myCar = Car("XYZ-999", 142)
    print(myCar)
    myCar.accelerate(60)
    myCar.drive(1.5)
    print(myCar)


if __name__ == "__main__":
    part3()
