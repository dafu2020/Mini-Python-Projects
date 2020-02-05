from unittest import TestCase
import lab04


class Test(TestCase):
    def test_eratosthenes_smallest(self):
        """Test the smallest integer"""
        argument = 1
        expected = []
        lab04.eratosthenes(argument)
        self.assertEqual(expected, lab04.eratosthenes(argument),
                         "The number is the smallest positive integer.")

    def test_cash_money_less_then_10(self):
        """Test the positive integer less than 10"""
        argument = 8
        expected = [2, 3, 5, 7]
        lab04.eratosthenes(argument)
        self.assertEqual(expected, lab04.eratosthenes(argument),
                         "The number is a positive number between 1 - 10.")

    def test_cash_money_less_then_100(self):
        """Test the positive integer less than 100"""
        argument = 50
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        lab04.eratosthenes(argument)
        self.assertEqual(expected, lab04.eratosthenes(argument),
                         "The number is a positive number between 10 - 100.")

    def test_cash_money_less_then_1000(self):
        """Test the positive integer less than 1000"""
        argument = 501
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                    103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                    211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
                    331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
                    449, 457, 461, 463, 467, 479, 487, 491, 499]
        lab04.eratosthenes(argument)
        self.assertEqual(expected, lab04.eratosthenes(argument),
                         "The number is a positive number between 100 - 1000.")

    def test_cash_money_larger_then_1000(self):
        """Test the positive integer larger than 1000"""
        argument = 608
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                    103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                    211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
                    331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
                    449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577,
                    587, 593, 599, 601, 607]
        lab04.eratosthenes(argument)
        self.assertEqual(expected, lab04.eratosthenes(argument),
                         "The number is a positive number larger than 1000.")
