from unittest import TestCase
from unittest.mock import patch
import dnd


class Test(TestCase):
    @patch('random.choice', side_effect=['b'])
    def test_random_b(self, mock_choice):
        actual = dnd.generate_consonant()
        self.assertEqual(actual, 'b')

    @patch('random.choice', side_effect=['f'])
    def test_random_f(self, mock_choice):
        actual = dnd.generate_consonant()
        self.assertEqual(actual, 'f')

    @patch('random.choice', side_effect=['j'])
    def test_random_j(self, mock_choice):
        actual = dnd.generate_consonant()
        self.assertEqual(actual, 'j')

    @patch('random.choice', side_effect=['m'])
    def test_random_m(self, mock_choice):
        actual = dnd.generate_consonant()
        self.assertEqual(actual, 'm')

    @patch('random.choice', side_effect=['r'])
    def test_random_r(self, mock_choice):
        actual = dnd.generate_consonant()
        self.assertEqual(actual, 'r')

    @patch('random.choice', side_effect=['x'])
    def test_random_x(self, mock_choice):
        actual = dnd.generate_consonant()
        self.assertEqual(actual, 'x')