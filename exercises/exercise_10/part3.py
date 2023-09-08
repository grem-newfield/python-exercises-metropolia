# 3. Extend the program again by adding a method `fire_alarm` that does not
# receive any parameters and moves all elevators to the bottom floor. Continue
# the main program by causing a fire alarm in your building.

from classes import Building


def part3():
    myBuilding = Building(10, 0, 4)
    myBuilding.run_elevator(0, 8)
    myBuilding.run_elevator(2, 4)
    print("We all good: ")
    print(myBuilding)
    myBuilding.fire_alarm()
    print(myBuilding)


if __name__ == "__main__":
    part3()
