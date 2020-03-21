from unittest import TestCase
from exceptions import find_an_even


class Test(TestCase):
    def test_empty_list(self):
        argument = []
        with self.assertRaises(ValueError):
            find_an_even(argument)

    def test_list_size_one_no_even(self):
        argument = [1]
        with self.assertRaises(ValueError):
            find_an_even(argument)

    def test_list_size_one_even(self):
        argument = [2]
        expect = 2
        actual = find_an_even(argument)
        self.assertEqual(expect, actual)

    def test_list_no_even(self):
        argument = [1, 3, 5, 7]
        with self.assertRaises(ValueError):
            find_an_even(argument)

    def test_list_no_even_same(self):
        argument = [1, 3, 3, 7]
        with self.assertRaises(ValueError):
            find_an_even(argument)

    def test_list_contain_even(self):
        argument = [1, 2, 3, 5]
        expect = 2
        actual = find_an_even(argument)
        self.assertEqual(expect, actual)

    def test_list_contain_multiple_even(self):
        argument = [1, 2, 3, 4]
        expect = 2
        actual = find_an_even(argument)
        self.assertEqual(expect, actual)
