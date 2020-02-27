"""
Demonstrate how to calculate the sum and the dot product of two sparse vectors as dictionaries
"""

import doctest


# store vector as dictionary
def vector_to_dictionary(sparse_vector=list) -> dict:
    """ convert sparse vector to dictionary.

    :param sparse_vector: a list contains only number
    :precondition: sparse_vector must be a list that contains only number
    :postcondiiton: convert the sparse vector to dictionary form
    :return: the correctly converted sparse vector as a dictionary
    >>> sparse_vector = [1]
    >>> vector_to_dictionary(sparse_vector)
    {0: 1, 'length': 1}
    >>> sparse_vector = [1, 0, 0, 1]
    >>> vector_to_dictionary(sparse_vector)
    {0: 1, 3: 1, 'length': 4}
    >>> sparse_vector = [1, 0, 0, 2, 0, 0, 0, 3, 0, 0, 4]
    >>> vector_to_dictionary(sparse_vector)
    {0: 1, 3: 2, 7: 3, 10: 4, 'length': 11}
    """
    length_vector = len(sparse_vector)
    my_dic = {}
    for keys, values in enumerate(sparse_vector):
        my_dic[keys] = values
        if my_dic[keys] == 0:
            my_dic.pop(keys)
    my_dic['length'] = length_vector
    return my_dic


# add the vector dictionaries
def sparse_add(vector_one=dict, vector_two=dict) -> dict:
    """Calculate sum.

    A function to calculate the sum of two sparse vectors in dictionary form.
    :param vector_one: a dictionary
    :param vector_two: a dictionary
    :precondition: vector_one and vector_two must be sparse vectors in dictionary form with equal length
    :postcondiition: a new dictionary that represent the sum of two sparse vector
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
    add_dic = {'length': vector_one['length']}
    if vector_one['length'] == vector_two['length']:
        for key_one in vector_one:
            if key_one not in vector_two:
                add_dic[key_one] = vector_one[key_one]
            elif key_one in vector_one and key_one != 'length':
                add_dic[key_one] = vector_one[key_one] + vector_two[key_one]
                if add_dic[key_one] == 0:
                    add_dic.pop(key_one)
        for key_two in vector_two:
            if key_two not in vector_one:
                add_dic[key_two] = vector_two[key_two]
    return add_dic


# sum the element-wise products of their elements
def sparse_dot_product(vector_one=dict, vector_two=dict) -> dict:
    """Calculate dot product.

    A function to calculate the dot product of two sparse vectors.
    :param vector_one: a dictionary
    :param vector_two: a dictionary
    :precondition: vector_one and vector_two must be sparse vectors in dictionary form with equal length
    :postcondiition: calculate the dot product of two sparse vector
    :return: correctly calculated dot product of two sparse vector as a number
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
    if vector_one['length'] == vector_two['length']:
        for key_one in vector_one:
            if key_one in vector_two.keys() and key_one != 'length':
                dot_product += vector_one[key_one]*vector_two[key_one]
            else:
                dot_product += 0
    return dot_product


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
