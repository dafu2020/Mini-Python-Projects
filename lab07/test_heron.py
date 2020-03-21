from unittest import TestCase
from exceptions import heron


class Test(TestCase):
    def test_heron_zero(self):
        argument = 0
        expected = 0
        actual = heron(argument)
        self.assertEqual(expected, actual)

    def test_heron_1(self):
        argument = 1
        expected = 1.0
        actual = heron(argument)
        self.assertEqual(expected, actual)

    def test_heron_positive_number(self):
        argument = 4
        expected = 2.0
        actual = heron(argument)
        self.assertEqual(expected, actual)

    def test_heron_negative_one(self):
        argument = -1
        expected = -1
        actual = heron(argument)
        self.assertEqual(expected, actual)

    def test_heron_negative_number(self):
        argument = -100
        expected = -1
        actual = heron(argument)
        self.assertEqual(expected, actual)

