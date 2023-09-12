from random import randrange
from sys import argv
from helpers import asker, break_line


def part1():
    print("Running Part 1\n")

    def dice_roll() -> int:
        return randrange(1, 7)

    print("Rolling Normal Dice")

    while True:
        roll = dice_roll()
        if roll == 6:
            print("Boom: ", roll)
            break
        print("Roll: ", roll)

    break_line()


def part2():
    print("Running Part 2\n")

    def roll_n_sided_die(sides: int):
        if sides <= 1:
            print("Invalid amount of sides.")
            print("Defaulting to 2 sides")
            return (2, 2)
        return (randrange(1, sides + 1), sides)

    print("Rolling ?D Dice")

    sides = asker("Give side number: ", "int")

    while True:
        (roll, sides) = roll_n_sided_die(sides)
        if roll == sides:
            print("Boom: ", roll)
            break
        print("Roll: ", roll)

    break_line()


def part3():
    print("Running Part 3\n")

    def gallons_to_litres(gallons: float) -> float:
        conversion_rate = 4.54609288
        return gallons * conversion_rate

    gallons = None

    while True:
        try:
            gallons = float(input("Input gallons: ").strip())
        except KeyboardInterrupt:
            exit()
        except Exception:
            print("NaN. Negative number to exit")
            continue
        if gallons < 0:
            break
        print("Converted to Litres: ", gallons_to_litres(gallons))

    break_line()


def part4():
    print("Running Part 4\n")
    list_of_integers = [1, 2, 3, 4]
    expected_sum = 10

    def my_sum_function(int_list):
        return sum(int_list)

    print("Testing a function")
    assert my_sum_function(list_of_integers) == expected_sum

    print("Expected Sum: ", expected_sum)
    print("Sum: ", sum(list_of_integers))

    break_line()


def part5():
    print("Running Part 5\n")

    number_list = [1, 2, 3, 4, 5, 6, 7, 8]
    expected_list = [2, 4, 6, 8]

    def is_even(n):
        return n % 2 == 0

    def remove_uneven_numbers(some_list):
        out_list = []
        for n in some_list:
            if is_even(n):
                out_list.append(n)
        return out_list

    assert remove_uneven_numbers(number_list) == expected_list

    print("Testing my function.")
    print("Expected list: ", expected_list)
    print("Function list: ", remove_uneven_numbers(number_list))

    break_line()


def part6():
    from math import pi

    print("Running Part 6\n")
    # diameter of pizza : cm
    # price : €
    # calculate : €/m

    def calculate_price(pizza_diameter, pizza_price):
        area = pi * ((pizza_diameter / 2) ** 2)
        return pizza_price / area  # €/m

    pizza_1_price = asker("Pizza 1 diameter: (cm) ", "float")
    pizza_1_diameter = asker("Pizza 1 price: ", "float")
    pizza_2_price = asker("Pizza 2 diameter: (cm) ", "float")
    pizza_2_diameter = asker("Pizza 2 price: ", "float")

    assert pizza_1_diameter != 0, "\nPizza 1 diameter is 0. You got no pizza."
    assert pizza_2_diameter != 0, "\nPizza 2 diameter is 0. You got no pizza."

    price_1 = calculate_price(pizza_1_diameter, pizza_1_price)
    price_2 = calculate_price(pizza_2_diameter, pizza_2_price)

    print()
    print(
        f"""Pizza 1
    Size: {pizza_1_diameter}
    Price: {pizza_1_price}
    {price_1:.3} €/m\n"""
    )
    print(
        f"""Pizza 2
    Size: {pizza_2_diameter}
    Price: {pizza_2_price}
    {price_2:.3} €/m\n"""
    )
    if price_1 == 0.0 or price_2 == 0.0:
        print(f"Pizza {'1' if price_1 < price_2 else '2' } is FREE")
    else:
        print(f"Pizza {'1' if price_1 < price_2 else '2' } is more value")

    break_line()


if __name__ == "__main__":
    choice = "all"
    try:
        if argv[1]:
            choice = str(argv[1])
    except Exception:
        print(
            """Hint: you can pass your choice as an argument
      to the script like: python 6.py 4\n"""
        )
        choice = str(
            input("Hello, what part of the 6th exercise?\n(1,2,3,4,5,6,all): ")
        )
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
