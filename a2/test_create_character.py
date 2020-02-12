from unittest import TestCase
from unittest.mock import patch
import dnd



class Test(TestCase):
    @patch('random.choice', side_effect=['a'])
    def test_random_a(self, mock_choice):
        actual = dnd.generate_vowel()
        self.assertEqual(actual, 'a')

    @patch('random.choice', side_effect=['a'])
    def test_create_character_one_syllable(self):

