"""
Demonstrated unit tests for validate_ function
"""
from unittest import TestCase
from lab06.maze import validate_move


class Test(TestCase):
    def test_not_valid_direction(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                     [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                     [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                     [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                     [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        argument2 = {'x': 0, 'y': 0}
        argument3 = 'nonsense'
        actual = validate_move(argument1, argument2, argument3)
        expected = False
        self.assertEqual(expected, actual)

    def test_not_valid_coordination(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                     [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                     [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                     [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                     [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        argument2 = {'x': -1, 'y': -1}
        argument3 = 'no'
        actual = validate_move(argument1, argument2, argument3)
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_beginning_of_board_north(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                     [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                     [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                     [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                     [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        argument2 = {'x': 0, 'y': 0}
        argument3 = 'n'
        actual = validate_move(argument1, argument2, argument3)
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_beginning_of_board_south(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                     [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                     [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                     [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                     [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        argument2 = {'x': 0, 'y': 0}
        argument3 = 's'
        actual = validate_move(argument1, argument2, argument3)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_beginning_of_board_west(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                     [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                     [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                     [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                     [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        argument2 = {'x': 0, 'y': 0}
        argument3 = 'w'
        actual = validate_move(argument1, argument2, argument3)
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_beginning_of_board_east(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                     [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                     [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                     [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                     [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        argument2 = {'x': 0, 'y': 0}
        argument3 = 'e'
        actual = validate_move(argument1, argument2, argument3)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_middle_of_board_north(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                     [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                     [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                     [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                     [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        argument2 = {'x': 2, 'y': 2}
        argument3 = 'n'
        actual = validate_move(argument1, argument2, argument3)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_middle_of_board_south(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                     [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                     [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                     [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                     [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        argument2 = {'x': 2, 'y': 2}
        argument3 = 's'
        actual = validate_move(argument1, argument2, argument3)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_middle_of_board_west(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                     [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                     [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                     [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                     [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        argument2 = {'x': 2, 'y': 2}
        argument3 = 'w'
        actual = validate_move(argument1, argument2, argument3)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_middle_of_board_east(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                     [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                     [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                     [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                     [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        argument2 = {'x': 2, 'y': 2}
        argument3 = 'w'
        actual = validate_move(argument1, argument2, argument3)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_end_of_board_north(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                     [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                     [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                     [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                     [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        argument2 = {'x': 2, 'y': 2}
        argument3 = 'n'
        actual = validate_move(argument1, argument2, argument3)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_end_of_board_south(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                     [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                     [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                     [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                     [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        argument2 = {'x': 2, 'y': 2}
        argument3 = 's'
        actual = validate_move(argument1, argument2, argument3)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_end_of_board_west(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                     [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                     [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                     [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                     [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        argument2 = {'x': 2, 'y': 2}
        argument3 = 'w'
        actual = validate_move(argument1, argument2, argument3)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_end_of_board_east(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                     [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                     [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                     [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                     [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        argument2 = {'x': 2, 'y': 2}
        argument3 = 'w'
        actual = validate_move(argument1, argument2, argument3)
        expected = True
        self.assertEqual(expected, actual)
