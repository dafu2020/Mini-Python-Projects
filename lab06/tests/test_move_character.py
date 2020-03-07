"""
Demonstrated unit tests for move_character function
"""
from unittest import TestCase
from lab06.maze import move_character


class Test(TestCase):
    def test_board_beginning_move_north(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                     [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                     [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                     [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                     [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        argument2 = 'n'
        argument3 = {'x': 0, 'y': 0}
        actual = move_character(argument1, argument2, argument3)
        expected = {'x': 0, 'y': 0}
        self.assertEqual(expected, actual)

    def test_board_beginning_move_south(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                     [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                     [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                     [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                     [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        argument2 = 's'
        argument3 = {'x': 0, 'y': 0}
        actual = move_character(argument1, argument2, argument3)
        expected = {'x': 1, 'y': 0}
        self.assertEqual(expected, actual)

    def test_board_beginning_move_west(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                     [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                     [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                     [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                     [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        argument2 = 'w'
        argument3 = {'x': 0, 'y': 0}
        actual = move_character(argument1, argument2, argument3)
        expected = {'x': 0, 'y': 0}
        self.assertEqual(expected, actual)

    def test_board_beginning_move_east(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                     [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                     [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                     [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                     [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        argument2 = 'e'
        argument3 = {'x': 0, 'y': 0}
        actual = move_character(argument1, argument2, argument3)
        expected = {'x': 0, 'y': 1}
        self.assertEqual(expected, actual)

    def test_board_beginning_move_north_full(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                     [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                     [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                     [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                     [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        argument2 = 'north'
        argument3 = {'x': 0, 'y': 0}
        actual = move_character(argument1, argument2, argument3)
        expected = {'x': 0, 'y': 0}
        self.assertEqual(expected, actual)

    def test_board_beginning_move_south_full(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                     [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                     [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                     [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                     [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        argument2 = 'south'
        argument3 = {'x': 0, 'y': 0}
        actual = move_character(argument1, argument2, argument3)
        expected = {'x': 1, 'y': 0}
        self.assertEqual(expected, actual)

    def test_board_beginning_move_west_full(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                     [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                     [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                     [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                     [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        argument2 = 'west'
        argument3 = {'x': 0, 'y': 0}
        actual = move_character(argument1, argument2, argument3)
        expected = {'x': 0, 'y': 0}
        self.assertEqual(expected, actual)

    def test_board_beginning_move_east_full(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                     [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                     [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                     [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                     [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        argument2 = 'east'
        argument3 = {'x': 0, 'y': 0}
        actual = move_character(argument1, argument2, argument3)
        expected = {'x': 0, 'y': 1}
        self.assertEqual(expected, actual)

    def test_board_middle_move_north(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                     [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                     [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                     [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                     [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        argument2 = 'n'
        argument3 = {'x': 2, 'y': 2}
        actual = move_character(argument1, argument2, argument3)
        expected = {'x': 1, 'y': 2}
        self.assertEqual(expected, actual)

    def test_board_middle_move_south(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                     [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                     [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                     [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                     [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        argument2 = 's'
        argument3 = {'x': 2, 'y': 2}
        actual = move_character(argument1, argument2, argument3)
        expected = {'x': 3, 'y': 2}
        self.assertEqual(expected, actual)

    def test_board_middle_move_west(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                     [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                     [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                     [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                     [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        argument2 = 'w'
        argument3 = {'x': 2, 'y': 2}
        actual = move_character(argument1, argument2, argument3)
        expected = {'x': 2, 'y': 1}
        self.assertEqual(expected, actual)

    def test_board_middle_move_east(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                     [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                     [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                     [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                     [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        argument2 = 'e'
        argument3 = {'x': 2, 'y': 2}
        actual = move_character(argument1, argument2, argument3)
        expected = {'x': 2, 'y': 3}
        self.assertEqual(expected, actual)

    def test_board_end_move_north(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                     [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                     [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                     [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                     [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        argument2 = 'n'
        argument3 = {'x': 4, 'y': 4}
        actual = move_character(argument1, argument2, argument3)
        expected = {'x': 3, 'y': 4}
        self.assertEqual(expected, actual)

    def test_board_end_move_south(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                     [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                     [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                     [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                     [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        argument2 = 's'
        argument3 = {'x': 4, 'y': 4}
        actual = move_character(argument1, argument2, argument3)
        expected = {'x': 4, 'y': 4}
        self.assertEqual(expected, actual)

    def test_board_end_move_west(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                     [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                     [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                     [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                     [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        argument2 = 'w'
        argument3 = {'x': 4, 'y': 4}
        actual = move_character(argument1, argument2, argument3)
        expected = {'x': 4, 'y': 3}
        self.assertEqual(expected, actual)

    def test_board_end_move_east(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                     [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                     [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                     [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                     [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        argument2 = 'e'
        argument3 = {'x': 4, 'y': 4}
        actual = move_character(argument1, argument2, argument3)
        expected = {'x': 4, 'y': 4}
        self.assertEqual(expected, actual)
