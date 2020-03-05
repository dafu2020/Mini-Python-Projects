"""
Demonstrated unit tests for make_character function
"""
from unittest import TestCase
from lab06.maze import make_character


class Test(TestCase):
    def test_make_character(self):
        expected = {'x': 0, 'y': 0}
        actual = make_character()
        self.assertEqual(expected, actual)
