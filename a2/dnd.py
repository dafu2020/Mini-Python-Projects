import random


def roll_die(number_of_rolls, number_of_sides):
    """Die rolling simulator
    This function simulator the process of rolling a die, return the sum of the individual rolls.

    :param number_of_rolls: a positive non-zero integer.
    :param number_of_sides: a positive non-zero integer.
    :precondition: number_of_rolls and number_of_sides must be positive non-zero integers.
    :postcondition: return the sum of the individual rolls.
    :return: the sum of the individual rolls as an integer.
    """
    count = 0
    roll_sum = 0
    while count < number_of_rolls:
        roll_result = random.randint(1, number_of_sides)
        print(roll_result)
        count += 1
        roll_sum += roll_result
    return roll_sum


# print(roll_die(2, 6))

def generate_vowel():
    """ Random vowel generator

    :postcondition: randomly select a single vowel.
    :return: a randomly selected single vowel as a string.
    """
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'y']
    vowel_result = random.choice(vowel_list)
    return vowel_result


def generate_consonant():
    """ Random consonant generator

    :postcondition: randomly select a single consonant.
    :return: a randomly selected single consonant as a string.
    """
    consonant_list = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                      'p', 'q', 'r', 's', 't', 'v', 'x', 'z', 'w', 'y']

    consonant_result = random.choice(consonant_list)
    return consonant_result


# print(generate_consonant())

def generate_syllable():
    """ Syllable generator
    Generate a two-lettered syllable by joining the random consonant generated by generate_consonant()
    and the random vowel generated by generate_vowel().

    :precondition: the random consonant must be generated by generate_consonant(),
                   and the random vowel must be generated by generate_vowel().
    :postcondition: concatenate the consonant and vowel in this exact order, to a two-letter syllable as a string.
    :return: the correctly concatenate two-letter syllable as a string.
    """
    syllable_result = generate_consonant() + generate_vowel()
    return syllable_result


# print(generate_syllable())

def generate_name(syllables):
    """ Name generator
    Generate a name by joining a certain number of two-lettered syllables generated by generate_syllable().

    :param syllables: a positive integer.
    :precondition: syllables must be a positive non-zero integer.
    :postcondition: generate a name composed of the specified number of two-lettered syllables.
    :return: correctly generate a name composed of the specified number of two-lettered syllables as a string
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

    :postcondition: prints out a list of classes to the player and asks the player to select the class they want to play
    :return: the race that the player desired as a string
    """
    print("the class you can choose is: Barbarian, Bard, Cleric, Druid, "
          "Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard")
    player_class = str(input("please enter the class you desired: ").strip().lower().capitalize())
    # print(player_class)

    return player_class


# select_class()
def select_race():
    """ Select a race
    Select a race from the nine classes in Dungeons & Dragons.

    :postcondition: prints out a list of races to the player and asks the player to select the race they want to play
    :return: the race that the player desired as a string
    """
    print("the race you can choose is: Dragonborn, Dwarf, Elf, Gnome, Half-Elf, Halfling, Half-Orc, Human, Tiefling ")
    player_race = str(input("please enter the race you desired: ").strip().lower().capitalize())
    print(player_race)

    return player_race


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


def choose_inventory():
    """Choose inventory items
    This function prints a list of goods to the screen and ask the player what they want to buy.

    :precondition: must accepts a well-formed character object.
    :postcondition: must print a list of goods to the screen and ask the player what they want to buy.
    """
    menu = ("Welcome to the Olde Tyme Merchant!\n"
            " \n"
            "Here is what we have for sale:\n"
            " \n"
            "1. sword\n"
            "2. dagger\n"
            "3. chalice of becoming\n"
            "4. orb of discovery\n"
            "5. and so on and so on...\n"
            " ")

    print(menu)
    player_select = input("What would you like to buy (-1 to finish):").strip()

    inventory_dictionary = {
        "1": "sword",
        "2": "dagger",
        "3": "chalice of becoming",
        "4": "orb of discover",
        "5": " and so on and so on..."
    }

    inventory_list = []
    if player_select == 1 or player_select == 2 or player_select == 3 or player_select == 4:
        inventory_list.append(inventory_dictionary[player_select])
        print(menu)
        choose_inventory() #  print menu and ask for input one more time
    elif player_select == -1:
        return inventory_list
    else:
        print("You are asking for something we do not carry, want to choose again?")
        print(menu)
        choose_inventory()  # print menu and ask for input one more time


# choose_inventory()

def combat_round(opponent_one, opponent_two):
    """ Simulate a round ot combat
    This function represents a single round of combat, each combatants gets a turn to do something
    during a single round of combat.

    :param opponent_one: a well-formed dictionaries containing a correct character
    :param opponent_two: a well-formed dictionaries containing a correct character
    :precondition: both parameters must be well-formed dictionaries that each containing a correct character
    :return:
    """
    opponent_one_roll = roll_die(1, 12)
    opponent_two_roll = roll_die(1, 12)

    if opponent_one_roll == opponent_two_roll:
        while opponent_one_roll == opponent_two_roll:
            combat_round(opponent_one, opponent_two)
            # If the characters roll the same number, roll again to get a winner. Keep rolling until someone rolls a
    else:
        if opponent_one_roll > opponent_two_roll:

        elif opponent_two_roll > opponent_one_roll:


def main():
    syllables =input("Please select the number of syllables for their character’s name: ")
    character = create_character(syllables)
    # assigning the return value to a local variable.
    print_character(character)
    choose_inventory()
    print_character(character)
    # (f) Hard-code a dictionary that contains a foe for your character. Pass both to the combat_round function,
    # and show me a good round of combat, please!




if __name__ == "__main__":
    main()
