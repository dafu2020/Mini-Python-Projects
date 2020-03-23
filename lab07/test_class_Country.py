"""
Demonstrate the unit-test for Country object
"""
import unittest.mock
import io
from unittest import TestCase
from country import Country


class TestCountry(TestCase):

    def setUp(self):
        self.test_country_1 = Country('Country_one', 100, 1000)
        self.test_country_2 = Country("Country_two", 50, 100)

    def test_is_larger(self):
        expected = True
        actual = self.test_country_1.is_larger(self.test_country_2)
        self.assertEqual(expected, actual)

    def test_population_density(self):
        expected = 0.1
        actual = self.test_country_1.population_density()
        self.assertEqual(expected, actual)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test___str__(self, mock_stdout):
        expected = 'Country_one has a population of 100 and is 1000 square kilometres.\n'
        print(self.test_country_1)
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test___repr__(self):
        expected = 'Country(\"Country_one\", 100, 1000)'
        actual = self.test_country_1.__repr__()
        self.assertEqual(expected, actual)

    def test___repr__in_list(self):
        expected = ['Country(\"Country_one\", 100, 1000)']
        actual = [self.test_country_1.__repr__()]
        self.assertEqual(expected, actual)



