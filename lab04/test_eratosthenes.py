from unittest import TestCase
import lab04


class Test(TestCase):
    def test_eratosthenes_zero(self):
        """Test number zero as the upperbound."""
        argument = 0
        expected = []
        lab04.eratosthenes(argument)
        self.assertEqual(expected, lab04.eratosthenes(argument), "The upperbound number is zero.")

    def test_eratosthenes_one(self):
        """Test the smallest positive integer, one as the upperbound."""
        argument = 1
        expected = []
        lab04.eratosthenes(argument)
        self.assertEqual(expected, lab04.eratosthenes(argument),
                         "The upperbound number is the smallest positive integer, one. ")

    def test_eratosthenes_smallest_upperbound(self):
        """Test number two, the upperbound number is the smallest prime number. """
        argument = 2
        expected = [2]
        lab04.eratosthenes(argument)
        self.assertEqual(expected, lab04.eratosthenes(argument),
                         "The upperbound number is the smallest prime number. ")

    def test_eratosthenes_prime_upperbound(self):
        """Test number thirty one, the upper-bond number that is a primer number."""
        argument = 31
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        lab04.eratosthenes(argument)
        self.assertEqual(expected, lab04.eratosthenes(argument),
                         "The upperbound number is a prime number.")

    def test_eratosthenes_non_prime_upperbound(self):
        """Test number one hundred, the upper-bond number that is a non-primer number."""
        argument = 100
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        lab04.eratosthenes(argument)
        self.assertEqual(expected, lab04.eratosthenes(argument), "The upperbound number is a non-primer number.")
