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

    print(f"\nDice sum: {sum(dice)}\n\n")


def part2():
    numbers = []
    while True:
        number = input("Give me numbers, if you want to stop, anything else? : ")
        try:
            numbers.append(float(number))
        except:
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
        except:
            break
    print("\n\n")


def part3():
    number = 0
    try:
        number = int(input("Throw me some number (int): ").strip())
    except:
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

    assert is_prime(13) == True
    assert is_prime(3) == True
    assert is_prime(2) == True
    assert is_prime(73) == True
    assert is_prime(179) == True
    assert is_prime(283) == True
    assert is_prime(569) == True
    assert is_prime(5) == True
    assert is_prime(21) == False
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(564) == False

    if is_prime(number):
        print("Number is prime")
    else:
        print("Number is not a prime")


def part4():
    cities = []
    print("Give me 5 cities.")
    for _ in range(5):
        cities.append(input("Enter a city name: "))
    print("\nHere they are:")
    for i in range(5):
        print(f"{cities[i]}")


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
