"""
Demonstrated unit tests for move_character function
"""
from unittest import TestCase
from lab06.maze import move_character


class Test(TestCase):
    def test_board_beginning_move_north(self):
        argument1 = 'n'
        argument2 = {'x': 0, 'y': 0}
        actual = move_character(argument1, argument2)
        expected = {'x': 0, 'y': 0}
        self.assertEqual(expected, actual)

    def test_board_beginning_move_south(self):
        argument1 = 's'
        argument2 = {'x': 0, 'y': 0}
        actual = move_character(argument1, argument2)
        expected = {'x': 1, 'y': 0}
        self.assertEqual(expected, actual)

    def test_board_beginning_move_west(self):
        argument1 = 'w'
        argument2 = {'x': 0, 'y': 0}
        actual = move_character(argument1, argument2)
        expected = {'x': 0, 'y': 0}
        self.assertEqual(expected, actual)

    def test_board_beginning_move_east(self):
        argument1 = 'e'
        argument2 = {'x': 0, 'y': 0}
        actual = move_character(argument1, argument2)
        expected = {'x': 0, 'y': 1}
        self.assertEqual(expected, actual)

    def test_board_beginning_move_north_full(self):
        argument1 = 'north'
        argument2 = {'x': 0, 'y': 0}
        actual = move_character(argument1, argument2)
        expected = {'x': 0, 'y': 0}
        self.assertEqual(expected, actual)

    def test_board_beginning_move_south_full(self):
        argument1 = 'south'
        argument2 = {'x': 0, 'y': 0}
        actual = move_character(argument1, argument2)
        expected = {'x': 1, 'y': 0}
        self.assertEqual(expected, actual)

    def test_board_beginning_move_west_full(self):
        argument1 = 'west'
        argument2 = {'x': 0, 'y': 0}
        actual = move_character(argument1, argument2)
        expected = {'x': 0, 'y': 0}
        self.assertEqual(expected, actual)

    def test_board_beginning_move_east_full(self):
        argument1 = 'east'
        argument2 = {'x': 0, 'y': 0}
        actual = move_character(argument1, argument2)
        expected = {'x': 0, 'y': 1}
        self.assertEqual(expected, actual)

    def test_board_middle_move_north(self):
        argument1 = 'n'
        argument2 = {'x': 2, 'y': 2}
        actual = move_character(argument1, argument2)
        expected = {'x': 1, 'y': 2}
        self.assertEqual(expected, actual)

    def test_board_middle_move_south(self):
        argument1 = 's'
        argument2 = {'x': 2, 'y': 2}
        actual = move_character(argument1, argument2)
        expected = {'x': 3, 'y': 2}
        self.assertEqual(expected, actual)

    def test_board_middle_move_west(self):
        argument1 = 'w'
        argument2 = {'x': 2, 'y': 2}
        actual = move_character(argument1, argument2)
        expected = {'x': 2, 'y': 1}
        self.assertEqual(expected, actual)

    def test_board_middle_move_north(self):
        argument1 = 'e'
        argument2 = {'x': 2, 'y': 2}
        actual = move_character(argument1, argument2)
        expected = {'x': 2, 'y': 3}
        self.assertEqual(expected, actual)

    def test_board_end_move_north(self):
        argument1 = 'n'
        argument2 = {'x': 4, 'y': 4}
        actual = move_character(argument1, argument2)
        expected = {'x': 3, 'y': 4}
        self.assertEqual(expected, actual)

    def test_board_end_move_south(self):
        argument1 = 's'
        argument2 = {'x': 4, 'y': 4}
        actual = move_character(argument1, argument2)
        expected = {'x': 4, 'y': 4}
        self.assertEqual(expected, actual)

    def test_board_end_move_west(self):
        argument1 = 'w'
        argument2 = {'x': 4, 'y': 4}
        actual = move_character(argument1, argument2)
        expected = {'x': 4, 'y': 3}
        self.assertEqual(expected, actual)

    def test_board_end_move_east(self):
        argument1 = 'e'
        argument2 = {'x': 4, 'y': 4}
        actual = move_character(argument1, argument2)
        expected = {'x': 4, 'y': 4}
        self.assertEqual(expected, actual)
