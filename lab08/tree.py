class Tree:
    def __init__(self, species, age, trunk_circumference):
        if len(species) > 0:
            self.species = species.title()
        else:
            raise ValueError('The species cannot be empty')
        if age >= 0:
            self.age = age
        else:
            raise ValueError('The age of the tree cannot be negative')
        if trunk_circumference >= 0:
            self.trunk_circumference = trunk_circumference
        else:
            raise ValueError('The age of the tree cannot be negative')

    def get_species(self):
        """
        Return the species name.
        :return: species as a string
        """
        return self.species

    def get_age(self):
        """
        Return the age.
        :return: age as an int
        """
        return self.age

    def get_trunk_circumference(self):
        """
        Return the trunk circumference
        :return: trunk circumference as int.
        """
        return self.trunk_circumference

    def update_species(self, new_species):
        if len(new_species) > 0:
            self.species = new_species.title()
        else:
            raise ValueError('The species cannot be empty')

    def __str__(self):
        return f'{self.species} is {self.age} year(s) old, has a trunk circumference of {self.trunk_circumference} ' \
               f'centimetres.'

    def __repr__(self) -> str:
        return f'Tree(\"{self.species}\", {self.age}, {self.trunk_circumference})'


def main():
    tree_1 = Tree('Osmanthus fragrans', 12, 20)
    tree_2 = Tree('Douglas fir', 1, 10)

    print(repr(tree_1))
    print(tree_2)


if __name__ == "__main__":
    main()
