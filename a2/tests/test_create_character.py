"""
Demonstrated unit tests for create_character function
"""
from unittest import TestCase
from unittest.mock import patch
import dnd


class Test(TestCase):

    def test_not_valid_input_string(self):
        actual = 'uyy'
        dnd.create_character(actual)
        expected = None
        self.assertEqual(expected, dnd.create_character(actual))

    def test_not_valid_input_float(self):
        actual = 2.1
        dnd.create_character(actual)
        expected = None
        self.assertEqual(expected, dnd.create_character(actual))

    @patch('random.choice', side_effect=['b', 'a'])
    @patch('random.randint', side_effect=[1, 1, 1,
                                          1, 1, 1,
                                          1, 1, 1,
                                          1, 1, 1,
                                          1, 1, 1,
                                          1, 1, 1,
                                          1])
    @patch('builtins.input', side_effect=['1', '1'])
    def test_a_character_one_syllable_same_roll_same_class_race(self, mock_name, mock_roll, mock_class_race):
        actual = dnd.create_character(1)
        expected = {'Name': 'Ba', 'Strength': 3, 'Intelligence': 3, 'Wisdom': 3, 'Dexterity': 3, 'Constitution': 3,
                    'Charisma': 3, 'inventory': [], 'experience points': 0, 'class': 'Barbarian', 'Race': 'Dragonborn',
                    'HP': [1, 1]}
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['b', 'a'])
    @patch('random.randint', side_effect=[1, 4, 2,
                                          4, 2, 2,
                                          1, 1, 3,
                                          5, 1, 2,
                                          1, 6, 6,
                                          1, 6, 1,
                                          3])
    @patch('builtins.input', side_effect=['1', '1'])
    def test_a_character_one_syllable_different_roll_same_race_class(self, mock_name, mock_roll, mock_class_race):
        actual = dnd.create_character(1)
        expected = {'Name': 'Ba', 'Strength': 7, 'Intelligence': 8, 'Wisdom': 5, 'Dexterity': 8, 'Constitution': 13,
                    'Charisma': 8, 'inventory': [], 'experience points': 0, 'class': 'Barbarian', 'Race': 'Dragonborn',
                    'HP': [3, 3]}
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['b', 'a'])
    @patch('random.randint', side_effect=[1, 4, 2,
                                          4, 2, 2,
                                          1, 1, 3,
                                          5, 1, 2,
                                          1, 6, 6,
                                          1, 6, 1,
                                          3])
    @patch('builtins.input', side_effect=['7', '3'])
    def test_a_character_one_syllable_different_roll_different_race_class(self, mock_name, mock_roll, mock_class_race):
        actual = dnd.create_character(1)
        expected = {'Name': 'Ba', 'Strength': 7, 'Intelligence': 8, 'Wisdom': 5, 'Dexterity': 8, 'Constitution': 13,
                    'Charisma': 8, 'inventory': [], 'experience points': 0, 'class': 'Paladin', 'Race': 'Elf',
                    'HP': [3, 3]}
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['l', 'i', 'l', 'i', 's', 'a'])
    @patch('random.randint', side_effect=[1, 1, 1,
                                          1, 1, 1,
                                          1, 1, 1,
                                          1, 1, 1,
                                          1, 1, 1,
                                          1, 1, 1,
                                          1])
    @patch('builtins.input', side_effect=['1', '1'])
    def test_a_character_multi_syllables_same_roll_same_class_race(self, mock_name, mock_roll, mock_class_race):
        actual = dnd.create_character(3)
        expected = {'Name': 'Lilisa', 'Strength': 3, 'Intelligence': 3, 'Wisdom': 3, 'Dexterity': 3, 'Constitution': 3,
                    'Charisma': 3, 'inventory': [], 'experience points': 0, 'class': 'Barbarian', 'Race': 'Dragonborn',
                    'HP': [1, 1]}
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['l', 'i', 'l', 'i', 's', 'a'])
    @patch('random.randint', side_effect=[1, 4, 2,
                                          4, 2, 2,
                                          1, 1, 3,
                                          5, 1, 2,
                                          1, 6, 6,
                                          1, 6, 1,
                                          3])
    @patch('builtins.input', side_effect=['1', '1'])
    def test_a_character_multi_syllables_different_roll_same_race_class(self, mock_name, mock_roll, mock_class_race):
        actual = dnd.create_character(3)
        expected = {'Name': 'Lilisa', 'Strength': 7, 'Intelligence': 8, 'Wisdom': 5, 'Dexterity': 8, 'Constitution': 13,
                    'Charisma': 8, 'inventory': [], 'experience points': 0, 'class': 'Barbarian', 'Race': 'Dragonborn',
                    'HP': [3, 3]}
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['l', 'i', 'l', 'i', 's', 'a'])
    @patch('random.randint', side_effect=[1, 4, 2,
                                          4, 2, 2,
                                          1, 1, 3,
                                          5, 1, 2,
                                          1, 6, 6,
                                          1, 6, 1,
                                          3])
    @patch('builtins.input', side_effect=['7', '3'])
    def test_a_character_multi_syllables_different_roll_different_race_class(self, mock_name, mock_roll, mock_class_race):
        actual = dnd.create_character(3)
        expected = {'Name': 'Lilisa', 'Strength': 7, 'Intelligence': 8, 'Wisdom': 5, 'Dexterity': 8, 'Constitution': 13,
                    'Charisma': 8, 'inventory': [], 'experience points': 0, 'class': 'Paladin', 'Race': 'Elf',
                    'HP': [3, 3]}
        self.assertEqual(expected, actual)
