"""
Demonstrate the unittests for Tree object
"""
from unittest import TestCase
import unittest.mock
import io
from tree import Tree


class TestTree(TestCase):

    def setUp(self):
        """Setup two Tree objects"""
        self.test_tree_1 = Tree('Osmanthus fragrans', 12, 20.0)
        self.test_tree_2 = Tree('Douglas fir', 1, 10.0)

    def test___init___species_empty(self):
        """test __init__ with a empty str as the species name"""
        with self.assertRaises(ValueError):
            self.tree_fail = Tree('', 12, 20.0)

    def test___init___species_white_space(self):
        """test __init__ with a str of all white-space as the species name"""
        with self.assertRaises(ValueError):
            self.tree_fail = Tree(' ', 12, 20.0)

    def test___init___age_negative(self):
        """test __init__ with a negative int as the species age"""
        with self.assertRaises(ValueError):
            self.tree_fail = Tree('Osmanthus fragrans', -1, 20.0)

    def test___init___trunk_circumference_negative(self):
        with self.assertRaises(ValueError):
            self.tree_fail = Tree('Osmanthus fragrans', 12, -2)

    def test_get_species(self):
        """Test get the species name of a Tree"""
        expected = "Osmanthus Fragrans"
        actual = self.test_tree_1.get_species()
        self.assertEqual(expected, actual)

    def test_get_age(self):
        """Test get the age of a Tree"""
        expected = 12
        actual = self.test_tree_1.get_age()
        self.assertEqual(expected, actual)

    def test_get_trunk_circumference(self):
        """Test get the trunk circumference of a Tree"""
        expected = 20.0
        actual = self.test_tree_1.get_trunk_circumference()
        self.assertEqual(expected, actual)

    def test_update_age(self):
        """Test update the age of the Tree with a positive int"""
        argument = 12
        expected = 12
        self.test_tree_1.update_age(argument)
        actual = self.test_tree_1.get_age()
        self.assertEqual(expected, actual)

    def test_update_age_negative(self):
        """Test update the age of the Tree with a negative int"""
        argument = -1
        with self.assertRaises(ValueError):
            self.tree_fail = self.test_tree_1.update_age(argument)

    def test_update_trunk_circumference(self):
        """Test update the trunk circumference of the Tree with a positive float"""
        argument = 15.0
        expected = 15.0
        self.test_tree_1.update_trunk_circumference(argument)
        actual = self.test_tree_1.get_trunk_circumference()
        self.assertEqual(expected, actual)

    def test_update_age_negative(self):
        """Test update the trunk circumference of the Tree with a negative float"""
        argument = -1
        with self.assertRaises(ValueError):
            self.tree_fail = self.test_tree_1.update_trunk_circumference(argument)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test___str__(self, mock_stdout):
        """Test print an existed Tree"""
        expected = 'Osmanthus Fragrans is 12 year(s) old, has a trunk circumference of 20.0 centimetres.\n'
        print(self.test_tree_1)
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test___str___non_existed_Tree(self):
        """Test print a Tree that is not existed"""
        with self.assertRaises(AttributeError):
            print(self.test_tree_3)

    def test___repr__(self):
        """Test the repr of an existed Tree object"""
        expected = 'Tree("Osmanthus Fragrans", 12, 20.0)'
        actual = repr(self.test_tree_1)
        self.assertEqual(expected, actual)

    def test___str___non_existed_Tree(self):
        """Test the repr of an un-existed Tree object"""
        with self.assertRaises(AttributeError):
            repr(self.test_tree_3)
