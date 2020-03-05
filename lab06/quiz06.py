import math
import time


def timer(func):
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer


@timer
def eratosthenes_cindy(upperbound):
    number_list = list(range(0, upperbound + 1))
    prime_list = []

    for i in range(0, int((upperbound ** 0.5) + 1)):
        if is_prime_number_cindy(i) is not False:
            prime_list.append(i)
            for j in number_list:
                if j % i == 0:
                    number_list.remove(j)

    result_list = sorted(prime_list + number_list)
    result_list.pop(0)
    if len(result_list) == 0:
        return []
    elif result_list[0] == 1:
        result_list.remove(result_list[0])
        return result_list
    else:
        return result_list


def is_prime_number_cindy(number):
    if number < 2:
        return False
    if number == 2:
        return True
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


@timer
def eratosthenes_anunay(upperbound):
    prime_list = list(range(2, upperbound + 1))
    for i in range(2, int(math.sqrt(upperbound)) + 1):
        for prime_checker in range(2, i):
            if (i % prime_checker) == 0:
                break
        else:
            for multiple_check in range((i + i), upperbound + 1, i):
                if multiple_check in prime_list:
                    prime_list.remove(multiple_check)
    return prime_list


@timer
def primes_vivian(lower, upper):
    prime_num = list(range(lower, upper + 1))
    if 1 in prime_num:
        prime_num.remove(1)
    if 0 in prime_num:
        prime_num.remove(0)
    for number in prime_num:
        for divisor in range(2, math.ceil(math.sqrt(upper))):
            if number % divisor == 0 and number != divisor:
                prime_num.remove(number)
                break
    return prime_num


def main():
    lower_bound = 0
    upper_bound = 1000
    cindy = eratosthenes_cindy(upper_bound)
    anunay = eratosthenes_anunay(upper_bound)
    vivian = primes_vivian(lower_bound, upper_bound)
    group = (cindy, anunay, vivian)
    if min(group) == cindy:
        print(f"eratosthenes_cindy is fastest")
    elif min(group) == anunay:
        print(f"eratosthenes_anunay is fastest")
    elif min(group) == vivian:
        print(f"primes_vivian is fastest")


if __name__ == "__main__":
    main()
