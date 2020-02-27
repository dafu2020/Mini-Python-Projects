"""
Demonstrate the unittests for sparse_dot_product
"""
from unittest import TestCase
import sparse_vector


class Test(TestCase):
    def test_empty_sparse_vector(self):
        """Test two empty sparse vectors"""
        argument_one = {'length': 0}
        argument_two = {'length': 0}
        expected = 0
        actual: dict = sparse_vector.sparse_dot_product(argument_one, argument_two)
        self.assertEqual(expected, actual,)

    def test_length_one_same_integer_positive(self):
        """Test two length one sparse vectors with same positive integer elements"""
        argument_one = {0: 1, 'length': 1}
        argument_two = {0: 1, 'length': 1}
        expected = 1
        actual: dict = sparse_vector.sparse_dot_product(argument_one, argument_two)
        self.assertEqual(expected, actual)

    def test_length_one_same_integer_negative(self):
        """Test two length one sparse vectors with same negative integer elements"""
        argument_one = {0: -1, 'length': 1}
        argument_two = {0: -1, 'length': 1}
        expected = 1
        actual: dict = sparse_vector.sparse_dot_product(argument_one, argument_two)
        self.assertEqual(expected, actual)

    def test_length_one_integer_pos_neg(self):
        """Test two length one sparse vectors with elements added to zero"""
        argument_one = {0: 1, 'length': 1}
        argument_two = {0: -1, 'length': 1}
        expected = -1
        actual: dict = sparse_vector.sparse_dot_product(argument_one, argument_two)
        self.assertEqual(expected, actual)

    def test_length_one_same_floating_point(self):
        """Test two length one vectors with same floating point elements"""
        argument_one = {0: 0.1, 'length': 1}
        argument_two = {0: 0.1, 'length': 1}
        expected = 0.010000000000000002
        actual: dict = sparse_vector.sparse_dot_product(argument_one, argument_two)
        self.assertEqual(expected, actual)

    def test_length_one_integer_and_floating_point(self):
        """Test two length one vectors with floating point and integer"""
        argument_one = {0: 1, 'length': 1}
        argument_two = {0: 0.1, 'length': 1}
        expected = 0.1
        actual: dict = sparse_vector.sparse_dot_product(argument_one, argument_two)
        self.assertEqual(expected, actual)

    def test_unique_key(self):
        """Test two length one vectors with different index elements"""
        argument_one = {1: 1, 'length': 2}
        argument_two = {0: 2, 'length': 2}
        expected = 0
        actual: dict = sparse_vector.sparse_dot_product(argument_one, argument_two)
        self.assertEqual(expected, actual)

    def test_mixture_key(self):
        """Test two length one vectors with different properties of the elements"""
        argument_one = {0: 1, 1: -0.2, 2: -1, 'length': 3}
        argument_two = {0: 2, 2: 9, 'length': 3}
        expected = -7
        actual: dict = sparse_vector.sparse_dot_product(argument_one, argument_two)
        self.assertEqual(expected, actual)