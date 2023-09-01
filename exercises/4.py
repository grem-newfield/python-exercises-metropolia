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


# 5. Write a program that asks the user for a username and password. If either or both are incorrect, the program
# ask the user to enter the username and password again. This continues until the login information is correct or
# wrong credentials have been entered five times. If the information is correct, the program prints out `Welcome`.
# After five failed attempts the program prints out `Access denied`. The correct username is **python** and password
# **rules**.


def part5():
    username = "python"; password = "rules" 
    
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


# 6. Implement an algorithm for calculating an approximation for the value of pi (π). Let's assume that A is a unit
# circle. A unit circle has the radius of one and it is centered at the origin (0,0). Smallest possible square B
# is drawn around the unit circle so that circle A is completely inside the square. The corners of the square are now
# (-1,-1), (1, -1), (1, 1), and (-1, 1). If a large number of random points are scattered inside the square, the fraction
# of points that fall inside the circle A correlates with the fraction of the area of circle A compared to the area of
# square B: πr^2/4 = π*1^2/4 = π/4. This can be used as a simple method for calculating an approximation of the value
# of pi: Let's generate a large number of random points, such as one million, inside square B. Let N be the total number
# of random points. Each point inside the square is tested for whether it resides inside circle A. Let n be the total
# number of points that fall inside circle A. Now we have n/N≈π/4, and from that we get π≈4n/N. Write a program that
# asks the user how many random points to generate, and then calculates the approximate value of pi using the method
# explained above. At the end, the program prints out the approximation of pi to the user. (Notice that it is easy to
# test if a point falls inside circle A by testing if it fulfills the inequation x^2+y^2<1.).

# Write a program that
# asks the user how many random points to generate,
# and then calculates the approximate value of pi
# using the method
# explained above.


# At the end, the program prints out the approximation of pi to the user. (Notice that it is easy to
# test if a point falls inside circle A by testing if it fulfills the inequation x^2+y^2<1.).

def part6():
    from math import pi
    from random import  uniform

    radius = 1

    try: total_points = int(input("How many points? (integer) ").strip())
    except: print("Couldnt parse points amount"); return

    def generate_points(amount):
        points = []
        for _ in range(amount):
            point = [uniform(-1,1),uniform(-1,1)]
            points.append(point)
        return points

    def is_point_in_circle(point):
        return point[0]**2+point[1]**2 < 1

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
