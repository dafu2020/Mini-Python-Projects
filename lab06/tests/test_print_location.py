"""
Demonstrated unit tests for print_location function
"""
from unittest import TestCase
from lab06.maze import print_location
from unittest.mock import patch
import io


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_location_beginning_of_the_board(self, mock_stdout):
        argument = {'x': 0, 'y': 0}
        print_location(argument)
        expected = (' $ . . . .\n'
                    ' . . . . .\n'
                    ' . . . . .\n'
                    ' . . . . .\n'
                    ' . . . . .\n')
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_location_middle_of_the_board(self, mock_stdout):
        argument = {'x': 2, 'y': 2}
        print_location(argument)
        expected = (' . . . . .\n'
                    ' . . . . .\n'
                    ' . . $ . .\n'
                    ' . . . . .\n'
                    ' . . . . .\n')
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_location_end_of_the_board(self, mock_stdout):
        argument = {'x': 4, 'y': 4}
        print_location(argument)
        expected = (' . . . . .\n'
                    ' . . . . .\n'
                    ' . . . . .\n'
                    ' . . . . .\n'
                    ' . . . . $\n')
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)