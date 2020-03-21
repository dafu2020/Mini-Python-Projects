from unittest import TestCase
import unittest.mock
import io
import file_io


class Test(TestCase):
    def test_empty_filename(self):
        argument = ''
        with self.assertRaises(FileNotFoundError):
            file_io.top_ten_words(argument)

    def test_wrong_filename(self):
        argument = 'this_is_not_existed.txt'
        with self.assertRaises(FileNotFoundError):
            file_io.top_ten_words(argument)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_alice(self, mock_stdout):
        file_name = 'alice.txt'
        file_io.top_ten_words(file_name)
        expected = 'the - 1804\nand - 912\nto - 797\na - 684\nof - 622\nshe - 538\nit - 529\nsaid - 462\n' \
                   'in - 425\nyou - 418\n'
        self.assertEqual(mock_stdout.getvalue(), expected)
