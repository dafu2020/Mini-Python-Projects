import doctest


class Country:

    # construct a new Country
    def __init__(self, name: str, population: int, area: int):
        """
        Initialize a new Country.

        :param name: a string
        :param population: a positive integer
        :param area: a positive integer
        :precondition: name must be a string; population must be a positive integer; area must be a positive integer in
                        square kilometers.
        :postcondition: initialized Country as an object

        >>> doc_country_one = Country('Country_one', 100, 1000)

        >>> doc_country_two = Country('country_two', 2000, 40000)

        """
        # name the country
        if len(name) >= 0:
            self.name = name
        else:
            raise ValueError("Country name cannot be empty!")
        # set the population of the country
        if population > 0:
            self.population = population
        else:
            raise ValueError("population must be a whole number and above zero!")
        # set the area of the country
        if area > 0:
            self.area = area
        else:
            raise ValueError("area must be above zero!")

    # define a method called is_larger to compare area of two Country
    def is_larger(self, a_Country) -> bool:
        """Compare the area with another Country

        :param a_Country: a class object
        :precondition: a_Country must be a class object
        :postcondition: True if Country area is larger than a_Country area, else False
        :return: the boolean result

        >>> doc_country_one = Country('Country_one', 100, 1000)
        >>> doc_country_two = Country('country_two', 2000, 40000)
        >>> doc_country_one.is_larger(doc_country_two)
        False

        >>> doc_country_one = Country('Country_one', 100, 1000)
        >>> doc_country_two = Country('country_two', 2000, 40000)
        >>> doc_country_two.is_larger(doc_country_one)
        True
        """
        if self.area > a_Country.area:
            return True  # returns true if the object being asked to perform the comparison is larger
        else:
            return False  # else return false

    # define a method called population_density to calculate population density of a Country
    def population_density(self) -> float:
        """Calculate the population density of a Country

        :precondition: A Country must have a population attribute and an area attribute
        :postcondition: calculate the population density
        :return: the correctly calculated population density as a float

        >>> doc_country_one = Country('Country_one', 100, 1000)
        >>> doc_country_one.population_density()
        0.1

        >>> doc_country_two = Country('country_two', 2000, 40000)
        >>> doc_country_two.population_density()
        0.05
        """
        return self.population / self.area  # ppl density = people per square kilometre

    # define a method called __str__ for printing an object
    def __str__(self) -> str:
        """
        Return a informative representation of this Country for printing purpose.
        :precondition: a country class object must has the attributes of name, population, and area
        :postcondition: describe the informative representation of this Country for printing purpose
        :return: a description of this Country as a str

        >>> doc_country_one = Country('Country_one', 100, 1000)
        >>> print(doc_country_one)
        Country_one has a population of 100 and is 1000 square kilometres.

        >>> doc_country_two = Country('country_two', 2000, 40000)
        >>> print(doc_country_two)
        country_two has a population of 2000 and is 40000 square kilometres.
        """
        return str(self.name) + ' has a population of ' + str(self.population) + ' and is ' + str(self.area) \
               + ' square kilometres.'

    # define a method called __repr__ for Python to use when we ask for the value of a variable in the shell
    def __repr__(self) -> str:
        """
        Return an informative representation of this Country.
        :precondition: a country class object must has the attributes of name, population, and area
        :postcondition: describe the informative representation of this Country
        :return: a description of this Country as a str

        >>> doc_country_one = Country('Country_one', 100, 1000)
        >>> repr(doc_country_one)
        'Country("Country_one", 100, 1000)'

        >>> doc_country_two = Country('country_two', 2000, 40000)
        >>> repr(doc_country_two)
        'Country("country_two", 2000, 40000)'
        """
        return f'Country(\"{self.name}\", {self.population}, {self.area})'


def main():
    """
    Drive the program.
    """
    doctest.testmod()
    canada = Country('Canada', 37590000, 9985000)
    denmark = Country("Denmark", 5603000, 42933)

    try:
        print(canada.is_larger(denmark))
        print(canada.population_density())
        print(canada)
        print(repr(canada))
        print([canada])
    except ValueError:
        print('An error has occurred!')


if __name__ == "__main__":
    main()
