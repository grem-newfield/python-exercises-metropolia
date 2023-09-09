from classes import Book, Magazine

# the print_information part is implemented as a __repr__ method


def part1():
    print("Magazine example:\n")
    mag = Magazine("Donald Duck", "Aki Hyyppä")
    print(mag)

    print("\nBook example:\n")
    book = Book("Compartment No. 6", "Rosa Liksom", 192)
    print(book)


if __name__ == "__main__":
    part1()
