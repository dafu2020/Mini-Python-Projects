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

    :return: a randomly selected single vowel as a string.
    """
    # vowel_list = ['i', 'I', 'ɛ', 'æ', 'ɜ', 'ɘ', 'u', 'ʊ', 'ɔ', 'ɒ', 'ʌ', 'ɑ']
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'y']
    vowel_result = random.choice(vowel_list)
    return vowel_result


def generate_consonant():
    """ Random consonant generator

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
        # print(generate_syllable())
        syllables_generated = generate_syllable()
        name_result += syllables_generated
        count += 1
    return name_result


print(generate_name(3))


