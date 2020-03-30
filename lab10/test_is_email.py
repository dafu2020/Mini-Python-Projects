from unittest import TestCase
from regular_expressions import is_email


class Test(TestCase):
    def test_username_0_character(self):
        argument = '@email.com'
        actual = is_email(argument)
        expect = False
        self.assertEqual(expect, actual)

    def test_username_1_character_number(self):
        argument = '1@email.com'
        actual = is_email(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_username_more_than_1_character_number(self):
        argument = '123@email.com'
        actual = is_email(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_username_1_character_letter(self):
        argument = 'a@email.com'
        actual = is_email(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_username_more_than_1_character_letter(self):
        argument = 'abc@email.com'
        actual = is_email(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_username_1_character_underscore(self):
        argument = '_@email.com'
        actual = is_email(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_username_more_than_1_character_underscore(self):
        argument = '___@email.com'
        actual = is_email(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_username_more_than_1_character_mix(self):
        argument = 'l_1@email.com'
        actual = is_email(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_username_more_than_1_character_mix_contain_other_character(self):
        argument = 'l._1@email.com'
        actual = is_email(argument)
        expect = False
        self.assertEqual(expect, actual)

    def test_has_one_at(self):
        argument = 'username@email.com'
        actual = is_email(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_one_than_one_at(self):
        argument = 'username@@email.com'
        actual = is_email(argument)
        expect = False
        self.assertEqual(expect, actual)

    def test_no_at(self):
        argument = 'usernameemail.com'
        actual = is_email(argument)
        expect = False
        self.assertEqual(expect, actual)

    def test_0_domain(self):
        argument = 'username@.com'
        actual = is_email(argument)
        expect = False
        self.assertEqual(expect, actual)

    def test_0_domain_space(self):
        argument = 'username@ .com'
        actual = is_email(argument)
        expect = False
        self.assertEqual(expect, actual)

    def test_domain_1_character_letter_lowercase(self):
        argument = 'username@l.com'
        actual = is_email(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_domain_1_character_letter_uppercase(self):
        argument = 'username@U.com'
        actual = is_email(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_domain_1_character_number(self):
        argument = 'username@1.com'
        actual = is_email(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_domain_more_than_1_character_number(self):
        argument = 'username@1234.com'
        actual = is_email(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_domain_more_than_1_character_letter(self):
        argument = 'username@hotMail.com'
        actual = is_email(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_domain_more_than_1_character_mix(self):
        argument = 'username@139mail.com'
        actual = is_email(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_domain_more_than_1_character_mix_containing_underscore(self):
        argument = 'username@139_mail.com'
        actual = is_email(argument)
        expect = False
        self.assertEqual(expect, actual)

    def test_domain_more_than_1_character_mix_containing_other_characters(self):
        argument = 'username@139*#mail.com'
        actual = is_email(argument)
        expect = False
        self.assertEqual(expect, actual)

    def test_has_dot_before_dot_com(self):
        argument = 'username@139mail.com'
        actual = is_email(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_has_dots_before_dot_com(self):
        argument = 'username@139mail..com'
        actual = is_email(argument)
        expect = False
        self.assertEqual(expect, actual)

    def test_dot_com_0_character(self):
        argument = 'username@139mail.'
        actual = is_email(argument)
        expect = False
        self.assertEqual(expect, actual)

    def test_dot_com_1_character(self):
        argument = 'username@139mail.1'
        actual = is_email(argument)
        expect = False
        self.assertEqual(expect, actual)

    def test_dot_com_2_characters(self):
        argument = 'username@139mail.1l'
        actual = is_email(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_dot_com_3_characters(self):
        argument = 'username@139mail.1l_'
        actual = is_email(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_dot_com_4_characters(self):
        argument = 'username@139mail.1l__'
        actual = is_email(argument)
        expect = True
        self.assertEqual(expect, actual)

    def test_dot_com_more_than_4_characters(self):
        argument = 'username@139mail.case12'
        actual = is_email(argument)
        expect = False
        self.assertEqual(expect, actual)

    def test_dot_com_more_than_4_characters_contain_dot_characters(self):
        argument = 'username@139mail.i.2'
        actual = is_email(argument)
        expect = False
        self.assertEqual(expect, actual)

    def test_dot_contain_underscore(self):
        argument = 'username@139mail.1_2'
        actual = is_email(argument)
        expect = True
        self.assertEqual(expect, actual)
