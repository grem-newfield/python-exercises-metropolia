from car import Car


def part2():
    myCar = Car("SDJ-320", 142)
    print(myCar)
    myCar.accelerate(30)
    print(myCar)
    myCar.accelerate(70)
    print(myCar)
    myCar.accelerate(50)
    print(myCar)
    myCar.accelerate(-200)
    print(myCar)


if __name__ == "__main__":
    part2()
