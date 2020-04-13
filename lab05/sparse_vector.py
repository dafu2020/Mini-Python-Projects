"""
Demonstrate how to calculate the sum and the dot product of two sparse vectors as dictionaries
"""

import doctest


def sparse_add(vector_one=dict, vector_two=dict) -> dict:
    """Calculate the sum of two sparse vectors

    :param vector_one: a dictionary that only contains integer as values
    :param vector_two: a dictionary that only contains integer as values
    :precondition: vector_one and vector_two must be sparse vectors of integers in dictionary form with equal length
    :postcondition: a new dictionary that represent the sum of two sparse vector
    :return: correctly calculated sum of two sparse vector that stored in a dictionary

    >>> vector_one  =  {0: 1, 'length': 1}
    >>> vector_two =  {0: 1, 'length': 1}
    >>> sparse_add(vector_one, vector_two)
    {'length': 1, 0: 2}

    >>> vector_one  =  {0: 1, 'length': 1}
    >>> vector_two =  {0: -1, 'length': 1}
    >>> sparse_add(vector_one, vector_two)
    {'length': 1}

    >>> vector_one  =  {0: 1, 2: 1, 4: 2, 6: 1, 9: 1, 'length': 11}
    >>> vector_two =  {0: -1, 2: 2, 7: 3, 10: 4, 'length': 11}
    >>> sparse_add(vector_one, vector_two)
    {'length': 11, 2: 3, 4: 2, 6: 1, 9: 1, 7: 3, 10: 4}
    """
    # create a dictionary to store result
    sum_dict = {'length': vector_one['length']}

    # eliminate empty vector(s)
    if vector_one['length'] == 0 and vector_two['length'] == 0:
        return None
    else:
        if vector_one['length'] == vector_two['length']:    # two vectors must be equal length
            for key_one in vector_one:
                # include keys only present in the first vector
                if key_one not in vector_two:
                    sum_dict[key_one] = vector_one[key_one]
                # add values with the same key
                elif key_one in vector_one and key_one != 'length':
                    sum_dict[key_one] = vector_one[key_one] + vector_two[key_one]
                    # remove any key-value pair with value of 0
                    if sum_dict[key_one] == 0:
                        sum_dict.pop(key_one)
            for key_two in vector_two:
                # include keys only present in the second vector
                if key_two not in vector_one:
                    sum_dict[key_two] = vector_two[key_two]
        return sum_dict


def sparse_dot_product(vector_one=dict, vector_two=dict) -> dict:
    """Calculate dot product.

    A function to calculate the dot product of two sparse vectors.
    :param vector_one: a dictionary that only contains integer as values
    :param vector_two: a dictionary that only contains integer as values
    :precondition: vector_one and vector_two must be sparse vectors of integers in dictionary form with equal length
    :postcondition: calculate the dot product of two sparse vector
    :return: correctly calculated dot product of two sparse vector as an integer
    >>> vector_one  =  {0: 1, 'length': 1}
    >>> vector_two =  {0: 1, 'length': 1}
    >>> sparse_dot_product(vector_one, vector_two)
    1
    >>> vector_one  =  {0: 1, 'length': 2}
    >>> vector_two =  {1: 1, 'length': 2}
    >>> sparse_dot_product(vector_one, vector_two)
    0
    >>> vector_one  =  {0: 1, 1: 2, 'length': 2}
    >>> vector_two =  {1: 1, 'length': 2}
    >>> sparse_dot_product(vector_one, vector_two)
    2
    """
    dot_product = 0
    if vector_one['length'] == 0 and vector_two['length'] == 0:
        return None
    else:
        if vector_one['length'] == vector_two['length']:
            for key_one in vector_one:
                if key_one in vector_two and key_one != 'length':
                    dot_product += vector_one[key_one] * vector_two[key_one]
                else:
                    dot_product += 0
        return dot_product


def main():
    """
    Test the functions in this module.
    """
    doctest.testmod()


if __name__ == "__main__":
    main()
