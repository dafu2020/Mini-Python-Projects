from unittest import TestCase
from unittest.mock import patch
import unittest.mock
import io
import dnd


class Test(TestCase):
    @patch('random.randint', side_effect=[1, 1, 1])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_both_missed(self, mock_stdout, mock_roll):
        actual_1 = {
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
            'Race': 'Human',
            'HP': [100, 20]}
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
        dnd.attack(actual_1, actual_2)
        expected = 'lyli is attacking Loki by 1\nlyli missed\nLoki is going to attack now by 1' \
                   '\nLoki missed lyli still alive\n'
        self.assertEqual(mock_stdout.getvalue(), expected)
