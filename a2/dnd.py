import random
import doctest


def roll_die(number_of_rolls, number_of_sides):
    """

    :param number_of_rolls: positive non-zero integers
    :param number_of_sides: positive non-zero integers
    :return: the result of the die rolling simulation as a integer
    """
    count = 0
    while count < number_of_rolls:
        roll_result = random.randint(1, number_of_sides)
        count += 1
        print(roll_result)
        return roll_result


# return the result of the last roll?? or return the  result of all the rolls (like dictionary)?

