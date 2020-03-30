from unittest import TestCase

from regular_expressions import is_nakamoto


class Test(TestCase):
    def test_empty(self):
        argument = ''
        actual = is_nakamoto(argument)
        expect = False
        self.assertEqual(expect, actual)

    def test_whitespace(self):
        argument = ' '
        actual = is_nakamoto(argument)
        expect = False
        self.assertEqual(expect, actual)

    def test_size_1_character(self):
        argument = '1'
        actual = is_nakamoto(argument)
        expect = False
        self.assertEqual(expect, actual)

    def test_valid_name(self):
        argument = 'Alice Nakamoto'
        actual = is_nakamoto(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_first_name_not_capitalized(self):
        argument = 'satoshi Nakamoto'
        actual = is_nakamoto(argument)
        expect = False
        self.assertEqual(expect, actual)

    def test_contain_non_letter_character(self):
        argument = 'Mr. Nakamoto'
        actual = is_nakamoto(argument)
        expect = False
        self.assertEqual(expect, actual)

    def test_no_first_name(self):
        argument = 'Nakamoto'
        actual = is_nakamoto(argument)
        expect = False
        self.assertEqual(expect, actual)

    def test_Nakamoto_not_capitalized(self):
        argument = 'Satoshi nakamoto'
        actual = is_nakamoto(argument)
        expect = False
        self.assertEqual(expect, actual)