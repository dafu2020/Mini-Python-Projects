from unittest import TestCase
import file_io


class Test(TestCase):
    def test_empty_filename(self):
        argument = ''
        with self.assertRaises(FileNotFoundError):
            file_io.open_text(argument)

    def test_wrong_filename(self):
        argument = 'this_is_not_existed.txt'
        with self.assertRaises(FileNotFoundError):
            file_io.open_text(argument)

    def test_right_file(self):
        file_name = 'doctest_1.txt'
        actual = file_io.open_text(file_name)
        expected = 'this file is for the purpose of doctest:'
        self.assertEqual(actual, expected)
