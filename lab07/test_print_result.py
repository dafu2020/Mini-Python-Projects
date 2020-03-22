"""
Demonstrate the unittest of print_result function.
"""
from unittest import TestCase
import unittest.mock
import io
import file_io


class Test(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_empty_list(self, mock_stdout):
        """Test function with a empty list"""
        argument = []
        file_io.print_result(argument)
        expected = ''
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_non_nested_size_one_list(self, mock_stdout):
        """Test function with a non-nested list"""
        argument = ['one', 1]
        with self.assertRaises(TypeError):
            file_io.print_result(argument)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_nested_size_one_list(self, mock_stdout):
        """Test function with a size one nested list"""
        argument = [[1, 'one']]
        file_io.print_result(argument)
        expected = 'one - 1\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_list_size_less_than_ten_value_all_number(self, mock_stdout):
        """Test function with a size less than ten nested list"""
        argument = [[5, 5], [4, 4], [3, 3], [2, 2], [1, 1]]
        file_io.print_result(argument)
        expected = '5 - 5\n4 - 4\n3 - 3\n2 - 2\n1 - 1\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_list_size_less_than_ten_value_all_str(self, mock_stdout):
        """Test function with a size less than ten nested list with string"""
        argument = [[5, 'five'], [4, 'four'],
                    [3, 'three'], [2, 'two'], [1, 'one']]
        file_io.print_result(argument)
        expected = 'five - 5\nfour - 4\nthree - 3\ntwo - 2\none - 1\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_list_size_ten_value_all_number(self, mock_stdout):
        """Test function with a size ten nested list with number"""
        argument = [[10, 10], [9, 9], [8, 8], [7, 7], [6, 6], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1]]
        file_io.print_result(argument)
        expected = '10 - 10\n9 - 9\n8 - 8\n7 - 7\n6 - 6\n5 - 5\n4 - 4\n3 - 3\n2 - 2\n1 - 1\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_list_size_ten_value_all_str(self, mock_stdout):
        """Test function with a size ten nested list with string"""
        argument = [[10, 'ten'], [9, 'nine'], [8, 'eight'], [7, 'seven'], [6, 'six'], [5, 'five'], [4, 'four'],
                    [3, 'three'], [2, 'two'], [1, 'one']]
        file_io.print_result(argument)
        expected = 'ten - 10\nnine - 9\neight - 8\nseven - 7\nsix - 6\nfive - 5\nfour - 4\nthree - 3\ntwo - 2\none - 1\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_list_size_ten_value_str_num_mix(self, mock_stdout):
        """Test function with a size ten nested list with string and number"""
        argument = [[10, 10], [9, 9], [8, 8], [7, 'seven'], [6, 'six'], [5, 'five'], [4, 'four'],
                    [3, 'three'], [2, 'two'], [1, 'one']]
        file_io.print_result(argument)
        expected = '10 - 10\n9 - 9\n8 - 8\nseven - 7\nsix - 6\nfive - 5\nfour - 4\nthree - 3\ntwo - 2\none - 1\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_list_size_more_than_ten_value_str_num_mix(self, mock_stdout):
        """Test function with a size more than ten nested list with string and number"""
        argument = [[10, 10], [9, 9], [8, 8], [7, 'seven'], [6, 'six'], [5, 'five'], [4, 'four'],
                    [3, 'three'], [2, 'two'], [1, 'one'], [1, 'new']]
        file_io.print_result(argument)
        expected = '10 - 10\n9 - 9\n8 - 8\nseven - 7\nsix - 6\nfive - 5\nfour - 4\nthree - 3\ntwo - 2\n' \
                   'one - 1\nnew - 1\n'
        self.assertEqual(mock_stdout.getvalue(), expected)
