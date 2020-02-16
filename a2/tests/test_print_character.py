"""
Demonstrated unit tests for print_character function
"""
from unittest import TestCase
import unittest.mock
import io
import dnd


class Test(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_character(self, mock_stdout):
        actual = {
            'Name': 'Somi',
            'Strength': 10,
            'Intelligence': 5,
            'Wisdom': 6,
            'Dexterity': 9,
            'Constitution': 13,
            'Charisma': 9,
            'inventory': [],
            'XP': 0,
            'class': 'sorcerer',
            'Race': 'the Frost Giants in Jotunheim',
            'HP': [4, 4]}
        dnd.print_character(actual)
        expected = 'Name Somi\nStrength 10\nIntelligence 5\nWisdom 6\nDexterity 9\nConstitution 13\nCharisma 9' \
                   '\ninventory []\nXP 0\nclass sorcerer' \
                   '\nRace the Frost Giants in Jotunheim\nHP [4, 4]\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_opponent(self, mock_stdout):
        actual = {
            'Name': 'Loki',
            'Strength': 5,
            'Intelligence': 20,
            'Wisdom': 20,
            'Dexterity': 6,
            'Constitution': 20,
            'Charisma': 6,
            'inventory': ['The Scepter'],
            'XP': 0,
            'class': 'sorcerer',
            'Race': 'the Frost Giants in Jotunheim',
            'HP': [20, 20]}
        dnd.print_character(actual)
        expected = 'Name Loki\nStrength 5\nIntelligence 20\nWisdom 20\nDexterity 6\nConstitution 20\nCharisma 6' \
                   '\ninventory [\'The Scepter\']\nXP 0\nclass sorcerer' \
                   '\nRace the Frost Giants in Jotunheim\nHP [20, 20]\n'

        self.assertEqual(mock_stdout.getvalue(), expected)
