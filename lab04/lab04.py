import doctest

# do unit test
def eratosthenes(upperbound):
    """Calculate prime numbers
    A function mimic Sieve of Eratosthenes method to find all prime numbers up to any given limit.

    :param upperbound: a positive integer
    :precondition: must be a positive integer
    :postcondition: calculates the correct prime numbers between [0, upperbound]
    :return: all primes between [0, upperbound] as a list.

    >>> eratosthenes(30)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    >>> eratosthenes(10)
    [2, 3, 5, 7]
    >>> eratosthenes(100)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    """
    # max_number = int(upperbound ** 0.5)
    # make a list from 0 to N
    number_list = list(range(0, upperbound + 1))
    prime_list = []

    for i in range(0, int((upperbound ** 0.5) + 1)):
        # find the primes
        if is_prime_number(i) is not False:
            prime_list.append(i)
            # find the multiple of prime
            for j in number_list:
                if j % i == 0:
                    number_list.remove(j)

    result_list = sorted(prime_list + number_list)  # join and sort the list
    result_list.remove(result_list[0])  # remove 1, which is not a prime number
    return result_list


def is_prime_number(number):
    if number < 2:
        return False
    if number == 2:
        return True
    for i in range(2, number):
        # if num(number) can be divided with no remainder by any number from 2 to num-1
        # then it is not a prime number
        if number % i == 0:
            return False
    return True


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
