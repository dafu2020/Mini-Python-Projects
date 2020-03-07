"""
Demonstrated unit tests for make_board function
"""
from unittest import TestCase
from lab06.maze import make_board


class Test(TestCase):
    def test_make_empty_board(self):
        argument = 0
        expected = []
        actual = make_board(argument)
        self.assertEqual(expected, actual)

    def test_make_1_by_1_board(self):
        argument = 1
        expected = [[0, 0]]
        actual = make_board(argument)
        self.assertEqual(expected, actual)

    def test_make_5_by_5_board(self):
        argument = 5
        expected = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                    [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                    [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                    [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                    [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        actual = make_board(argument)
        self.assertEqual(expected, actual)
