class Country:

    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def is_larger(self, Country):
        if self.area > Country.area:
            return True
        else:
            return False

    def population_density(self):
        return self.population / self.area

    def __str__(self):
        return str(self.name) + ' has a population of ' + str(self.population) + ' and is ' + str(self.area) \
               + ' square kilometres.'

    def __repr__(self):
        return f'Country(\"{self.name}\", {self.population}, {self.area})'


def main():
    canada = Country('Canada', 37590000, 9985000)
    denmark = Country("Denmark", 5603000, 42933)

    print(canada.is_larger(denmark))
    print(canada.population_density())
    print(canada)
    print([canada])



if __name__ == "__main__":
    main()
