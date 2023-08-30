from math import pi, prod, fsum
name: str = input("What is your name: ")
print(f"Hello {name}, I see you there.")
print()
print()
try:
    circle_radius: float = float(input("Give circle radius: "))
except Exception:
    raise Exception("Input must be a number")
print("Area of circle: ", circle_radius**2 * pi, "\n\n")
try:
    length = float(input("Input rectangle length: "))
    width = float(input("Input rectangle width: "))
except Exception:
    raise Exception("Input must be a number")
print("Perimeter: ", (length + width) * 2)
print("Area: ", length * width, "\n\n")
try:
    nums = [float(n) for n in input("Input 3 numbers split by spaces: ").split(" ")]
except Exception:
    raise Exception("3 numbers split by spaces, please")
print("Sum: ", fsum(nums))
print("Product: ", prod(nums))
print("Average: ", fsum(nums) / 3.0, "\n\n")
try:
    talents, pounds, lots = [
        float(n)
        for n in input(
            """Input talents, pounds and lots,
in that order, split by spaces: """
        ).split(" ")
    ]
except Exception:
    raise Exception("Did u do something wrong?")

def to_talent(talents):
    return talents * 20.0
def to_lot(pounds):
    return pounds * 32.0
def to_grams(lots):
    return lots * 13.3

grams: float = to_grams(to_lot(to_talent(pounds) + talents) + lots )
print("Weight in modern units:")

if grams >= 1000:
    kilos = str(grams/1000).split(".")
    print(f"    {kilos[0]} kilograms and {kilos[1]} grams\n\n")
else:
    print("    %.2f grams" % grams, "\n\n")

import random
print("Random Combinations for your lock: ")
rand_3_digit = []
for i in range(3): rand_3_digit.append(random.randrange(0,9))
print("3 digit: ", rand_3_digit)
rand_4_digit = []
for i in range(4): rand_4_digit.append(random.randrange(1,6))
print("4 digit: ", rand_4_digit)