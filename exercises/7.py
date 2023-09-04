# ## 7. Tuple, set, and dictionary
from sys import argv


def break_line():
    print(
        "--------------------------------------------------------------------------------"
    )
    print()


# 1. Write a program that asks the user for a number of a month and then prints
# out the corresponding season (`spring`, `summer`, `autumn`, `winter`). Save
# the seasons as strings into a tuple in your program. We can define each
# season to last three months, December being the first month of winter.


def part1():
    print("Running Part 1\n")
    seasons = ("winter","spring", "summer", "autumn")
    month = None
    while True:
        try:
            month = int(input("Choose a month: (int) ").strip())
            if month not in range(1, 12 + 1):
                print("That is not a month number.")
                continue
            break
        except KeyboardInterrupt:
            exit()
        except:
            print("NaN. Number of month required.")
            continue

    print("It is in",seasons[month // 3])

    break_line()


# 2. Write a program that asks the user to enter names until he/she enters an
# empty string. After each name is read the program either prints out `New
# name` or `Existing name` depending on whether the name was entered for the
# first time. Finally, the program lists out the input names one by one, one
# below another in any order. Use the set data structure to store the names.


def part2():
    print("Running Part 2\n")

    break_line()


# 3. Write a program for fetching and storing airport data. The program asks
# the user if they want to enter a new airport, fetch the information of an
# existing airport or quit. If the user chooses to enter a new airport, the
# program asks the user to enter the ICAO code and name of the airport. If the
# user chooses to fetch airport information instead, the program asks for the
# ICAO code of the airport and prints out the corresponding name. If the user
# chooses to quit, the program execution ends. The user can choose a new option
# as many times they want until they choose to quit. (The ICAO code is an
# identifier that is
# unique to each airport.
# For example, the ICAO
# code of Helsinki-Vantaa
# Airport is EFHK. You
# can easily find the
# ICAO codes of different
# airports online.)
def part3():
    print("Running Part 3\n")

    break_line()


if __name__ == "__main__":
    choice = "all"
    try:
        if argv[1]:
            choice = str(argv[1])
    except:
        print(
            """Hint: you can pass your choice as an argument 
      to the script like: python 6.py 4\n"""
        )
        choice = str(input("Hello, what part of the 6th exercise?\n(1,2,3,all): "))
    match choice:
        case "1":
            part1()
        case "2":
            part2()
        case "3":
            part3()
        case "all":
            part1()
            part2()
            part3()
        case _:
            print("Wrong input?\nExiting...")
