import unittest.mock  # NEW
import io  # NEW
from unittest import TestCase
from unittest.mock import patch
import dnd


class Test(TestCase):
    @patch('random.choice', side_effect=['g', 'a', 'f', 'a', 'g', 'e'])
    def test_ask_for_value_and_convert_to_lower(self, mock_input):
        arguemrnt = 3
        actual = dnd.generate_name(arguemrnt)
        expected = "gafage"
        self.assertEqual(expected, actual)
