"""
Demonstrate the unittest of find_an_even function.
"""
from unittest import TestCase
from exceptions import find_an_even


class Test(TestCase):
    def test_empty_list(self):
        """Test function with a empty list"""
        argument = []
        with self.assertRaises(ValueError):
            find_an_even(argument)

    def test_list_size_one_no_even(self):
        """Test function with a size one list containing no even number"""
        argument = [1]
        with self.assertRaises(ValueError):
            find_an_even(argument)

    def test_list_size_one_even(self):
        """Test function with a size one list containing one even number"""
        argument = [2]
        expect = 2
        actual = find_an_even(argument)
        self.assertEqual(expect, actual)

    def test_list_no_even(self):
        """Test function with a list containing no even number"""
        argument = [1, 3, 5, 7]
        with self.assertRaises(ValueError):
            find_an_even(argument)

    def test_list_no_even_same(self):
        """Test function with a list containing no even number and repeated number"""
        argument = [1, 3, 3, 7]
        with self.assertRaises(ValueError):
            find_an_even(argument)

    def test_list_contain_even(self):
        """Test function with a list containing even numbers"""
        argument = [1, 2, 3, 5]
        expect = 2
        actual = find_an_even(argument)
        self.assertEqual(expect, actual)

    def test_list_contain_multiple_even(self):
        """Test function with a list containing multiple even numbers"""
        argument = [1, 2, 3, 4]
        expect = 2
        actual = find_an_even(argument)
        self.assertEqual(expect, actual)

    def test_list_contain_multiple_repeated_even(self):
        """Test function with a list containing multiple even numbers and repeated number"""
        argument = [1, 2, 4, 4]
        expect = 2
        actual = find_an_even(argument)
        self.assertEqual(expect, actual)
