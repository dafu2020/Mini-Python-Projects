import doctest


def eratosthenes(upperbound):
    """Calculate prime numbers
    A function mimic the Sieve of Eratosthenes method to find all prime numbers within the certain range.

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
    # make a list from 0 to N
    number_list = list(range(0, upperbound + 1))
    prime_list = []

    for i in range(0, int((upperbound ** 0.5) + 1)):
        # find the primes
        if is_prime_number(i) is not False:
            prime_list.append(i)
            # find the multiples of that prime
            for j in number_list:
                if j % i == 0:
                    number_list.remove(j)

    result_list = sorted(prime_list + number_list)  # join and sort the list
    if result_list[0] == 0:
        result_list.remove(result_list[0])
    if result_list[0] == 1:
        result_list.remove(result_list[0])

    return result_list


def is_prime_number(number):
    """ Prime number determiner
    A function used to determine whether a number is a prime number.

    :param number: a positive integer
    :precondition: must be a positive integer
    :postcondition: give boolean result of determination
    :return: whether a number is prime number as a boolean result

    >>> is_prime_number(1)
    False
    >>> is_prime_number(2)
    True
    >>> is_prime_number(9)
    False

    """
    if number < 2:
        return False
    if number == 2:
        return True
    for i in range(2, number):
        # if num(number) can be divided with no remainder by any number from 2 to number-1 (one number before it)
        # then it is not a prime number
        if number % i == 0:
            return False
    return True


def cash_money(canadian_money):
    """ Determine the amount of denominations
    A function accepts an amount of Canadian money, and determines the fewest of each bill and coin needed to present.

    :param canadian_money: a positive float that only has 2 decimal places
    precondition: must be a positive float that only has 2 decimal places
    postcondition: calculates the amount of each denomination that are required
    :return: the amount of each denomination that are required as a list

    >>> cash_money(66.53)
    [0, 1, 0, 1, 1, 0, 1, 2, 0, 0, 3]

    >>> cash_money(1150.67)
    [11, 1, 0, 0, 0, 0, 0, 2, 1, 1, 2]

    >>> cash_money(12763.23)
    [127, 1, 0, 1, 0, 1, 1, 0, 2, 0, 3]
    """

    denomination_list = [10000, 5000, 2000, 1000, 500, 200, 100, 25, 10, 5, 1]

    breakdown = []
    canadian_money *= 100

    for i in denomination_list:
        if canadian_money // i == 0:
            breakdown.append(0)
        elif canadian_money // i != 0:
            count = int(canadian_money // i)
            canadian_money = canadian_money % i
            breakdown.append(count)
    return breakdown


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
