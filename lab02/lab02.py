import random


def roll_die(number_of_rolls=int, number_of_side=int):
    """simulate rolling a die of the specified size the specified number of times"""
    total_points = random.randint(number_of_rolls, number_of_side * number_of_rolls)
    return total_points


def main():
    print(roll_die(2, 6))


if __name__ == "__main__":
    main()


def create_name():
    """Random name generator
    When execute this function will return a string of random letters.
    """
    letters = 'abcdefghijklmnopqrstuvwxyz'
    selection = random.choices(letters, k=3)
    print(selection)
    result = "".join(selection)
    return result.capitalize()


def main():
    print(create_name())


if __name__ == "__main__":
    main()
