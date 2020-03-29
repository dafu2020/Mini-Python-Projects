import time
import doctest


def timer(func):
    """
    Display the time required for execute a function.

    :param func: a function
    :precondition: func must be a function
    :postcondition: write the result of the runtime in file
    """

    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time

        # answer in file
        function_name = func.__name__
        write_file(function_name, args[0], run_time)
        return value, function_name, run_time

    return wrapper_timer


def write_file(function_name: str, number: int, run: float):
    """
    Write in a file.

    :param function_name: a string
    :param number: an integer
    :param run: a float
    :precondition: function_name must be string; number must a integer; run must be a float
    :postcondition: write in a file with the provided information
    """
    with open('results.txt', 'a') as file_object:
        file_object.write(f'the run time for {function_name}({number}) is {run} \n')


@timer
def factorial_iterative(my_number: int) -> int:
    """Calculate factorial using loop

    :param my_number: an integer
    :precondition: my_number myst ba an integer
    :postcondition: calculate the factorial using a loop
    :return: the calculated factorial as an integer

    >>> factorial_iterative(0)
    1

    >>> factorial_iterative(5)
    120

    """
    factorial = 1
    for i in range(1, my_number + 1):
        factorial *= i

    return factorial


@timer
def factorial_recursive(my_number: int) -> int:
    """Calculate factorial using recursion

    Pass the value of my_number to the factorial_recursive_helper function for actual calculation.
    :param my_number: an integer
    :precondition: my_number myst ba an integer
    :postcondition: calculate the factorial using recursion
    :return: the calculated factorial as an integer

    >>> factorial_iterative(0)
    1

    >>> factorial_iterative(5)
    120
    """
    return factorial_recursive_helper(my_number)


def factorial_recursive_helper(num: int) -> int:
    """Calculate factorial using recursion

    :param num: an integer
    :precondition: my_number myst ba an integer
    :postcondition: calculate the factorial using recursion
    :return: the calculated factorial as an integer

    >>> factorial_iterative(0)
    1

    >>> factorial_iterative(5)
    120
    """

    if num <= 1:
        return 1
    return num * factorial_recursive_helper(num - 1)


def main():
    """
    Drive program
    """
    doctest.testmod()

    for i in range(1, 101):
        (iterative_value, iterative_name, iterative_runtime) = factorial_iterative(i)
        (recursive_value, recursive_name, recursive_runtime) = factorial_recursive(i)
        if iterative_runtime > recursive_runtime:
            with open('results.txt', 'a') as file_object:
                file_object.write(f'{recursive_name} is faster for number {i}!\n\n')
        elif recursive_runtime > iterative_runtime:
            with open('results.txt', 'a') as file_object:
                file_object.write(f'{iterative_name} is faster for number {i}!\n\n')
        elif recursive_runtime == iterative_runtime:
            with open('results.txt', 'a') as file_object:
                file_object.write(f'they are equally fast for number {i}\n\n')


if __name__ == '__main__':
    main()
