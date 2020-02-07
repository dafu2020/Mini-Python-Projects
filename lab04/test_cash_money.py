from unittest import TestCase
import lab04


class Test(TestCase):
    def test_cash_money_zero(self):
        """Test the value 0.00"""
        argument = 0.00
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        lab04.cash_money(argument)
        self.assertEqual(expected, lab04.cash_money(argument),
                         "The number is zero")

    def test_cash_money_penny(self):
        """Test a penny"""
        argument = 0.01
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        lab04.cash_money(0.01)
        self.assertEqual(expected, lab04.cash_money(argument),
                         "The number is a penny.")

    def test_cash_money_two_pennies(self):
        """Test the two pennies"""
        argument = 0.02
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]
        lab04.cash_money(argument)
        self.assertEqual(expected, lab04.cash_money(argument),
                         "The number is two pennie.")

    def test_cash_money_nickle(self):
        """Test a nickle"""
        argument = 0.05
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        lab04.cash_money(argument)
        self.assertEqual(expected, lab04.cash_money(argument),
                         "The number is a nickle.")

    def test_cash_money_dime(self):
        """Test a dime"""
        argument = 0.10
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
        lab04.cash_money(argument)
        self.assertEqual(expected, lab04.cash_money(argument),
                         "The number is a dime")

    def test_cash_money_quarter(self):
        """Test a quarter"""
        argument = 0.25
        expected = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
        lab04.cash_money(argument)
        self.assertEqual(expected, lab04.cash_money(argument),
                         "The number is a quarter")

    def test_cash_money_loonie(self):
        """Test a loonie"""
        argument = 1.00
        expected = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        lab04.cash_money(argument)
        self.assertEqual(expected, lab04.cash_money(argument),
                         "The number is a loonie")

    def test_cash_money_loonie_and_dime(self):
        """Test a loonie and a dime """
        argument = 1.05
        expected = [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]
        lab04.cash_money(argument)
        self.assertEqual(expected, lab04.cash_money(argument),
                         "The number is a loonie and a dime")

    def test_cash_money_toonie(self):
        """Test a loonie"""
        argument = 2.00
        expected = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        lab04.cash_money(argument)
        self.assertEqual(expected, lab04.cash_money(argument),
                         "The number is toonie")

    def test_cash_money_fin(self):
        """Test a fin"""
        argument = 5.00
        expected = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        lab04.cash_money(argument)
        self.assertEqual(expected, lab04.cash_money(argument),
                         "The number is a fin")

    def test_cash_money_ten_bucks(self):
        """Test a ten dollar bill"""
        argument = 10.00
        expected = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        lab04.cash_money(argument)
        self.assertEqual(expected, lab04.cash_money(argument),
                         "The number is a ten dollar bill")

    def test_cash_money_ten_bucks_and_twenty_seven_cents(self):
        """Test a ten dollar bill and twenty-seven cents"""
        argument = 10.27
        expected = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 2]
        lab04.cash_money(argument)
        self.assertEqual(expected, lab04.cash_money(argument),
                         "The number is a ten dollar bill and twenty-seven cents")

    def test_cash_money_twenty_bucks(self):
        """Test a twenty dollar bill"""
        argument = 20.00
        expected = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        lab04.cash_money(argument)
        self.assertEqual(expected, lab04.cash_money(argument),
                         "The number is a twenty dollar bill")

    def test_cash_money_fifty_bucks(self):
        """Test a fifty dollar bill"""
        argument = 50.00
        expected = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        lab04.cash_money(argument)
        self.assertEqual(expected, lab04.cash_money(argument),
                         "The number is a fifty dollar bill")

    def test_cash_money_one_hundred_bucks(self):
        """Test a one hundred dollar bill"""
        argument = 100.00
        expected = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        lab04.cash_money(argument)
        self.assertEqual(expected, lab04.cash_money(argument),
                         "The number is a one hundred dollar bill")

    def test_cash_money_one_hundred_bucks_and_fifty_seven_cents(self):
        """Test a one hundred dollar bill and fifty seven cents"""
        argument = 100.57
        expected = [1, 0, 0, 0, 0, 0, 0, 2, 0, 1, 2]
        lab04.cash_money(argument)
        self.assertEqual(expected, lab04.cash_money(argument),
                         "The number is one hundred dollar bill and fifty seven cents")

    def test_cash_money_one_hundred_eighty_eight_bucks_and_forty_one_cents(self):
        """Test the one hundred eighty eight dollar bills and forty one cents"""
        argument = 188.41
        expected = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        lab04.cash_money(argument)
        self.assertEqual(expected, lab04.cash_money(argument),
                         "The number is a one hundred eighty eight dollar bills and forty one cents")
