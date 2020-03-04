def make_board():
    """Make a 5*5 game board

    :postcondition: create a list contain coordination for a 5*5 game board
    :return: the successfully created 5*5 game board as a list
    """
    game_board = []
    for x in range(5):
        for y in range(5):
            game_board.append((x, y))
    return game_board


def make_character():
    """Make a character

    :postcondition: create a dictionary with character information
    :return: store character information as a dictionary
    """
    name = input('Please select a name for your character:  ')
    character_dict = {
        'name': name,
        'x': 0,
        'y': 0,
    }
    return character_dict


def print_location(character_dictionary: dict) -> None:
    """Print the location of the character

    :param character_dictionary: must be a dictionary
    :precondition: character_dictionary must contain two integers as the x and y coordinates of the character
    :postcondition: print the location of the character base on the x and y coordinates
    """
    for y in range(5):
        for x in range(5):
            print(' $ ', end='') if (character_dictionary['x'], character_dictionary['y']) == (x, y) else print(' . ',
                                                                                                                end='')
        print()



