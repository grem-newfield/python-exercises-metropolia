from sys import argv
from part1 import part1
from part2 import part2
from part3 import part3
from part4 import part4


def break_line():
    print("-" * 80)
    print()


choice = "all"
print(argv)
try:
    if argv[1]:
        choice = str(argv[1])
except:
    print(
        """Hint: you can pass your choice as an argument
to the script like: python 6.py 4\n"""
    )
    choice = str(input("Hello, what part of the 10th exercise?\n(1,2,3,4,all): "))
match choice:
    case "1":
        part1()
        break_line()
    case "2":
        part2()
        break_line()
    case "3":
        part3()
        break_line()
    case "4":
        part4()
        break_line()
    case "all":
        part1()
        break_line()
        part2()
        break_line()
        part3()
        break_line()
        part4()
        break_line()
    case _:
        print("Wrong input?\nExiting...")
