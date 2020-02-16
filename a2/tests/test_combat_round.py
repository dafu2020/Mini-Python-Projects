"""
Demonstrated unit tests for combat_round function
"""
from unittest import TestCase
from unittest.mock import patch
import unittest.mock
import io
import dnd


class Test(TestCase):
    @patch('random.randint', side_effect=[1, 1, 2, 1, 2, 1])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_roll_same_points_once(self, mock_stdout, mock_roll):
        actual_1 = {
            'Name': 'Dududu',
            'Strength': 10,
            'Intelligence': 5,
            'Wisdom': 5,
            'Dexterity': 9,
            'Constitution': 12,
            'Charisma': 9,
            'inventory': [],
            'experience points': 0,
            'class': 'sorcerer',
            'Race': 'Human',
            'HP': [5, 5]}
        actual_2 = {
            'Name': 'Loki',
            'Strength': 5,
            'Intelligence': 20,
            'Wisdom': 20,
            'Dexterity': 6,
            'Constitution': 20,
            'Charisma': 6,
            'inventory': ['The Scepter'],
            'experience points': 0,
            'class': 'sorcerer',
            'Race': 'the Frost Giants in Jotunheim',
            'HP': [20, 20]}
        dnd.combat_round(actual_1, actual_2)
        dnd.print_character(actual_1)
        dnd.print_character(actual_2)
        expected = 'Dududu is attacking Loki by 2\nDududu missed\nLoki is going to attack now by 1' \
                   '\nLoki missed Dududu still alive\n' \
                   'Name Dududu\nStrength 10\nIntelligence 5\nWisdom 5\nDexterity 9\nConstitution 12\nCharisma 9\n' \
                   'inventory []\nexperience points 0\nclass sorcerer\nRace Human\nHP [5, 5]\n' \
                   'Name Loki\nStrength 5\nIntelligence 20\nWisdom 20\nDexterity 6\nConstitution 20\nCharisma 6' \
                   '\ninventory [\'The Scepter\']\nexperience points 0\nclass sorcerer\nRace the Frost Giants in ' \
                   'Jotunheim\nHP [20, 20]\n'

        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('random.randint', side_effect=[1, 1, 2, 2, 4, 4, 8, 2, 2, 1])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_roll_same_points_multiple_times(self, mock_stdout, mock_roll):
        actual_1 = {
            'Name': 'Dududu',
            'Strength': 10,
            'Intelligence': 5,
            'Wisdom': 5,
            'Dexterity': 9,
            'Constitution': 12,
            'Charisma': 9,
            'inventory': [],
            'experience points': 0,
            'class': 'sorcerer',
            'Race': 'Human',
            'HP': [5, 5]}
        actual_2 = {
            'Name': 'Loki',
            'Strength': 5,
            'Intelligence': 20,
            'Wisdom': 20,
            'Dexterity': 6,
            'Constitution': 20,
            'Charisma': 6,
            'inventory': ['The Scepter'],
            'experience points': 0,
            'class': 'sorcerer',
            'Race': 'the Frost Giants in Jotunheim',
            'HP': [20, 20]}
        dnd.combat_round(actual_1, actual_2)
        dnd.print_character(actual_1)
        dnd.print_character(actual_2)
        expected = 'Dududu is attacking Loki by 2\nDududu missed\nLoki is going to attack now by 1' \
                   '\nLoki missed Dududu still alive\n' \
                   'Name Dududu\nStrength 10\nIntelligence 5\nWisdom 5\nDexterity 9\nConstitution 12\nCharisma 9\n' \
                   'inventory []\nexperience points 0\nclass sorcerer\nRace Human\nHP [5, 5]\n' \
                   'Name Loki\nStrength 5\nIntelligence 20\nWisdom 20\nDexterity 6\nConstitution 20\nCharisma 6' \
                   '\ninventory [\'The Scepter\']\nexperience points 0\nclass sorcerer\nRace the Frost Giants in ' \
                   'Jotunheim\nHP [20, 20]\n'

        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('random.randint', side_effect=[8, 2, 2, 1])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_roll_different_points(self, mock_stdout, mock_roll):
        actual_1 = {
            'Name': 'Dududu',
            'Strength': 10,
            'Intelligence': 5,
            'Wisdom': 5,
            'Dexterity': 9,
            'Constitution': 12,
            'Charisma': 9,
            'inventory': [],
            'experience points': 0,
            'class': 'sorcerer',
            'Race': 'Human',
            'HP': [5, 5]}
        actual_2 = {
            'Name': 'Loki',
            'Strength': 5,
            'Intelligence': 20,
            'Wisdom': 20,
            'Dexterity': 6,
            'Constitution': 20,
            'Charisma': 6,
            'inventory': ['The Scepter'],
            'experience points': 0,
            'class': 'sorcerer',
            'Race': 'the Frost Giants in Jotunheim',
            'HP': [20, 20]}
        dnd.combat_round(actual_1, actual_2)
        dnd.print_character(actual_1)
        dnd.print_character(actual_2)
        expected = 'Dududu is attacking Loki by 2\nDududu missed\nLoki is going to attack now by 1' \
                   '\nLoki missed Dududu still alive\n' \
                   'Name Dududu\nStrength 10\nIntelligence 5\nWisdom 5\nDexterity 9\nConstitution 12\nCharisma 9\n' \
                   'inventory []\nexperience points 0\nclass sorcerer\nRace Human\nHP [5, 5]\n' \
                   'Name Loki\nStrength 5\nIntelligence 20\nWisdom 20\nDexterity 6\nConstitution 20\nCharisma 6' \
                   '\ninventory [\'The Scepter\']\nexperience points 0\nclass sorcerer\nRace the Frost Giants in ' \
                   'Jotunheim\nHP [20, 20]\n'

        self.assertEqual(mock_stdout.getvalue(), expected)
