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

        def open_text(file_name: str) -> str:
            """Open and read file.

            :param file_name: a string
            :precondition: file_name must be a file
            :postcondition: open and read a file
            :return: file opens a str

            """
            # open file
            with open(file_name) as file_object:
                text = file_object.read()
            return text

        def format_text(text: str) -> str:
            """Format the text into individual words

            :param text: a string
            :precondition: file_name must be a file
            :postcondition: remove punctuation marks; convert all character into lowercase;
                            split the entire text into individual words
            :return: the formatted individual words as strings
            """
            # replace punctuation mark with ' '(space)
            for character in ',.~!@#$%^&*()_+-={}[]|/<>:\'\";':
                text = text.replace(character, '')
            text = text.lower()

            # get the individual words from the text
            word_in_text = text.split()

            return word_in_text

