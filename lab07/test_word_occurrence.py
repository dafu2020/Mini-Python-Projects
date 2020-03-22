"""
Demonstrate the unittest of word_occurrence function.
"""
from unittest import TestCase
import file_io


class Test(TestCase):
    def test_empty_list(self):
        """Test function with a empty list"""
        argument = []
        actual = file_io.word_occurrence(argument)
        expected = {}
        self.assertEqual(actual, expected)

    def test_list_size_one(self):
        """Test function with a size one list containing str"""
        argument = ['one']
        actual = file_io.word_occurrence(argument)
        expected = {'one': 1}
        self.assertEqual(actual, expected)

    def test_list_unique_items(self):
        """Test function with list containing non-repeated str"""
        argument = ['one', 'two', 'three', 'four']
        actual = file_io.word_occurrence(argument)
        expected = {'four': 1, 'one': 1, 'three': 1, 'two': 1}
        self.assertEqual(actual, expected)

    def test_list_repeated_items(self):
        """Test function with list containing repeated str that are equal occurrences"""
        argument = ['one', 'two', 'three', 'four', 'one', 'two', 'three', 'four']
        actual = file_io.word_occurrence(argument)
        expected = {'four': 2, 'one': 2, 'three': 2, 'two': 2}
        self.assertEqual(actual, expected)

    def test_list_items_not_same_number(self):
        """Test function with list containing repeated str"""
        argument = ['two', 'three', 'four', 'four', 'four', 'one', 'two', 'three', 'four', 'three', 'three', 'four']
        actual = file_io.word_occurrence(argument)
        expected = {'four': 5, 'one': 1, 'three': 4, 'two': 2}
        self.assertEqual(actual, expected)

    def test_list_all_numbers(self):
        """Test function with list containing repeated number"""
        argument = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        actual = file_io.word_occurrence(argument)
        expected = {1: 1, 2: 2, 3: 3, 4: 4}
        self.assertEqual(actual, expected)

    def test_list_mixture(self):
        """Test function with list containing repeated number and str mixture"""
        argument = ['two', 'three', 'four', 'four', 'four', 'one', 'two', 'three', 'four', 'three', 'three', 'four', 1,
                    2, 2, 3, 3, 3, 4, 4, 4, 4]
        actual = file_io.word_occurrence(argument)
        expected = {1: 1, 2: 2, 3: 3, 4: 4, 'four': 5, 'one': 1, 'three': 4, 'two': 2}
        self.assertEqual(actual, expected)
