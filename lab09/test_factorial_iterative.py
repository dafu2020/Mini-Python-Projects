from unittest import TestCase
from lab09.factorial import factorial_iterative


class Test(TestCase):
    def test_factorial_iterative_zero(self):
        argument = 0
        actual = factorial_iterative(argument)[0]
        expected = 1
        self.assertEqual(expected, actual)

    def test_factorial_iterative_one(self):
        argument = 1
        actual = factorial_iterative(argument)[0]
        expected = 1
        self.assertEqual(expected, actual)

    def test_factorial_iterative_five(self):
        argument = 5
        actual = factorial_iterative(argument)[0]
        expected = 120
        self.assertEqual(expected, actual)
