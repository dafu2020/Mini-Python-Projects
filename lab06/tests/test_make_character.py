"""
Demonstrated unit tests for make_character function
"""
from unittest import TestCase
from lab06.maze import make_character
from unittest.mock import patch


class Test(TestCase):
    @patch('builtins.input', return_value='jane')
    def test_make_character(self, mock_input):
        expected = {'name': 'Jane', 'x': 0, 'y': 0}
        actual = make_character()
        self.assertEqual(expected, actual)
