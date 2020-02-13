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
    def test_a_character_input_one(self, mock_name, mock_roll, mock_class_race):
        actual = dnd.create_character(1)
        expected = {'Name': 'ba', 'Strength': 3, 'Intelligence': 3, 'Wisdom': 3, 'Dexterity': 3, 'Constitution': 3,
                    'Charisma': 3, 'inventory': [], 'experience points': 0, 'class': 'Barbarian', 'Race': 'Dragonborn',
                    'HP': [1, 1]}
        self.assertEqual(expected, actual)
