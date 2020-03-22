class Country:

    # construct a new Country
    def __init__(self, name, population, area):
        """
        Initialize a new Country.

        :param name: a string
        :param population: a positive integer
        :param area: a positive integer
        :precondition: name must be a string; population must be a positive integer; area must be a positive in
        :postcondition: initialized Country as a class object

        """
        self.name = name
        self.population = population
        self.area = area

    # define a method called is_larger to compare area of two Country
    def is_larger(self, Country) -> bool:
        """Compare the area with another Country

        :param Country: a class object
        :precondition: Country must be a class object
        :postcondition: conclude the boolean result of the comparision
        :return: the boolean result
        """
        if self.area > Country.area:
            return True  # returns true if the object being asked to perform the comparison is larger
        else:
            return False  # else return false

    # define a method called population_density to calculate population density of a Country
    def population_density(self) -> float:
        """Calculate the density of a Country

        :precondition: A Country must have a population attribute and an area attribute
        :postcondition: calculate the population density
        :return: the correctly calculated population density as a float
        """
        return self.population / self.area  # ppl density = people per square kilometre

    # define a method called __str__ for printing an object
    def __str__(self) -> str:
        """
        Return a informative representation of this Country for printing purpose.
        :precondition: a country class object must has the attributes of name, population, and area
        :postcondition: describe the informative representation of this Country for printing purpose
        :return: a description of this Country as a str
        :return:
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
        """
        return f'Country(\"{self.name}\", {self.population}, {self.area})'


def main():
    canada = Country('Canada', 37590000, 9985000)
    denmark = Country("Denmark", 5603000, 42933)

    print(canada.is_larger(denmark))
    print(canada.population_density())
    print(canada)
    print(canada.__repr__())
    print([canada])


if __name__ == "__main__":
    main()
