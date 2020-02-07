from unittest import TestCase
import lab04


class Test(TestCase):
    def test_eratosthenes_zero(self):
        """Test number zero"""
        argument = 0
        expected = []
        lab04.eratosthenes(argument)
        self.assertEqual(expected, lab04.eratosthenes(argument), "The number is zero.")

    def test_eratosthenes_one(self):
        """Test the smallest positive integer, one"""
        argument = 1
        expected = []
        lab04.eratosthenes(argument)
        self.assertEqual(expected, lab04.eratosthenes(argument), "The number is the smallest positive integer, one. ")

    def test_eratosthenes_two(self):
        """Test the two, the smallest prime number """
        argument = 2
        expected = [2]
        lab04.eratosthenes(argument)
        self.assertEqual(expected, lab04.eratosthenes(argument), "The number is the smallest prime number. ")

    def test_eratosthenes_thirty_one(self):
        """Test the upper-bond number is primer number"""
        argument = 31
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        lab04.eratosthenes(argument)
        self.assertEqual(expected, lab04.eratosthenes(argument),
                         "The number is a prime number, and an upperbound number.")

    def test_eratosthenes_one_hundred(self):
        """Test the integer one hundred"""
        argument = 100
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        lab04.eratosthenes(argument)
        self.assertEqual(expected, lab04.eratosthenes(argument), "The number is integer one hundred.")

