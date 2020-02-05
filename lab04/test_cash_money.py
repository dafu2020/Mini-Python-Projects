from unittest import TestCase
import lab04


class Test(TestCase):

    def test_cash_money_smallest(self):
        """Test the smallest float"""
        argument = 0.01
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        lab04.cash_money(argument)
        self.assertEqual(expected, lab04.cash_money(argument),
                         "The number is the smallest positive two decimal place float.")

    def test_cash_money_less_then_50(self):
        """Test the float less than 50"""
        argument = 15.32
        expected = [0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 2]
        lab04.cash_money(argument)
        self.assertEqual(expected, lab04.cash_money(argument),
                         "The number is a float number between 0.01 to 50.00.")

    def test_cash_money_less_than_100(self):
        """Test the float less than 100"""
        argument = 66.53
        expected = [0, 1, 0, 1, 1, 0, 1, 2, 0, 0, 3]
        lab04.cash_money(argument)
        self.assertEqual(expected, lab04.cash_money(argument),
                         "The number is a float number between 50.00 to 100.00.")

    def test_cash_money_larger_than_100(self):
        """Test the float larger than 100"""
        argument = 99999.99
        expected = [999, 1, 2, 0, 1, 2, 0, 3, 2, 0, 4]
        lab04.cash_money(argument)
        self.assertEqual(expected, lab04.cash_money(argument),
                         "The number is a float number larger than 100.00.")
