from unittest import TestCase

from lab09.factorial import factorial_recursive


class Test(TestCase):
    def test_factorial_recursive_zero(self):
        argument = 0
        actual = factorial_recursive(argument)[0]
        expected = 1
        self.assertEqual(expected, actual)

    def test_factorial_recursive_one(self):
        argument = 1
        actual = factorial_recursive(argument)[0]
        expected = 1
        self.assertEqual(expected, actual)

    def test_factorial_recursive_bigger_than_5(self):
        argument = 5
        actual = factorial_recursive(argument)[0]
        expected = 120
        self.assertEqual(expected, actual)

    def test_factorial_recursive_bigger_than_10(self):
        argument = 11
        actual = factorial_recursive(argument)[0]
        expected = 39916800
        self.assertEqual(expected, actual)
