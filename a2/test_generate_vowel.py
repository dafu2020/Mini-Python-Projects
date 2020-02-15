"""
Demonstrated unit tests for generate_vowel function
"""
from unittest import TestCase
from unittest.mock import patch
import dnd


class Test(TestCase):
    @patch('random.choice', side_effect=['a'])
    def test_first_item_on_the_list(self, mock_choice):
        actual = dnd.generate_vowel()
        self.assertEqual(actual, 'a')

    @patch('random.choice', side_effect=['y'])
    def test_last_item_on_the_list(self, mock_choice):
        actual = dnd.generate_vowel()
        self.assertEqual(actual, 'y')

    @patch('random.choice', side_effect=['i'])
    def test_random_item_on_the_list(self, mock_choice):
        actual = dnd.generate_vowel()
        self.assertEqual(actual, 'i')
