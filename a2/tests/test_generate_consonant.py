"""
Demonstrated unit tests for generate_consonant function
"""
from unittest import TestCase
from unittest.mock import patch
import dnd


class Test(TestCase):
    @patch('random.choice', side_effect=['b'])
    def test_fist_item_on_the_list(self, mock_choice):
        actual = dnd.generate_consonant()
        self.assertEqual(actual, 'b')

    @patch('random.choice', side_effect=['y'])
    def test_last_item_on_the_list(self, mock_choice):
        actual = dnd.generate_consonant()
        self.assertEqual(actual, 'y')

    @patch('random.choice', side_effect=['r'])
    def test_random_item_on_the_list(self, mock_choice):
        actual = dnd.generate_consonant()
        self.assertEqual(actual, 'r')
