from unittest import TestCase
from unittest.mock import patch
import dnd


class Test(TestCase):
    @patch('random.choice', side_effect=['g', 'a'])
    def test_syllable_g_a(self, mock_choice):
        actual = dnd.generate_syllable()
        self.assertEqual(actual, 'ga')

    @patch('random.choice', side_effect=['y', 'y'])
    def test_syllable_y_y(self, mock_choice):
        actual = dnd.generate_syllable()
        self.assertEqual(actual, 'yy')

    @patch('random.choice', side_effect=['k', 'i'])
    def test_syllable_g_a(self, mock_choice):
        actual = dnd.generate_syllable()
        self.assertEqual(actual, 'ki')

    @patch('random.choice', side_effect=['m', 'o'])
    def test_syllable_g_a(self, mock_choice):
        actual = dnd.generate_syllable()
        self.assertEqual(actual, 'mo')

    @patch('random.choice', side_effect=['n', 'u'])
    def test_syllable_g_a(self, mock_choice):
        actual = dnd.generate_syllable()
        self.assertEqual(actual, 'nu')

    @patch('random.choice', side_effect=['x', 'e'])
    def test_syllable_g_a(self, mock_choice):
        actual = dnd.generate_syllable()
        self.assertEqual(actual, 'xe')
