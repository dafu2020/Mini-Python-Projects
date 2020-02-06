import doctest


def dijkstra(my_list):
    """Assort a given list
    Function to sort out a list of randomly shuffled
    strings: 'red', 'white', and 'blue' in a specific order.

    :param my_list: a non-empty list that contains randomly shuffled
    strings: 'red', 'white', and 'blue'.
    :pre-condition: the list passed to the function will be a non-empty list of strings that are either "red", "blue", or "white".
    :post-condition: a sorted list.

    >>> my_list = ["red"]
    >>> dijkstra(my_list)
    >>> print(my_list)
    ['red']

    >>> my_list = ["blue", "white", "red"]
    >>> dijkstra(my_list)
    >>> print(my_list)
    ['red', 'white', 'blue']

    >>> my_list = ['red', 'red', 'red']
    >>> dijkstra(my_list)
    >>> print(my_list)
    ['red', 'red', 'red']

    >>> my_list = ["red", "white", "blue"]
    >>> dijkstra(my_list)
    >>> print(my_list)
    ['red', 'white', 'blue']

    >>> my_list = ["red", "white", "blue", "white", "blue", "blue", "white", "red"]
    >>> dijkstra(my_list)
    >>> print(my_list)
    ['red', 'red', 'white', 'white', 'white', 'blue', 'blue', 'blue']

    >>> my_list = ["red", "blue", "red"]
    >>> dijkstra(my_list)
    >>> print(my_list)
    ['red', 'red', 'blue']
    """

    my_list.sort()

    for item in my_list:
        if item == "blue":
            my_list.remove("blue")
            my_list.append("blue")
        else:
            my_list


def main():
    doctest.testmod()
    my_list = ["white", "white", "blue", "blue", "red", "white", "blue"]
    dijkstra(my_list)
    print(my_list)


if __name__ == "__main__":
    main()

# test:
# ["red"]
# ["blue", "white", "red"]
# ["red", "red", "red"]
# ["red", "white", "blue"]
# ["red", "blue", "white", "white", "red", "blue", "white", "white", "red", "blue", "white", "white"]
# ["red", "blue", "red"]
