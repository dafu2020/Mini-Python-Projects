"""
Demonstrated unit tests for select_race function
"""
from unittest import TestCase
from unittest.mock import patch
import dnd


class Test(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_Dragonborn(self, mock_input):
        actual = dnd.select_race()
        expected = 'Dragonborn'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2'])
    def test_Dwarf(self, mock_input):
        actual = dnd.select_race()
        expected = 'Dwarf'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['3'])
    def test_Elf(self, mock_input):
        actual = dnd.select_race()
        expected = 'Elf'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['4'])
    def test_Gnome(self, mock_input):
        actual = dnd.select_race()
        expected = 'Gnome'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['5'])
    def test_Half_Elf(self, mock_input):
        actual = dnd.select_race()
        expected = 'Half-Elf'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['6'])
    def test_Halfling(self, mock_input):
        actual = dnd.select_race()
        expected = 'Halfling'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['7'])
    def test_Half_Orc(self, mock_input):
        actual = dnd.select_race()
        expected = 'Half-Orc'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['8'])
    def test_Human(self, mock_input):
        actual = dnd.select_race()
        expected = 'Human'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['9'])
    def test_Tiefling(self, mock_input):
        actual = dnd.select_race()
        expected = 'Tiefling'
        self.assertEqual(expected, actual)