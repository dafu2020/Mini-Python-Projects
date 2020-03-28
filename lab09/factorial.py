import time


def timer(func):
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


def write_file(function_name, number, run):
    with open('results.txt', 'a') as file_object:
        file_object.write(f'the run time for {function_name}({number}) is {run} \n')


@timer
def factorial_iterative(my_number: int) -> tuple:
    """

    :param my_number:
    :return:
    """
    factorial = 1
    for i in range(1, my_number + 1):
        factorial *= i

    return factorial


@timer
def factorial_recursive(my_number: int) -> int:
    """

    :param my_number:
    :return:
    """
    return factorial_recursive_helper(my_number)


def factorial_recursive_helper(num: int) -> int:
    """s

    :param num:
    :return:
    """

    if num <= 1:
        return 1
    return num * factorial_recursive_helper(num - 1)


def main():
    for i in range(1, 101):
        (iterative_value, iterative_name, iterative_runtime) = factorial_iterative(i)
        (recursive_value, recursive_name, recursive_runtime) = factorial_recursive(i)
        if iterative_runtime > recursive_runtime:
            with open('results.txt', 'a') as file_object:
                file_object.write(f'{recursive_name} is faster for number {i}!\n\n')
        elif recursive_runtime < iterative_runtime:
            with open('results.txt', 'a') as file_object:
                file_object.write(f'{iterative_name} is faster for number {i}!\n\n')
        else:
            with open('results.txt', 'a') as file_object:
                file_object.write(f'they are equally fast for number {i}\n\n')


if __name__ == '__main__':
    main()
