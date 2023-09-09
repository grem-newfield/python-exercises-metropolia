from sys import argv
from part1 import part1
from part2 import part2


def break_line():
    print(
        "--------------------------------------------------------------------------------"
    )
    print()


choice = "all"
print(argv)
try:
    if argv[1]:
        choice = str(argv[1])
except:
    print(
        """Hint: you can pass your choice as an argument
to the script like: python exercise.py 1
or even a folder: python exr_folder 1\n"""
    )
    choice = str(input("Hello, what part of the 11th exercise?\n(1,2,all): "))
match choice:
    case "1":
        part1()
        break_line()
    case "2":
        part2()
        break_line()
    case "all":
        part1()
        break_line()
        part2()
        break_line()
    case _:
        print("Wrong input?\nExiting...")
