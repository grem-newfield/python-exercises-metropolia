from random import randint


def part1():
    number = 1000
    while number > 0:
        if number % 3 == 0:
            print(" ", number, end="")
        number -= 1


def part2():
    def inches_to_cm(inches):
        return inches * 2.54

    print("Inches to cm converter.\n")
    while True:
        number = input("Type in inches: ").strip()
        try:
            if float(number) < 0:
                print("Negative number.")
                break
            print(f"Converted to cm: {inches_to_cm(float(number))}")
        except:
            print("NaN.")
            break


def part3():
    numbers = []
    print("Throw me some numbers.\n")
    while True:
        try:
            numbers.append(float(input("Type: ").strip()))
            print(f"Numbers given: {numbers}")
        except:
            print("NaN.")
            break
    numbers.sort()
    if len(numbers) == 0:
        print("You gave no numbers.")
        return
    print(f"Largest and smallest: {numbers.pop()} , {numbers.pop(0)}")


def part4():
    from random import randrange

    secret_number = randrange(1, 10)
    print("I want to play a game.")
    print("Guess my number!")
    while True:
        try:
            guess = float(input("Type: ").strip())
            if guess > secret_number:
                print("Too high")
            elif guess < secret_number:
                print("Too low")
            else:
                print("Correct")
                break
        except:
            print("NaN.")
            continue


def part5():
    username = "python"
    password = "rules"

    login_tries = 5

    while login_tries > 0:
        login_tries -= 1
        print("Please log-in.")
        inputted_username = input("Username: ").strip()
        inputted_password = input("Password: ").strip()
        if inputted_password == password and inputted_username == username:
            print("Welcome")
            break
        print("Access denied.\n\n")
        print(f"Tries left: {login_tries}")
    print("\n\n")


def part6():
    from math import pi
    from random import uniform

    radius = 1

    try:
        total_points = int(input("How many points? (integer) ").strip())
    except:
        print("Couldnt parse points amount")
        return

    def generate_points(amount):
        points = []
        for _ in range(amount):
            point = [uniform(-1, 1), uniform(-1, 1)]
            points.append(point)
        return points

    def is_point_in_circle(point):
        return point[0] ** 2 + point[1] ** 2 < 1

    points = generate_points(total_points)
    points_inside = 0

    for point in points:
        if is_point_in_circle(point):
            points_inside += 1

    # π≈4n/N.
    # N = total number
    # n = numbers in circle A

    approximate_pi = 4 * (points_inside / total_points)
    print(f"Approximate PI based on {total_points} random points: {approximate_pi}")

    circle_A = pi * radius**2
    circle_A_origin = (0, 0)
    square_B = 1 * 1


if __name__ == "__main__":
    choice = str(input("Hello, what part of the 3rd exercise?\n(1,2,3,4,5,6,all): "))
    match choice:
        case "1":
            part1()
        case "2":
            part2()
        case "3":
            part3()
        case "4":
            part4()
        case "5":
            part5()
        case "6":
            part6()
        case "all":
            part1()
            part2()
            part3()
            part4()
            part5()
            part6()
        case _:
            print("Wrong input?\nExiting...")
