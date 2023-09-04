# ## 7. Tuple, set, and dictionary
from math import prod
from sys import argv


def break_line():
    print(
        "--------------------------------------------------------------------------------"
    )
    print()


def part1():
    print("Running Part 1\n")
    seasons = ("winter", "spring", "summer", "autumn")
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

    print("It is in", seasons[month // 3])

    break_line()


def part2():
    print("Running Part 2\n")

    names = set()

    while True:
        try:
            name = input("Give me names! : ")
            if name == " ":
                break
            if name in names:
                print("Existing name.")
                continue
            names.add(name)
            print("New name.")
        except KeyboardInterrupt:
            exit()
        except:
            print("? ? ?")
            continue

    for name in names:
        print(name)

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

    # new airport
    # fetch info of airport
    # quit

    airports = dict()

    while True:
        try:
            user_input = input("(A)dd new airport, (F)etch info, (Q)uit: ")
            match user_input:
                case "a" | "A":
                    while True:
                        try:
                            print("\nAdding new airport")
                            airport_icao = input("ICAO code: ").upper()
                            if len(airport_icao) > 4 or len(airport_icao) < 3:
                                print("Error. Invalid ICAO format")
                                continue
                            airport_name = input("Airport name: ")
                            airports[airport_icao] = airport_name
                            print(f"\nAdded {airport_name}:{airport_icao}\n")
                            break
                        except KeyboardInterrupt:
                            exit()
                        except:
                            print("Error. Invalid Input")
                            continue
                case "f" | "F":
                    while True:
                        try:
                            print("\nEnter the airports ICAO code")
                            airport_icao = input("> ").upper()
                            if len(airport_icao) > 4 or len(airport_icao) < 3:
                                print("Error. Invalid ICAO format")
                                continue
                            airport_name = airports[airport_icao]
                            print(f"Full airport name: {airport_name}\n")
                            break
                        except KeyboardInterrupt:
                            exit()
                        except:
                            print("Error. Unknown ICAO")
                            print("Airports in memory:")
                            print(airports.keys())
                            continue
                case "q" | "Q":
                    break
                case _:
                    continue
        except KeyboardInterrupt:
            exit()
        except:
            continue

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
