import random
import doctest


def roll_die(number_of_rolls, number_of_sides):
    """

    :param number_of_rolls: positive non-zero integers
    :param number_of_sides: positive non-zero integers
    :return: the result of the die rolling simulation as a integer
    """
    count = 0
    while count < number_of_rolls:
        roll_result = random.randint(1, number_of_sides)
        count += 1
        print(roll_result)
        return roll_result


# return the result of the last roll?? or return the  result of all the rolls (like dictionary)?

def generate_vowel():
    """ Random vowel generator

    :postcondition: randomly select a single vowel.
    :return: a randomly selected single vowel as a string.
    """
    # vowel_list = ['i', 'I', 'ɛ', 'æ', 'ɜ', 'ɘ', 'u', 'ʊ', 'ɔ', 'ɒ', 'ʌ', 'ɑ']
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'y']
    vowel_result = random.choice(vowel_list)
    return vowel_result


def generate_consonant():
    """ Random consonant generator

    :postcondition: randomly select a single consonant.
    :return: a randomly selected single consonant as a string.
    """
    # consonant_list = ['p', 'b', 't', 'd', 'k', 'g', 'f', 'v', 'θ', 'ð', 's', 'z', 'ʃ',
    # '', 'h', 'x', 'tʃ', '', 'm', 'n', 'ŋ', 'l', 'r', 'w', 'j']
    consonant_list = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                      'p', 'q', 'r', 's', 't', 'v', 'x', 'z', 'w', 'y']

    consonant_result = random.choice(consonant_list)
    return consonant_result


# print(generate_consonant())

def generate_syllable():
    """ Syllable generator
    Generate a two-lettered syllable by joining the random generated consonant generated by generate_consonant()
    and the random generated vowel generated by generate_vowel().

    :return: concatenate the consonant and vowel,to a two-letter syllable as  a  string
    """
    syllable_result = generate_consonant() + generate_vowel()
    return syllable_result


# print(generate_syllable())

def generate_name(syllables):
    """ Name generator
    Generate a name by joining a certain number of two-lettered syllables generated by generate_syllable().

    :param syllables: a positive integer
    :precondition: syllables must be a positive non-zero integer
    :postcondition: generate a name composed of the specified number of two-lettered syllables
    :return: generate a name composed of the specified number of two-lettered syllables as a string
    """

    count = 0
    name_result = ''
    while count < syllables:
        syllables_generated = generate_syllable()
        name_result += syllables_generated
        count += 1
    return name_result


# print(generate_name(3))

def create_character(syllables):
    """ Create a Dungeons and Dragons character

    :param syllables:
    :return:
    """
    if syllables != isinstance(1, int):
        # isinstance (1, int) is a boolean expression to test if syllables is not a positive non-zero integer
        print("Warning: this is not a correct input, please enter a positive integer.")
        return None
    else:
        inventory_list = []
        character = {
            'Name': generate_name(syllables),
            'Strength': roll_die(3, 6),
            'Intelligence': roll_die(3, 6),
            'Wisdom': roll_die(3, 6),
            'Dexterity': roll_die(3, 6),
            'Constitution': roll_die(3, 6),
            'Charisma': roll_die(3, 6),
            'inventory': inventory_list,
            'experience points': 0,
            'class': select_class(),
            'Race': select_race(),
            'HP': ["maximum HP", "current HP"]
        }
        return character
        # 3f) Each of these attributes is initialized by rolling three six- sided dice. We call this 3d6 in D&D.
        # 3 o) HP??


def select_class():
    """ Select a class
    Select a class from the twelve classes in Dungeons & Dragons.

    :postcondition: prints out a list of classes to the user and asks the user to select the class they want to play
    :return: the race that the user desired as a string
    """
    print("the class you can choose is: Barbarian, Bard, Cleric, Druid, "
          "Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard")
    user_class = str(input("please enter the class you desired: ").strip().lower().capitalize())
    # print(user_class)

    return user_class


# select_class()
def select_race():
    """ Select a race
    Select a race from the nine classes in Dungeons & Dragons.

    :postcondition: prints out a list of races to the user and asks the user to select the race they want to play
    :return: the race that the user desired as a string
    """
    print("the race you can choose is: Dragonborn, Dwarf, Elf, Gnome, Half-Elf, Halfling, Half-Orc, Human, Tiefling ")
    user_race = str(input("please enter the race you desired: ").strip().lower().capitalize())
    print(user_race)

    return user_race


# select_race()

def print_character(character):
    """Print character information
    This function print a list of the character's information which is generated by the create_character function.

    :param character:a list formatted by the create_character function.
    :precondition: character must be formed my the the create_character function.
    :postcondition: print the character list formatted by the create_character function
    """
    print(character)
    # 4) can it work????


