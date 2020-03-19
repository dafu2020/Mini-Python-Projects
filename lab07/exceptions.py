def heron(my_number) -> float:
    """ Mimic Heron’s algorithm to find the square root of a number

    :param my_number: a number
    :precondition: my_number must be a number
    :postcondition: calculate the square root of number
    :return: the calculated square root as a float number

    """
    try:
        guess = my_number
        guess_product = guess * guess

        while guess_product != my_number:
            guess = (guess + (my_number / guess)) / 2
            guess_product = guess * guess

        return guess
    except ZeroDivisionError:
        print('No, I can’t do that!')
        return -1


def find_an_even(input_list):
    """Return the first even number in input_list

     :param input_list: a list of integers
     :precondition: input_list must be a list of integer
     :postcondition: return the first even number in input_list
     :raise ValueError: if input_list does not contain an even number
     :return: first even number in input_list

     """
    try:
        for i in input_list:
            if i % 2 == 0:
                return i
        else:
            raise ValueError
    except ValueError:
        print('wrong list')
        return -1


print(find_an_even([1, 4, 2]))
