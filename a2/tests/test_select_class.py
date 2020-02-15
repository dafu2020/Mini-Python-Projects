"""
Demonstrated unit tests for select_class function
"""
from unittest import TestCase
from unittest.mock import patch
import dnd


class Test(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_Barbarian(self, mock_input):
        actual = dnd.select_class()
        expected = 'Barbarian'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2'])
    def test_Bard(self, mock_input):
        actual = dnd.select_class()
        expected = 'Bard'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['3'])
    def test_Cleric(self, mock_input):
        actual = dnd.select_class()
        expected = 'Cleric'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['4'])
    def test_Druid(self, mock_input):
        actual = dnd.select_class()
        expected = 'Druid'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['5'])
    def test_Fighter(self, mock_input):
        actual = dnd.select_class()
        expected = 'Fighter'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['6'])
    def test_Monk(self, mock_input):
        actual = dnd.select_class()
        expected = 'Monk'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['7'])
    def test_Paladin(self, mock_input):
        actual = dnd.select_class()
        expected = 'Paladin'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['8'])
    def test_Ranger(self, mock_input):
        actual = dnd.select_class()
        expected = 'Ranger'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['9'])
    def test_Rogue(self, mock_input):
        actual = dnd.select_class()
        expected = 'Rogue'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['10'])
    def test_Sorcerer(self, mock_input):
        actual = dnd.select_class()
        expected = 'Sorcerer'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['11'])
    def test_Warlock(self, mock_input):
        actual = dnd.select_class()
        expected = 'Warlock'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['12'])
    def test_Wizard(self, mock_input):
        actual = dnd.select_class()
        expected = 'Wizard'
        self.assertEqual(expected, actual)
