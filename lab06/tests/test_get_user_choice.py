"""
Demonstrated unit tests for get_user_choice function
"""
from unittest import TestCase
from lab06.maze import get_user_choice
from unittest.mock import patch


class Test(TestCase):
    @patch('builtins.input', return_value='')
    def test_empty_input(self, mock_input):
        expected = ''
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='N')
    def test_one_letter_input_uppercase(self, mock_input):
        expected = 'n'
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='n')
    def test_one_letter_input_lowercase(self, mock_input):
        expected = 'n'
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='NORTH')
    def test_all_uppercase(self, mock_input):
        expected = 'north'
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='North')
    def test_capitalize(self, mock_input):
        expected = 'north'
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='north')
    def test_all_lowercase(self, mock_input):
        expected = 'north'
        actual = get_user_choice()
        self.assertEqual(expected, actual)
