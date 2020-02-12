from unittest import TestCase
from unittest.mock import patch
import dnd


class Test(TestCase):
    def test_roll_one_sided_die_once(self):
        expected = 1
        actual = dnd.roll_die(1, 1)
        self.assertEqual(expected, actual)

    def test_roll_six_sided_die_once(self):
        actual = dnd.roll_die(1, 6)
        self.assertGreaterEqual(actual, 1)
        self.assertLessEqual(actual, 6)

    def test_roll_six_sided_die_twice(self):
        actual = dnd.roll_die(2, 6)
        self.assertGreaterEqual(actual, 2)
        self.assertLessEqual(actual, 12)

    def test_roll_ten_sided_die_ten_times(self):
        actual = dnd.roll_die(10, 10)
        self.assertGreaterEqual(actual, 10)
        self.assertLessEqual(actual, 100)

    @patch('random.randint', side_effect=[3, 3])
    def test_roll_die_single_roll_two_times(self, mock_randint):
        actual = dnd.roll_die(2, 3)
        self.assertEqual(actual, 6)

    @patch('random.randint', side_effect=[3, 3, 3])
    def test_roll_die_single_roll_three_times(self, mock_randint):
        actual = dnd.roll_die(3, 3)
        self.assertEqual(actual, 9)

    @patch('random.randint', side_effect=[3, 2, 1])
    def test_roll_die_single_roll_three_times_different_value(self, mock_randint):
        actual = dnd.roll_die(3, 3)
        self.assertEqual(actual, 6)


