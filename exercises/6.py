from random import randrange
from sys import argv

def part1():
    def dice_roll() -> int:
        return randrange(1,7)

    print("Rolling Normal Dice")

    while True:
        roll = dice_roll()
        if roll == 6: 
            print("Boom: ", roll)
            break
        print("Roll: ", roll)

def part2():
    def roll_n_sided_die(sides: int):
        if sides <= 1:
            return (2,2)
        return (randrange(1, sides+1), sides)

    print("Rolling ?D Dice")
    while True: 
        try: sides = int(input("Give side number: ").strip()); break 
        except: print("NaN"); continue
    
    while True:
        (roll, sides) = roll_n_sided_die(sides)
        if roll == sides: 
            print("Boom: ", roll)
            break
        print("Roll: ", roll)


def part3():
    def gallons_to_litres(gallons: float) -> float:
        conversion_rate = 4.54609288
        return gallons * conversion_rate

    gallons = None

    while True: 
        try: gallons = float(input("Input gallons: ").strip())
        except: print("NaN"); continue
        if gallons < 0: 
            break
        print("Converted to Litres: ", gallons_to_litres(gallons))


# 4. Write a function that gets a list of integers as a parameter. The function returns the sum of all the numbers in
# the list. For testing, write a main program where you create a list, call the function, and print out the value it
# returned.

def part4(): pass
# 5. Write a function that gets a list of integers as a parameter. The function returns a second list that is otherwise
# the same as the original list except that all uneven numbers have been removed. For testing, write a main program 
# where you create a list, call the function, and then print out both the original as well as the cut-down list.

def part5(): pass
# 6. Write a function that receives two parameters: the diameter of a round pizza in centimeters and the price of
# the pizza in euros. The function calculates and returns the unit price of the pizza per square meter. The main program
# asks the user to enter the diameter and price of two pizzas and tells the user which pizza provides better value for
# money (which of them has a lower unit price). You must use the function you wrote for calculating the unit prices. 

def part6(): pass


if __name__ == "__main__":
    choice = "all"
    try: 
        if argv[1]:
            print(argv)
            choice = str(argv[1])
    except:
        choice = str(input("Hello, what part of the 6th exercise?\n(1,2,3,4,5,6,all): "))
    match choice:
        case "1":
            part1()
        case "2":
            part2()
        case "3":
            part3()
        case "4":
            part4()
        case "5":
            part5()
        case "6":
            part6()
        case "all":
            part1()
            part2()
            part3()
            part4()
            part5()
            part6()
        case _:
            print("Wrong input?\nExiting...")
