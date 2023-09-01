
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


#  3. Write a program that asks the user for an integer and tells if the number
#  is a prime number. Prime numbers are
#  number that are only divisible by one or the number itself.
#    • For example, 13 is a prime number as it can only be divided by 1 or 13
#    so that the result is an integer.
#    • On the other hand, 21 is not a prime number as it is divisible by 3 and
#    7.


def part3():
    number = 0
    try:
        number = int(input("Throw me some number (int): ").strip())
    except:
        print("Input an integer."); return

    def is_prime(n: int) -> bool:
    # number that are only divisible by one or the number itself.
        if n % n == 0 and n % 2 != 0:
            return True
        else:
            return False


    



#  4. Write a program that asks the user to enter the names of five cities one
#  by on (use a  for  loop for reading the names)
#  and stores them into a list structure. Finally, the program prints out the
#  names of the cities one by one, one city per line,
#  in the same order they were read as input. Use a  for  loop for asking the
#  names and a  for/in  loop to iterate through the
#  list.


def part4():
    print("TODO")


if __name__ == "__main__":
    choice = str(input("Hello, what part of the 5rd exercise?\n(1,2,3,4,all): "))
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
