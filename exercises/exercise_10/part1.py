# 1. Write an `Elevator` class that receives the numbers of the bottom and top
# floors as initializer parameters. The elevator has methods `go_to_floor`,
# `floor_up` and `floor_down`. A new elevator is always at the bottom floor. If
# you make elevator `h` for example the method call `h.go_to_floor(5)`, the
# method calls either the `floor_up` or `floor_down` methods as many times as
# it needs to get to the fifth floor. The methods run the elevator one floor up
# or down and tell what floor the elevator is after each move. Test the class
# by creating an elevator in the main program, tell it to move to a floor of
# your choice and then back to the bottom floor.

from classes import Elevator


def part1():
    # tests
    el = Elevator(0)
    el.go_to_floor(5)
    el.floor_down()
    el.floor_up()
    el.go_to_floor(2)
    el.go_to_floor(50)
    print(el)
    assert el.floor == 50


if __name__ == "__main__":
    part1()
