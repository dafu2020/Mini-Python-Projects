from unittest import TestCase
from unittest.mock import patch
import dnd


class Test(TestCase):
    @patch('random.choice', side_effect=['a'])
    def test_random_a(self, mock_choice):
        actual = dnd.generate_vowel()
        self.assertEqual(actual, 'a')

    @patch('random.choice', side_effect=['e'])
    def test_random_e(self, mock_choice):
        actual = dnd.generate_vowel()
        self.assertEqual(actual, 'e')

    @patch('random.choice', side_effect=['i'])
    def test_random_i(self, mock_choice):
        actual = dnd.generate_vowel()
        self.assertEqual(actual, 'i')

    @patch('random.choice', side_effect=['o'])
    def test_random_o(self, mock_choice):
        actual = dnd.generate_vowel()
        self.assertEqual(actual, 'o')

    @patch('random.choice', side_effect=['u'])
    def test_random_u(self, mock_choice):
        actual = dnd.generate_vowel()
        self.assertEqual(actual, 'u')