"""
Demonstrated unit tests for attack function
"""
from unittest import TestCase
from unittest.mock import patch
import unittest.mock
import io
import dnd


class Test(TestCase):
    @patch('random.randint', side_effect=[2, 1])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_both_missed(self, mock_stdout, mock_roll):
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
        dnd.attack(actual_1, actual_2)
        expected = 'Dududu is attacking Loki by 2\nDududu missed\nLoki is going to attack now by 1' \
                   '\nLoki missed Dududu still alive\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('random.randint', side_effect=[6])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_p1_attack_p2_died(self, mock_stdout, mock_roll):
        actual_1 = {
            'Name': 'Dududu',
            'Strength': 5,
            'Intelligence': 5,
            'Wisdom': 5,
            'Dexterity': 5,
            'Constitution': 5,
            'Charisma': 5,
            'inventory': [],
            'experience points': 0,
            'class': 'sorcerer',
            'Race': 'Human',
            'HP': [5, 5]}
        actual_2 = {
            'Name': 'Loki',
            'Strength': 5,
            'Intelligence': 5,
            'Wisdom': 5,
            'Dexterity': 5,
            'Constitution': 5,
            'Charisma': 5,
            'inventory': ['The Scepter'],
            'experience points': 0,
            'class': 'sorcerer',
            'Race': 'the Frost Giants in Jotunheim',
            'HP': [5, 5]}
        dnd.attack(actual_1, actual_2)
        expected = 'Dududu is attacking Loki by 6\nLoki is dead\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('random.randint', side_effect=[6, 6])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_p1_attack_p2_alive_p2_attack_p1_died(self, mock_stdout, mock_roll):
        actual_1 = {
            'Name': 'Dududu',
            'Strength': 5,
            'Intelligence': 5,
            'Wisdom': 5,
            'Dexterity': 5,
            'Constitution': 5,
            'Charisma': 5,
            'inventory': [],
            'experience points': 0,
            'class': 'sorcerer',
            'Race': 'Human',
            'HP': [5, 5]}
        actual_2 = {
            'Name': 'Loki',
            'Strength': 5,
            'Intelligence': 5,
            'Wisdom': 5,
            'Dexterity': 5,
            'Constitution': 5,
            'Charisma': 5,
            'inventory': ['The Scepter'],
            'experience points': 0,
            'class': 'sorcerer',
            'Race': 'the Frost Giants in Jotunheim',
            'HP': [20, 20]}
        dnd.attack(actual_1, actual_2)
        expected = 'Dududu is attacking Loki by 6\nLoki still alive\n' \
                   'Loki is going to attack by 6\nDududu is dead\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('random.randint', side_effect=[6, 4])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_p1_attack_p2_alive_p2_attack_p1_alive(self, mock_stdout, mock_roll):
        actual_1 = {
            'Name': 'Dududu',
            'Strength': 5,
            'Intelligence': 5,
            'Wisdom': 5,
            'Dexterity': 3,
            'Constitution': 5,
            'Charisma': 5,
            'inventory': [],
            'experience points': 0,
            'class': 'sorcerer',
            'Race': 'Human',
            'HP': [5, 5]}
        actual_2 = {
            'Name': 'Loki',
            'Strength': 5,
            'Intelligence': 5,
            'Wisdom': 5,
            'Dexterity': 5,
            'Constitution': 5,
            'Charisma': 5,
            'inventory': ['The Scepter'],
            'experience points': 0,
            'class': 'sorcerer',
            'Race': 'the Frost Giants in Jotunheim',
            'HP': [20, 20]}
        dnd.attack(actual_1, actual_2)
        expected = 'Dududu is attacking Loki by 6\nLoki still alive\n' \
                   'Loki is going to attack by 4\nDududu is alive\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('random.randint', side_effect=[6, 2])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_p1_attack_p2_alive_p2_attack_and_missed(self, mock_stdout, mock_roll):
        actual_1 = {
            'Name': 'Dududu',
            'Strength': 5,
            'Intelligence': 5,
            'Wisdom': 5,
            'Dexterity': 5,
            'Constitution': 5,
            'Charisma': 5,
            'inventory': [],
            'experience points': 0,
            'class': 'sorcerer',
            'Race': 'Human',
            'HP': [8, 8]}
        actual_2 = {
            'Name': 'Loki',
            'Strength': 5,
            'Intelligence': 5,
            'Wisdom': 5,
            'Dexterity': 5,
            'Constitution': 5,
            'Charisma': 5,
            'inventory': ['The Scepter'],
            'experience points': 0,
            'class': 'sorcerer',
            'Race': 'the Frost Giants in Jotunheim',
            'HP': [20, 20]}
        dnd.attack(actual_1, actual_2)
        expected = 'Dududu is attacking Loki by 6\nLoki still alive\n' \
                   'Loki is going to attack by 2\nLoki missed Dududu is alive\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('random.randint', side_effect=[4, 10])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_p1_missed_p2_attack_p1_dead(self, mock_stdout, mock_roll):
        actual_1 = {
            'Name': 'Dududu',
            'Strength': 5,
            'Intelligence': 5,
            'Wisdom': 5,
            'Dexterity': 5,
            'Constitution': 5,
            'Charisma': 5,
            'inventory': [],
            'experience points': 0,
            'class': 'sorcerer',
            'Race': 'Human',
            'HP': [8, 8]}
        actual_2 = {
            'Name': 'Loki',
            'Strength': 5,
            'Intelligence': 5,
            'Wisdom': 5,
            'Dexterity': 5,
            'Constitution': 5,
            'Charisma': 5,
            'inventory': ['The Scepter'],
            'experience points': 0,
            'class': 'sorcerer',
            'Race': 'the Frost Giants in Jotunheim',
            'HP': [20, 20]}
        dnd.attack(actual_1, actual_2)
        expected = 'Dududu is attacking Loki by 4\nDududu missed\nLoki is going to attack now by 10\nDududu is dead\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('random.randint', side_effect=[4, 7])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_p1_missed_p2_attack_p1_alive(self, mock_stdout, mock_roll):
        actual_1 = {
            'Name': 'Dududu',
            'Strength': 5,
            'Intelligence': 5,
            'Wisdom': 5,
            'Dexterity': 5,
            'Constitution': 5,
            'Charisma': 5,
            'inventory': [],
            'experience points': 0,
            'class': 'sorcerer',
            'Race': 'Human',
            'HP': [8, 8]}
        actual_2 = {
            'Name': 'Loki',
            'Strength': 5,
            'Intelligence': 5,
            'Wisdom': 5,
            'Dexterity': 5,
            'Constitution': 5,
            'Charisma': 5,
            'inventory': ['The Scepter'],
            'experience points': 0,
            'class': 'sorcerer',
            'Race': 'the Frost Giants in Jotunheim',
            'HP': [20, 20]}
        dnd.attack(actual_1, actual_2)
        expected = 'Dududu is attacking Loki by 4\nDududu missed\nLoki is going to attack now by 7\nDududu is alive\n'
        self.assertEqual(mock_stdout.getvalue(), expected)
