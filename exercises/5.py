from helpers import break_line


def part1():
    from random import randrange

    def roll_dice():
        return randrange(1, 6)

    how_many_to_roll = int(input("How many dice to roll? : "))

    dice = []

    for i in range(how_many_to_roll):
        roll = roll_dice()
        dice.append(roll)
        print(f"Rolled dice {i+1}: {roll}")

    print(f"\nDice sum: {sum(dice)}")
    break_line()


def part2():
    numbers = []
    while True:
        number = input("Give me numbers, if you want to stop, anything else? : ")
        try:
            numbers.append(float(number))
        except Exception:
            break
        print(numbers)
    numbers.sort()
    if len(numbers) <= 0:
        print("\n\n")
        return
    print("\nHere are the greatest numbers:", end="")
    for _ in range(5):
        try:
            print(" ", numbers.pop(), end="")
        except Exception:
            break
    print()
    break_line()


def part3():
    number = 0
    try:
        number = int(input("Throw me some number (int): ").strip())
    except Exception:
        print("Input an integer.")
        return

    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(n**0.5) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    if is_prime(number):
        print("Number is prime")
    else:
        print("Number is not a prime")

    break_line()


def part4():
    cities = []
    print("Give me 5 cities.")
    for _ in range(5):
        cities.append(input("Enter a city name: "))
    print("\nHere they are:")
    for i in range(5):
        print(f"{cities[i]}")

    break_line()


if __name__ == "__main__":
    choice = str(input("Hello, what part of the 5th exercise?\n(1,2,3,4,all): "))
    match choice:
        case "1":
            part1()
        case "2":
            part2()
        case "3":
            part3()
        case "4":
            part4()
        case "all":
            part1()
            part2()
            part3()
            part4()
        case _:
            print("Wrong input?\nExiting...")
