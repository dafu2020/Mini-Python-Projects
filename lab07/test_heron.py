"""
Demonstrate the unittest of heron function.
"""
from unittest import TestCase
from exceptions import heron


class Test(TestCase):
    def test_heron_zero(self):
        """Test function with 0"""
        argument = 0
        expected = 0
        actual = heron(argument)
        self.assertEqual(expected, actual)

    def test_heron_1(self):
        """Test function with 1"""
        argument = 1
        expected = 1.0
        actual = heron(argument)
        self.assertEqual(expected, actual)

    def test_heron_positive_number(self):
        """Test function with a positive number"""
        argument = 4
        expected = 2.0
        actual = heron(argument)
        self.assertEqual(expected, actual)

    def test_heron_negative_one(self):
        """Test function with -1"""
        argument = -1
        expected = -1
        actual = heron(argument)
        self.assertEqual(expected, actual)

    def test_heron_negative_number(self):
        """Test function with a negative number"""
        argument = -100
        expected = -1
        actual = heron(argument)
        self.assertEqual(expected, actual)
