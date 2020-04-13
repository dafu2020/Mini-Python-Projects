from unittest import TestCase
from lab09.factorial import factorial_recursive_helper


class Test(TestCase):
    def test_factorial_recursive_helper_0(self):
        argument = 0
        actual = factorial_recursive_helper(argument)
        expected = 1
        self.assertEqual(expected, actual)

    def test_factorial_recursive_helper_1(self):
        argument = 1
        actual = factorial_recursive_helper(argument)
        expected = 1
        self.assertEqual(expected, actual)

    def test_factorial_recursive_helper_bigger_than_1(self):
        argument = 5
        actual = factorial_recursive_helper(argument)
        expected = 120
        self.assertEqual(expected, actual)

    def test_factorial_recursive_helper_bigger_than_10(self):
        argument = 11
        actual = factorial_recursive_helper(argument)
        expected = 39916800
        self.assertEqual(expected, actual)
