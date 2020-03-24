import doctest


def heron(my_number: int) -> float:
    """ Mimic Heron’s algorithm to find the square root of a number

    :param my_number: a integer
    :precondition: my_number must be a integer
    :postcondition: calculate the square root of number
    :return: the calculated square root as a float number

    >>> heron(4)
    2.0
    >>> heron(9)
    3.0
    >>> heron(100)
    10.0

    """
    try:
        if my_number < 0 and my_number != -1:   # all negative number will raise ZeroDivisionError
            raise ZeroDivisionError

        else:
            guess = my_number   # start the guess with the number itself

        while guess ** 2 - my_number > 0.00001:     # conducting the heron's algorithism
            guess = (guess + my_number / guess) / 2
        guess = round(guess, 2)
        return guess
    except ZeroDivisionError:
        print('No, I can’t do that!')
        return -1


def find_an_even(input_list: list) -> int:
    """Return the first even number in input_list

     :param input_list: a list of integers
     :precondition: input_list must be a list of integer
     :postcondition: return the first even number in input_list
     :raise ValueError: if input_list does not contain an even number
     :return: first even number in input_list

     >>> my_list = [1, 2, 3, 4, 5, 6]
     >>> find_an_even(my_list)
     2

     >>> my_list = [2, 4, 6, 2.0]
     >>> find_an_even(my_list)
     2

     >>> my_list = [8, 4, 2]
     >>> find_an_even(my_list)
     8

     """
    for i in input_list:
        if i % 2 == 0:
            return i    # if the list contain a even number, return it and stop
    else:
        raise ValueError    # else raise ValueError


def main():
    doctest.testmod()
    test_list_0 = []  # empty list
    test_list_1 = [1]  # list size one
    test_list_2 = [1, 2, 3]  # list contain ond even number
    test_list_3 = [1, 3, 5]  # list contain no even number

    test_list_collection = [test_list_0, test_list_1, test_list_2, test_list_3]

    for test_list in test_list_collection:
        try:
            print(find_an_even(test_list))
        except ValueError:
            print('The list do not contain even number')


if __name__ == '__main__':
    main()

# print(find_an_even([2]))
# print(heron(-3))
