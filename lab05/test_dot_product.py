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
        expected = None
        actual: dict = sparse_vector.sparse_dot_product(argument_one, argument_two)
        self.assertEqual(expected, actual, )

    def test_length_one_zero_sparse_vector(self):
        """Test two length one sparse vectors contains zero"""
        argument_one = {'length': 1}
        argument_two = {'length': 1}
        expected = 0
        actual: dict = sparse_vector.sparse_dot_product(argument_one, argument_two)
        self.assertEqual(expected, actual)

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
        """Test two length one sparse vectors with elements include both positive and negative integers"""
        argument_one = {0: 1, 'length': 1}
        argument_two = {0: -1, 'length': 1}
        expected = -1
        actual: dict = sparse_vector.sparse_dot_product(argument_one, argument_two)
        self.assertEqual(expected, actual)

    def test_length_more_than_one_same_position_same_integer(self):
        """Test two length more than one sparse vector with elements that are at same position and same integer"""
        argument_one = {0: 1, 1: 2, 2: 1, 'length': 3}
        argument_two = {0: 1, 1: 2, 2: 1, 'length': 3}
        expected = 6
        actual: dict = sparse_vector.sparse_dot_product(argument_one, argument_two)
        self.assertEqual(expected, actual)

    def test_length_more_than_one_same_position_different_integer(self):
        """Test two length more than one sparse vector with elements that are at same position and different integer"""
        argument_one = {0: 1, 1: 2, 2: 3, 'length': 3}
        argument_two = {0: -1, 1: -2, 2: -3, 'length': 3}
        expected = -14
        actual: dict = sparse_vector.sparse_dot_product(argument_one, argument_two)
        self.assertEqual(expected, actual)

    def test_length_more_than_one_different_position(self):
        """"Test two length more than one sparse vector with elements that are integers at different position"""
        argument_one = {1: 1, 2: 3, 'length': 3}
        argument_two = {0: 2, 'length': 3}
        expected = 0
        actual: dict = sparse_vector.sparse_dot_product(argument_one, argument_two)
        self.assertEqual(expected, actual)

    def test_length_more_than_one_mixture(self):
        """Test two length one vectors with different properties of the elements"""
        argument_one = {0: 1, 1: -2, 2: -1, 3: -1, 'length': 3}
        argument_two = {0: 2, 2: -9, 3: 6, 'length': 3}
        expected = 5
        actual: dict = sparse_vector.sparse_dot_product(argument_one, argument_two)
        self.assertEqual(expected, actual)
