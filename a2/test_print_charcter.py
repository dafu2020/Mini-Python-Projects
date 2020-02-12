from unittest import TestCase
import unittest.mock
import io
import dnd


class Test(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_character(self, mock_stdout):
        actual = {
            'Name': 'lyli',
            'Strength': 10,
            'Intelligence': 5,
            'Wisdom': 100,
            'Dexterity': 9,
            'Constitution': 20,
            'Charisma': 9,
            'inventory': [],
            'experience points': 0,
            'class': 'sorcerer',
            'Race': 'the Frost Giants in Jotunheim',
            'HP': [100, 20]}
        dnd.print_character(actual)
        expected = 'Name lyli\nStrength 10\nIntelligence 5\nWisdom 100\nDexterity 9\nConstitution 20\nCharisma 9' \
                   '\ninventory []\nexperience points 0\nclass sorcerer' \
                   '\nRace the Frost Giants in Jotunheim\nHP [100, 20]\n'
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
            'experience points': 0,
            'class': 'sorcerer',
            'Race': 'the Frost Giants in Jotunheim',
            'HP': [20, 20]}
        dnd.print_character(actual)
        expected = 'Name Loki\nStrength 5\nIntelligence 20\nWisdom 20\nDexterity 6\nConstitution 20\nCharisma 6' \
                   '\ninventory [\'The Scepter\']\nexperience points 0\nclass sorcerer' \
                   '\nRace the Frost Giants in Jotunheim\nHP [20, 20]\n'

        self.assertEqual(mock_stdout.getvalue(), expected)
