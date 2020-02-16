"""
Demonstrated unit tests for choose_inventory function
"""
from unittest import TestCase
from unittest.mock import patch
import unittest.mock
import io
import dnd


class Test(TestCase):
    @patch('builtins.input', side_effect=['-1'])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_buy_nothing(self, mock_stdout, mock_inputs):
        actual = {'Name': 'Sasi', 'Strength': 10, 'Intelligence': 5, 'Wisdom': 7, 'Dexterity': 9, 'Constitution': 20,
                  'Charisma': 9, 'inventory': [], 'experience points': 0, 'class': 'sorcerer', 'Race': 'Elf',
                  'HP': [6, 6]}
        dnd.choose_inventory(actual)
        expected = {'Charisma': 9, 'Constitution': 20, 'Dexterity': 9, 'HP': [6, 6], 'Intelligence': 5,
                    'Name': 'Sasi', 'Race': 'Elf', 'Strength': 10, 'Wisdom': 7, 'class': 'sorcerer',
                    'experience points': 0, 'inventory': []}
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['1', '-1'])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_buy_one_thing(self, mock_stdout, mock_inputs):
        actual = {'Name': 'Sasi', 'Strength': 10, 'Intelligence': 5, 'Wisdom': 7, 'Dexterity': 9, 'Constitution': 20,
                  'Charisma': 9, 'inventory': [], 'experience points': 0, 'class': 'sorcerer', 'Race': 'Elf',
                  'HP': [6, 6]}
        dnd.choose_inventory(actual)
        expected = {'Charisma': 9, 'Constitution': 20, 'Dexterity': 9, 'HP': [6, 6], 'Intelligence': 5,
                    'Name': 'Sasi', 'Race': 'Elf', 'Strength': 10, 'Wisdom': 7, 'class': 'sorcerer',
                    'experience points': 0, 'inventory': ['sword']}
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['1', '1', '-1'])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_buy_two_same_things(self, mock_stdout, mock_inputs):
        actual = {'Name': 'Sasi', 'Strength': 10, 'Intelligence': 5, 'Wisdom': 7, 'Dexterity': 9, 'Constitution': 20,
                  'Charisma': 9, 'inventory': [], 'experience points': 0, 'class': 'sorcerer', 'Race': 'Elf',
                  'HP': [6, 6]}
        dnd.choose_inventory(actual)
        expected = {'Charisma': 9, 'Constitution': 20, 'Dexterity': 9, 'HP': [6, 6], 'Intelligence': 5,
                    'Name': 'Sasi', 'Race': 'Elf', 'Strength': 10, 'Wisdom': 7, 'class': 'sorcerer',
                    'experience points': 0, 'inventory': ['sword', 'sword']}
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['1', '3', '-1'])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_buy_two_different_things(self, mock_stdout, mock_inputs):
        actual = {'Name': 'Sasi', 'Strength': 10, 'Intelligence': 5, 'Wisdom': 7, 'Dexterity': 9, 'Constitution': 20,
                  'Charisma': 9, 'inventory': [], 'experience points': 0, 'class': 'sorcerer', 'Race': 'Elf',
                  'HP': [6, 6]}
        dnd.choose_inventory(actual)
        expected = {'Charisma': 9, 'Constitution': 20, 'Dexterity': 9, 'HP': [6, 6], 'Intelligence': 5,
                    'Name': 'Sasi', 'Race': 'Elf', 'Strength': 10, 'Wisdom': 7, 'class': 'sorcerer',
                    'experience points': 0, 'inventory': ['sword', 'Iris(sword)']}
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['1', '3', '7', '10', '-1'])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_buy_multiple_things(self, mock_stdout, mock_inputs):
        actual = {'Name': 'Sasi', 'Strength': 10, 'Intelligence': 5, 'Wisdom': 7, 'Dexterity': 9, 'Constitution': 20,
                  'Charisma': 9, 'inventory': [], 'experience points': 0, 'class': 'sorcerer', 'Race': 'Elf',
                  'HP': [6, 6]}
        dnd.choose_inventory(actual)
        expected = {'Charisma': 9, 'Constitution': 20, 'Dexterity': 9, 'HP': [6, 6], 'Intelligence': 5,
                    'Name': 'Sasi', 'Race': 'Elf', 'Strength': 10, 'Wisdom': 7, 'class': 'sorcerer',
                    'experience points': 0, 'inventory': ['sword', 'Iris(sword)', 'W870 Shotgun', 'Crystal Carillon']}
        self.assertEqual(actual, expected)
