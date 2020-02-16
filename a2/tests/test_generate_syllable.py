from unittest import TestCase
from unittest.mock import patch
import dnd


class Test(TestCase):
    @patch('random.choice', side_effect=['b', 'a'])
    def test_syllable_first_consonant_first_vowel(self, mock_choice):
        actual = dnd.generate_syllable()
        self.assertEqual(actual, 'ba')

    @patch('random.choice', side_effect=['b', 'y'])
    def test_syllable_first_consonant_last_vowel(self, mock_choice):
        actual = dnd.generate_syllable()
        self.assertEqual(actual, 'by')

    @patch('random.choice', side_effect=['b', 'e'])
    def test_syllable_first_consonant_random_vowel(self, mock_choice):
        actual = dnd.generate_syllable()
        self.assertEqual(actual, 'be')

    @patch('random.choice', side_effect=['y', 'y'])
    def test_syllable_last_consonant_last_vowel(self, mock_choice):
        actual = dnd.generate_syllable()
        self.assertEqual(actual, 'yy')

    @patch('random.choice', side_effect=['y', 'a'])
    def test_syllable_last_consonant_first_vowel(self, mock_choice):
        actual = dnd.generate_syllable()
        self.assertEqual(actual, 'ya')

    @patch('random.choice', side_effect=['y', 'u'])
    def test_syllable_last_consonant_random_vowel(self, mock_choice):
        actual = dnd.generate_syllable()
        self.assertEqual(actual, 'yu')

    @patch('random.choice', side_effect=['m', 'o'])
    def test_syllable_random_consonant_random_vowel(self, mock_choice):
        actual = dnd.generate_syllable()
        self.assertEqual(actual, 'mo')
