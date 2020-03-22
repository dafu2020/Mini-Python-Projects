from unittest import TestCase
import file_io


class Test(TestCase):
    def test_empty_dict(self):
        argument = {}
        with self.assertRaises(IndexError):
            file_io.top_ten(argument)

    def test_dict_size_one_all_number(self):
        argument = {0: 0}
        with self.assertRaises(IndexError):
            file_io.top_ten(argument)

    def test_dict_size_ten_all_number(self):
        argument = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
        actual = file_io.top_ten(argument)
        expected = [[10, 10], [9, 9], [8, 8], [7, 7], [6, 6], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1]]
        self.assertEqual(actual, expected)

    def test_dict_size_more_than_ten_all_number(self):
        argument = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12, 13: 13}
        actual = file_io.top_ten(argument)
        expected = [[13, 13], [12, 12], [11, 11], [10, 10], [9, 9], [8, 8], [7, 7], [6, 6], [5, 5], [4, 4]]
        self.assertEqual(actual, expected)

    def test_dict_same_occurrence_all_number(self):
        argument = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 10, 12: 10, 13: 10}
        actual = file_io.top_ten(argument)
        expected = [[10, 13], [10, 12], [10, 11], [10, 10], [9, 9], [8, 8], [7, 7], [6, 6], [5, 5], [4, 4]]
        self.assertEqual(actual, expected)

    def test_dict_size_one_all_str(self):
        argument = {'nothing': 0}
        with self.assertRaises(IndexError):
            file_io.top_ten(argument)

    def test_dict_size_ten_all_str(self):
        argument = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
                    'nine': 9, 'ten': 10}
        actual = file_io.top_ten(argument)
        expected = [[10, 'ten'], [9, 'nine'], [8, 'eight'], [7, 'seven'], [6, 'six'], [5, 'five'], [4, 'four'],
                    [3, 'three'], [2, 'two'], [1, 'one']]
        self.assertEqual(actual, expected)

    def test_dict_size_more_than_ten_all_str(self):
        argument = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
                    'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12}
        actual = file_io.top_ten(argument)
        expected = [[12, 'twelve'], [11, 'eleven'], [10, 'ten'], [9, 'nine'], [8, 'eight'], [7, 'seven'], [6, 'six'],
                    [5, 'five'], [4, 'four'], [3, 'three']]
        self.assertEqual(actual, expected)

    def test_dict_same_occurrence_all_str(self):
        argument = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
                    'nine': 9, 'ten': 10, 'eleven': 10, 'twelve': 10}
        actual = file_io.top_ten(argument)
        expected = [[10, 'twelve'], [10, 'ten'], [10, 'eleven'], [9, 'nine'], [8, 'eight'], [7, 'seven'], [6, 'six'],
                    [5, 'five'], [4, 'four'], [3, 'three']]
        self.assertEqual(actual, expected)

    def test_dict_str_and_number_mixture(self):
        argument = {'one': 1, 'two': 2, 3: 3, 'four': 4, 'five': 5, 6: 6, 'seven': 7, 'eight': 8,
                    'nine': 9, 'ten': 10, 1: 10, 'twelve': 10}
        with self.assertRaises(TypeError):
            file_io.top_ten(argument)
