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


