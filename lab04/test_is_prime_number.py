from unittest import TestCase
import lab04


class Test(TestCase):
    def test_is_prime_number_zero(self):
        """Test number zero."""
        argument = 0
        expected = False
        lab04.is_prime_number(argument)
        self.assertEqual(expected, lab04.is_prime_number(argument),
                         "The number is zero.")

    def test_is_prime_number_smallest_integer(self):
        """Test the smallest integer."""
        argument = 1
        expected = False
        lab04.is_prime_number(argument)
        self.assertEqual(expected, lab04.is_prime_number(argument),
                         "The number is the smallest positive integer.")

    def test_is_prime_number_two(self):
        """Test integer two, the smallest prime number."""
        argument = 2
        expected = True
        lab04.is_prime_number(argument)
        self.assertEqual(expected, lab04.is_prime_number(argument),
                         "The number two, the smallest prime number")

    def test_is_prime_number_thirty_one(self):
        """Test number thirty one, a prime number larger than 10."""
        argument = 31
        expected = True
        lab04.is_prime_number(argument)
        self.assertEqual(expected, lab04.is_prime_number(argument),
                         "The number thirty one, a prime number larger than 10")

    def test_is_prime_number_one_hundred(self):
        """Test number one hundred, a non-prime number larger than 10."""
        argument = 100
        expected = False
        lab04.is_prime_number(argument)
        self.assertEqual(expected, lab04.is_prime_number(argument),
                         "The number one hundred, a non-prime number larger than 10.")
