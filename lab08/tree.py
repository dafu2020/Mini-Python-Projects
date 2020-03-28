import doctest


class Tree:

    def __init__(self, species: str, age: int, trunk_circumference: float):
        """
        Initialize a new Tree.

        :param species: a string
        :param age: a positive integer
        :param trunk_circumference: a positive integer
        :precondition: species must be a string;
                        age must be a positive  integer;
                        trunk_circumference must be a positive integer in centimetres.
        :postcondition:initialized Tree as an object
        :raise ValueError: if species is empty or only-whitespaced;
                            if age is negative;
                            if trunk_circumference is negative.

        >>> tree_one = Tree('Osmanthus fragrans', 1, 10)

        >>> tree_two = Tree('Douglas fir', 1, 12)

        """
        if len(species) > 0 and species != ' ':
            self.__species = species.strip().title()
        else:
            raise ValueError('The species cannot be empty')
        if age >= 0:
            self.__age = age
        else:
            raise ValueError('The age of the tree cannot be negative')
        if trunk_circumference >= 0:
            self.__trunk_circumference = float(trunk_circumference)
        else:
            raise ValueError('The trunk circumference of the tree cannot be negative')

    def get_species(self) -> str:
        """
        Return the species name.

        :precondition: Tree must have an attribute called __species containing legit species name
        :postcondition: return the species name of the Tree
        :return: species as a string
        >>> tree_one = Tree('Osmanthus fragrans', 1, 10)
        >>> tree_one.get_species()
        'Osmanthus Fragrans'

        >>> tree_two = Tree('Douglas fir', 1, 12)
        >>> tree_two.get_species()
        'Douglas Fir'
        """
        return self.__species

    def get_age(self) -> int:
        """
        Return the age.
        :precondition: Tree must have an attribute called __age containing legit age
        :postcondition: return the age of the Tree
        :return: age as an int
        >>> tree_one = Tree('Osmanthus fragrans', 1, 10)
        >>> tree_one.get_age()
        1

        >>> tree_two = Tree('Douglas fir', 1, 12)
        >>> tree_two.get_age()
        1
        """
        return self.__age

    def get_trunk_circumference(self) -> float:
        """
        Return the trunk circumference
        :precondition: Tree must have an attribute called __trunk_circumference containing legit trunk circumference
        :postcondition: return the trunk circumference of the Tree
        :return: trunk circumference as float

        >>> tree_one = Tree('Osmanthus fragrans', 1, 10)
        >>> tree_one.get_trunk_circumference()
        10.0

        >>> tree_two = Tree('Douglas fir', 1, 12)
        >>> tree_two.get_trunk_circumference()
        12.0
        """
        return self.__trunk_circumference

    def update_age(self, new_age: int):
        """Update the age of the Tree

        :param new_age: a positive int
        :precondition: new_age must be a positive  integer;
                        Tree must have an attribute called __age containing legit age.
        :postcondition: modify the age of the Tree.
        :raise ValueError: if new_age is negative.


        >>> tree_one = Tree('Osmanthus fragrans', 1, 10)
        >>> tree_one.update_age(2)

        >>> tree_two = Tree('Douglas fir', 1, 12)
        >>> tree_two.update_age(2)
        """
        if new_age > 0:
            self.__age = new_age
        else:
            raise ValueError('The species cannot be empty')

    def update_trunk_circumference(self, new_trunk_circumference: float):
        """Update the trunk circumference of the Tree

        :param new_trunk_circumference: a positive float
        :precondition: new_trunk_circumference must be a positive float;
                        Tree must have an attribute called __trunk_circumference
                        containing legit trunk circumference in cm.
        :postcondition: modify the trunk circumference of the Tree.
        :raise ValueError: if new_trunk_circumference is negative.


        >>> tree_one = Tree('Osmanthus fragrans', 1, 10)
        >>> tree_one.update_trunk_circumference(12)

        >>> tree_two = Tree('Douglas fir', 1, 12)
        >>> tree_two.update_trunk_circumference(20)
        """
        if new_trunk_circumference > 0:
            self.__trunk_circumference = new_trunk_circumference
        else:
            raise ValueError('The species cannot be empty')

    def __str__(self) -> str:
        """
        Return a informative representation of this Tree for printing purpose.
        :precondition: a Tree  object must has the attributes of species, age, and trunk circumference.
        :postcondition: describe the informative representation of this Tree for printing purpose.
        :return: a description of this Tree as a str

        >>> tree_one = Tree('Osmanthus fragrans', 1, 10)
        >>> print(tree_one)
        Osmanthus Fragrans is 1 year(s) old, has a trunk circumference of 10.0 centimetres.

        >>> tree_two = Tree('Douglas fir', 1, 12)
        >>> print(tree_two)
        Douglas Fir is 1 year(s) old, has a trunk circumference of 12.0 centimetres.

        """
        return f'{self.__species} is {self.__age} year(s) old, has a trunk circumference of {self.__trunk_circumference} ' \
               f'centimetres.'

    def __repr__(self) -> str:
        """
        Return a informative representation of this Tree.
        :precondition: a Tree  object must has the attributes of species, age, and trunk circumference.
        :postcondition: describe the informative representation of this Tree.
        :return: a description of this Tree as a str

        >>> tree_one = Tree('Osmanthus fragrans', 1, 10)
        >>> repr(tree_one)
        'Tree("Osmanthus Fragrans", 1, 10.0)'

        >>> tree_two = Tree('Douglas fir', 1, 12)
        >>> repr(tree_two)
        'Tree("Douglas Fir", 1, 12.0)'

        """
        return f'Tree(\"{self.__species}\", {self.__age}, {self.__trunk_circumference})'


def main():
    doctest.testmod()
    tree_1 = Tree('Osmanthus fragrans', 12, 20)
    tree_2 = Tree('Douglas fir', 1, 10)

    print(repr(tree_1))
    print(tree_2)


if __name__ == "__main__":
    main()
