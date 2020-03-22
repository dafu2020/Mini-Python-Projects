from unittest import TestCase
import file_io


class Test(TestCase):
    def test_empty_text(self):
        argument = ''
        actual = file_io.format_text(argument)
        expected = []
        self.assertEqual(actual, expected)

    def test_one_word_text(self):
        argument = 'one'
        actual = file_io.format_text(argument)
        expected = ['one']
        self.assertEqual(actual, expected)

    def test_multi_words_text(self):
        argument = 'this txt here is used for unittest purpose'
        actual = file_io.format_text(argument)
        expected = ['this', 'txt', 'here', 'is', 'used', 'for', 'unittest', 'purpose']
        self.assertEqual(actual, expected)

    def test_multi_words_text_repeat(self):
        argument = 'this txt here is used for unittest purpose this txt here is used for unittest purpose'
        actual = file_io.format_text(argument)
        expected = ['this', 'txt', 'here', 'is', 'used', 'for', 'unittest', 'purpose', 'this', 'txt', 'here', 'is',
                    'used', 'for', 'unittest', 'purpose']
        self.assertEqual(actual, expected)
