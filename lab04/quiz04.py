"""Function to find out the minimum, maximum , average and spread of the list.
"""

import doctest


def statistics(number_list):
    """Function to perform statistic calculations

    :param number_list: a list contains integers and floats.
    :precondition: the number_list can only contain integers and floats.
    :postcondition: return a list of statistic results.
    :return: a list contains the length minimum, maximum, average and spread of the given list.

    >>> statistics([])
    [None, None, None, None, None]

    >>> statistics([1,2,3,4,5,6])
    [6, 1, 6, 3.5, 5]

    >>> statistics([-1,-2,-3,-4,-5,-6])
    [6, -6, -1, -3.5, 5]

    >>> statistics([1.0,1,2,2.0])
    [4, 1.0, 2, 1.5, 1.0]

    >>> statistics([8,2,7])
    [3, 2, 8, 5.67, 6]

    """

    if len(number_list) == 0:
        none_list = [None, None, None, None, None]
        return none_list

    else:
        list_length = len(number_list)

        list_max = max(number_list)

        list_min = min(number_list)

        list_average = round(sum(number_list) / len(number_list), 2)

        list_spread = list_max - list_min

        return [list_length, list_min, list_max, list_average, list_spread]


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
