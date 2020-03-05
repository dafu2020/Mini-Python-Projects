"""
Demonstrated unit tests for check_if_exit_reached function
"""
from unittest import TestCase
from lab06.maze import check_if_exit_reached


class Test(TestCase):
    def test_length_one_board(self):
        argument1 = [[0, 0]]
        argument2 = {'x': 0, 'y': 0}
        actual = check_if_exit_reached(argument1, argument2)
        expected = True
        self.assertEqual(expected, actual)

    def test_board_beginning(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]]
        argument2 = {'x': 0, 'y': 0}
        actual = check_if_exit_reached(argument1, argument2)
        expected = False
        self.assertEqual(expected, actual)

    def test_board_middle(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]]
        argument2 = {'x': 0, 'y': 2}
        actual = check_if_exit_reached(argument1, argument2)
        expected = False
        self.assertEqual(expected, actual)

    def test_board_end(self):
        argument1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]]
        argument2 = {'x': 0, 'y': 4}
        actual = check_if_exit_reached(argument1, argument2)
        expected = True
        self.assertEqual(expected, actual)
