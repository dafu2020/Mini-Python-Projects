from unittest import TestCase
import lab04


class Test(TestCase):
    def test_is_prime_number_smallest(self):
        """Test the smallest integer"""
        argument = 1
        expected = False
        lab04.is_prime_number(argument)
        self.assertEqual(expected, lab04.is_prime_number(argument), "The number is the smallest positive integer.")

    def test_is_prime_number_two(self):
        """Test the integer number two"""
        argument = 2
        expected = True
        lab04.is_prime_number(argument)
        self.assertEqual(expected, lab04.is_prime_number(argument),
                         "The number is the integer number two.")

    def test_is_prime_number_less_than_ten(self):
        """Test the integer number bigger than two but less than ten"""
        argument = 9
        expected = False
        lab04.is_prime_number(argument)
        self.assertEqual(expected, lab04.is_prime_number(argument),
                         "The integer number is bigger than two but less than ten.")

    def test_is_prime_number_less_than_one_hundred(self):
        """Test the integer number than ten but less than one hundred"""
        argument = 77
        expected = False
        lab04.is_prime_number(argument)
        self.assertEqual(expected, lab04.is_prime_number(argument),
                         "The integer number is bigger than ten but less than one hundred.")

    def test_is_prime_number_larger_than_one_hundred(self):
        """Test the integer number bigger than two but less than ten"""
        """Test the integer number bigger than fifty but less than one hundred."""
        argument = 121
        expected = False
        lab04.is_prime_number(argument)
        self.assertEqual(expected, lab04.is_prime_number(argument),
                         "The integer number is bigger than hundred.")
