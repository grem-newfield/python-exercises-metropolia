# 2. Extend the previous program by creating a `Building` class. The
# initializer parameters for the class are the numbers of the bottom and
# top floors and the number of elevators in the building. When a
# building is created, the building creates the required number of
# elevators. The list of elevators is stored as a property of the
# building. Write a method called `run_elevator` that accepts the number
# of the elevator and the destination floor as its parameters. In the

# main program, write the statements for creating a new building and
# running the elevators of the building.


from classes import Building


def part2():
    myBuilding = Building(10, 0, 4)
    print("New building with 10 floors, and 2 elevators: ", myBuilding)
    myBuilding.run_elevator(0, 8)
    myBuilding.run_elevator(2, 4)
    print("After running run_elevator method: ", myBuilding)


if __name__ == "__main__":
    part2()
