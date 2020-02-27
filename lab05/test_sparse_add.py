"""
Demonstrate the unittests for sparse_add
"""
from unittest import TestCase
import sparse_vector


class Test(TestCase):
    def test_empty_sparse_vector(self):
        """Test two empty sparse vectors"""
        argument_one = {'length': 0}
        argument_two = {'length': 0}
        expected = {'length': 0}
        actual: dict = sparse_vector.sparse_add(argument_one, argument_two)
        self.assertEqual(expected, actual, ' they are two empty vectors')

    def test_length_one_same_integer_positive(self):
        """Test two length one sparse vectors with same positive integer elements"""
        argument_one = {0: 1, 'length': 1}
        argument_two = {0: 1, 'length': 1}
        expected = {0: 2, 'length': 1}
        actual: dict = sparse_vector.sparse_add(argument_one, argument_two)
        self.assertEqual(expected, actual, ' they are two length one vectors with same positive integer elements')

    def test_length_one_same_integer_negative(self):
        """Test two length one sparse vectors with same negative integer elements"""
        argument_one = {0: -1, 'length': 1}
        argument_two = {0: -1, 'length': 1}
        expected = {0: -2, 'length': 1}
        actual: dict = sparse_vector.sparse_add(argument_one, argument_two)
        self.assertEqual(expected, actual, ' they are two length one vectors with same negative integer elements')

    def test_length_one_integer_pos_neg_add_to_zero(self):
        """Test two length one sparse vectors with elements added to zero"""
        argument_one = {0: 1, 'length': 1}
        argument_two = {0: -1, 'length': 1}
        expected = {'length': 1}
        actual: dict = sparse_vector.sparse_add(argument_one, argument_two)
        self.assertEqual(expected, actual, ' they are two length one vectors with integer elements added to zero')

    def test_length_one_integer_pos_neg_add_to_nonzero(self):
        """Test two length one sparse vectors with elements added to zero"""
        argument_one = {0: 2, 'length': 1}
        argument_two = {0: -1, 'length': 1}
        expected = {0: 1, 'length': 1}
        actual: dict = sparse_vector.sparse_add(argument_one, argument_two)
        self.assertEqual(expected, actual, ' they are two length one vectors with integer elements added to zero')

    def test_sparse_length_one_same_floating_point(self):
        """Test two length one vectors with same floating point elements"""
        argument_one = {0: 0.1, 'length': 1}
        argument_two = {0: 0.1, 'length': 1}
        expected = {0: 0.2, 'length': 1}
        actual: dict = sparse_vector.sparse_add(argument_one, argument_two)
        self.assertEqual(expected, actual, ' they are two length one vectors with same floating point elements')

    def test_sparse_length_one_floating_point_and_integer(self):
        """Test two length one vectors with same floating point elements"""
        argument_one = {0: 1, 'length': 1}
        argument_two = {0: 0.1, 'length': 1}
        expected = {0: 1.1, 'length': 1}
        actual: dict = sparse_vector.sparse_add(argument_one, argument_two)
        self.assertEqual(expected, actual, ' they are two length one vectors with same floating point elements')

    def test_length_more_than_one_same_integer_positive(self):
        """Test two length more than one sparse vectors with same positive integer elements"""
        argument_one = {0: 1, 1: 1, 'length': 3}
        argument_two = {0: 1, 1: 1, 'length': 3}
        expected = {0: 2, 1: 2, 'length': 3}
        actual: dict = sparse_vector.sparse_add(argument_one, argument_two)
        self.assertEqual(expected, actual)

    def test_length_more_than_one_different_integer_positive(self):
        """Test two length more than one sparse vectors with different positive integer elements"""
        argument_one = {1: 2, 'length': 3}
        argument_two = {0: 1, 1: 1, 'length': 3}
        expected = {0: 1, 1: 3, 'length': 3}
        actual: dict = sparse_vector.sparse_add(argument_one, argument_two)
        self.assertEqual(expected, actual)

    def test_length_more_than_one_different_integer_pos_and_neg(self):
        """Test two length more than one sparse vectors with different integer elements"""
        argument_one = {1: -2, 'length': 3}
        argument_two = {0: 1, 1: 1, 'length': 3}
        expected = {0: 1, 1: -1, 'length': 3}
        actual: dict = sparse_vector.sparse_add(argument_one, argument_two)
        self.assertEqual(expected, actual)

    def test_length_more_than_one_different_integer_pos_and_neg_add_to_zero(self):
        """Test two length more than one sparse vectors with different integer elements added to zero"""
        argument_one = {1: -2, 'length': 3}
        argument_two = {0: 1, 1: 2, 'length': 3}
        expected = {0: 1, 'length': 3}
        actual: dict = sparse_vector.sparse_add(argument_one, argument_two)
        self.assertEqual(expected, actual)

    def test_length_more_than_one_integer_and_floating_point(self):
        """Test two length more than one sparse vectors with different integer and floating points"""
        argument_one = {1: -2, 'length': 3}
        argument_two = {0: 1, 1: 2.0, 'length': 3}
        expected = {0: 1, 'length': 3}
        actual: dict = sparse_vector.sparse_add(argument_one, argument_two)
        self.assertEqual(expected, actual)

    def test_length_more_than_one_mixture(self):
        """Test two length more than one sparse vectors with different integer and floating points"""
        argument_one = {0: 1, 2: 1, 4: 2, 6: 1, 9: 1.34, 'length': 11}
        argument_two = {0: -1, 2: 2, 7: 3, 10: 4, 'length': 11}
        expected = {'length': 11, 2: 3, 4: 2, 6: 1, 9: 1.34, 7: 3, 10: 4}
        actual: dict = sparse_vector.sparse_add(argument_one, argument_two)
        self.assertEqual(expected, actual)
