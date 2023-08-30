def part1():
    fish_length_limit = 42.0
    fish_length = float(input("What is the fish length in cm? Type: "))
    if fish_length < fish_length_limit:
        print(
            f"Yo, release that one, it's too small. {fish_length_limit - fish_length} cm smaller than the allowed size."
        )
    else:
        print("Nice haul")


def part2():
    cabin_class = str(input("\n\nEnter your cabin class: "))

    # under the hood "match" is an "if/elif/else"
    match cabin_class:
        case "LUX":
            print("Cabin Class LUX!\nupper-deck cabin with a balcony.")
        case "A":
            print("Cabin Class A!\nabove the car deck, equipped with a window.")
        case "B":
            print("Cabin Class B!\nwindowless cabin above the car deck.")
        case "C":
            print("Cabin Class C!\nwindowless cabin below the car deck.")
        case _:
            print("Invalid cabin class!")


def part3():
    gender = str(input("What is your biological gender? (m/f): "))
    hemoglobin_value = float(input("What is your hemoglobin level? (in g/l): "))

    def answer(answer):
        print(f"Your hemoglobin value is {answer}.")

    match gender:
        case "f" | "female":
            if hemoglobin_value > 155.0:
                answer("too high")
            elif hemoglobin_value < 117.0:
                answer("too low")
            elif hemoglobin_value > 117.0 and hemoglobin_value < 155.0:
                answer("normal")
            else:
                print(f"somethings wrong: {hemoglobin_value}")
        case "m" | "male":
            if hemoglobin_value > 167.0:
                answer("too high")
            elif hemoglobin_value < 134.0:
                answer("too low")
            elif hemoglobin_value > 134.0 and hemoglobin_value < 167.0:
                answer("normal")
            else:
                print(f"somethings wrong: {hemoglobin_value}")
        case _:
            print(
                f"Something wrong? Dump:\nhemoglobin: {hemoglobin_value}\ngender: {gender}"
            )


def part4():
    year = int(input("\n\nEnter a year: "))

    if year % 4 == 0 or year % 400 == 0:
        print("It's a leap year")
    else:
        print("It's not a leap year")


if __name__ == "__main__":
    choice = str(input("Hello, what part of the 3rd exercise?\n(1,2,4,5,all): "))
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
