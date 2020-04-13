"""
Demonstrate the unit-test for Country object
"""
import unittest.mock
import io
from unittest import TestCase
from country import Country


class TestCountry(TestCase):

    def setUp(self):
        """Setup two Country objects"""
        self.test_country_1 = Country('Country_one', 100, 1000)
        self.test_country_2 = Country("Country_two", 50, 100)

    def test___init___name_empty(self):
        with self.assertRaises(ValueError):
            self.country_fail = Country('', 10, 100)

    def test___init___name_population_negative(self):
        with self.assertRaises(ValueError):
            self.country_fail = Country('country_fail', -1, 100)

    def test___init___name_population_zero(self):
        with self.assertRaises(ValueError):
            self.country_fail = Country('country_fail', 0, 100)

    def test___init___name_area_negative(self):
        with self.assertRaises(ValueError):
            self.country_fail = Country('country_fail', 100, -1)

    def test___init___name_area_zero(self):
        with self.assertRaises(ValueError):
            self.country_fail = Country('country_fail', 100, 0)

    def test_is_larger(self):
        """Test the is_larger function with existed countries"""
        expected = True
        actual = self.test_country_1.is_larger(self.test_country_2)
        self.assertEqual(expected, actual)

    def test_is_larger_non_exist_country(self):
        """Test the is_larger function with non-existed country"""
        with self.assertRaises(AttributeError):
            self.test_country_3.is_larger(self.test_country_2)

    def test_population_density(self):
        """Test the population_density() function with an existed Country"""
        expected = 0.1
        actual = self.test_country_1.population_density()
        self.assertEqual(expected, actual)

    def test_population_density_non_exist_country(self):
        """Test the population_density function with non-existed Country object"""
        with self.assertRaises(AttributeError):
            self.test_country_3.population_density(self)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test___str__(self, mock_stdout):
        """Test print an existed Country"""
        expected = 'Country_One has a population of 100 and is 1000 square kilometres.\n'
        print(self.test_country_1)
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test___str___non_existed_Country(self):
        """Test print a Country that is not existed"""
        with self.assertRaises(AttributeError):
            print(self.test_country_3)

    def test___repr__(self):
        """Test the repr of an existed Country object"""
        expected = 'Country(\"Country_One\", 100, 1000)'
        actual = repr(self.test_country_1)
        self.assertEqual(expected, actual)

    def test___repr___Country_non_existed(self):
        """Test the repr of a non-existed Country object"""
        with self.assertRaises(AttributeError):
            repr(self.test_country_3)

    def test___repr__in_list(self):
        """Test the repr of an existed Country object in a list"""
        expected = ['Country(\"Country_One\", 100, 1000)']
        actual = [repr(self.test_country_1)]
        self.assertEqual(expected, actual)

    def test___repr__in_list_non_existed(self):
        """Test the repr of a non-existed object in a list"""
        with self.assertRaises(AttributeError):
            repr(self.test_country_3)
