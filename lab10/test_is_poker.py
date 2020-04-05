from unittest import TestCase
from regular_expressions import is_poker


class Test(TestCase):
    def test_is_invalid_zero_length_str(self):
        argument = ''
        actual = is_poker(argument)
        expect = False
        self.assertEqual(expect, actual)

    def test_is_invalid_length_one_str(self):
        argument = 'a'
        actual = is_poker(argument)
        expect = False
        self.assertEqual(expect, actual)

    def test_is_four_kind_invalid_card(self):
        argument = 'jjjjk'
        actual = is_poker(argument)
        expect = False
        self.assertEqual(expect, actual)

    def test_is_four_kind_all_letter(self):
        argument = 'aaaak'
        actual = is_poker(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_is_four_kind_letter_and_number(self):
        argument = 'tttt9'
        actual = is_poker(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_is_four_kind_all_number(self):
        argument = '99998'
        actual = is_poker(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_is_full_house_invalid_card(self):
        argument = 'jjjtt'
        actual = is_poker(argument)
        expect = False
        self.assertEqual(expect, actual)

    def test_is_full_house_all_letter(self):
        argument = 'aaakk'
        actual = is_poker(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_is_full_house_letter_and_number(self):
        argument = 'ttt99'
        actual = is_poker(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_is_full_house_all_number(self):
        argument = '99988'
        actual = is_poker(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_is_full_house_letter_and_number(self):
        argument = '222aa'
        actual = is_poker(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_is_straight_invalid_card(self):
        argument = 'akqjt'
        actual = is_poker(argument)
        expect = False
        self.assertEqual(expect, actual)

    def test_is_straight_all_number(self):
        argument = '87654'
        actual = is_poker(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_is_straight_number_and_letter(self):
        argument = '5432a'
        actual = is_poker(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_is_3_kind_invalid_card(self):
        argument = 'kkkaj'
        actual = is_poker(argument)
        expect = False
        self.assertEqual(expect, actual)

    def test_is_3_kind_all_letter(self):
        argument = 'kkkaq'
        actual = is_poker(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_is_3_kind_all_number(self):
        argument = '99987'
        actual = is_poker(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_is_3_kind_number_and_letter(self):
        argument = 'ttt98'
        actual = is_poker(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_is_2_pair_invalid_card(self):
        argument = 'kkjjq'
        actual = is_poker(argument)
        expect = False
        self.assertEqual(expect, actual)

    def test_is_2_pair_all_letter(self):
        argument = 'aaqqk'
        actual = is_poker(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_is_2_pair_all_number(self):
        argument = '99662'
        actual = is_poker(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_is_2_pair_number_and_letter(self):
        argument = 'tt889'
        actual = is_poker(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_is_pair_invalid_card(self):
        argument = 'qqatj'
        actual = is_poker(argument)
        expect = False
        self.assertEqual(expect, actual)

    def test_is_pair_all_letter(self):
        argument = 'aaqtk'
        actual = is_poker(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_is_pair_all_number(self):
        argument = '99673'
        actual = is_poker(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_is_pair_number_and_letter(self):
        argument = '223ka'
        actual = is_poker(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_is_high_invalid_card(self):
        argument = 'k4j9q'
        actual = is_poker(argument)
        expect = False
        self.assertEqual(expect, actual)

    def test_is_high_all_number(self):
        argument = '93784'
        actual = is_poker(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_is_high_number_and_letter(self):
        argument = 'a2qtk'
        actual = is_poker(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_is_invalid_less_than_5_card(self):
        argument = 'aaa'
        actual = is_poker(argument)
        expect = False
        self.assertEqual(expect, actual)

    def test_is_invalid_more_than_5_card(self):
        argument = 'aaaaaaaa'
        actual = is_poker(argument)
        expect = False
        self.assertEqual(expect, actual)

    def test_is_invalid_invalid_characters(self):
        argument = '(akqj'
        actual = is_poker(argument)
        expect = False
        self.assertEqual(expect, actual)
