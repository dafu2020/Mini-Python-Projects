from unittest import TestCase
from unittest.mock import patch
import dnd


class Test(TestCase):
    @patch('random.choice', side_effect=['b', 'a'])
    def test_one_syllable_name(self, mock_input):
        argument = 1
        actual = dnd.generate_name(argument)
        expected = "Ba"
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['y', 'y'])
    def test_one_syllable_name_same_consonant_and_vowel(self, mock_input):
        argument = 1
        actual = dnd.generate_name(argument)
        expected = "Yy"
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['b', 'a', 'b', 'a'])
    def test_two_syllables_name_same_syllable(self, mock_input):
        argument = 2
        actual = dnd.generate_name(argument)
        expected = "Baba"
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['b', 'a', 't', 'i'])
    def test_two_syllables_name_different_syllable(self, mock_input):
        argument = 2
        actual = dnd.generate_name(argument)
        expected = "Bati"
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['b', 'a', 't', 'i', 'd', 'u', 'y', 'o'])
    def test_multiple_syllables_name_different_syllable(self, mock_input):
        argument = 4
        actual = dnd.generate_name(argument)
        expected = "Batiduyo"
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y'])
    def test_multiple_syllables_name_same_consonant_and_vowel(self, mock_input):
        argument = 4
        actual = dnd.generate_name(argument)
        expected = "Yyyyyyyy"
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['b', 'a', 't', 'i', 'd', 'u', 'd', 'u', 'y', 'y'])
    def test_multiple_syllables_repeated_syllables(self, mock_input):
        argument = 5
        actual = dnd.generate_name(argument)
        expected = "Batiduduyy"
        self.assertEqual(expected, actual)
