## 13. Setting up a backend service with an interface
from sys import argv
from part1 import part1
from part2 import part2


def break_line():
    print("-" * 80)
    print()


choice = "all"
try:
    if argv[1]:
        choice = str(argv[1])
except Exception:
    print(
        """Hint: you can pass your choice as an argument
to the script like: python 6.py 4\n"""
    )
    choice = str(input("Hello, what part of the 13th exercise?\n(1,2,all): "))

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
