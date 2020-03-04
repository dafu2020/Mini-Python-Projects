"""
Function to model a simple game, finding the exist.
"""


import doctest


def make_board() -> list:
    """Make a 5*5 game board

    :postcondition: creates a list containing coordination for a 5*5 game board
    :return: the successfully created 5*5 game board as a list
    """
    game_board = []
    for x in range(5):
        for y in range(5):
            game_board.append([x, y])
    return game_board


def make_character():
    """Make a character

    :postcondition: create a dictionary with character information
    :return: store character information as a dictionary
    """
    name = input('Please select a name for your character:  ').capitalize()
    character_dict = {
        'name': name,
        'x': 0,
        'y': 0
    }
    return character_dict


def print_location(character_dictionary: dict) -> None:
    """Print the location of the character on the game board

    :param character_dictionary: must be a dictionary
    :precondition: character_dictionary must be a dictionary containing two integers as the x and y coordinates
                   of the character
    :postcondition: print the location of the character on the game board base on the x and y coordinates
    >>> character_dictionary = {'x': 0,'y': 0,}
    >>> print_location(character_dictionary)
     $ . . . .
     . . . . .
     . . . . .
     . . . . .
     . . . . .
    >>> character_dictionary = {'x':4, 'y':4}
    >>> print_location(character_dictionary)
     . . . . .
     . . . . .
     . . . . .
     . . . . .
     . . . . $
    """
    for x in range(5):
        for y in range(5):
            print(' $', end='') if [character_dictionary['x'], character_dictionary['y']] == [x, y] else print(' .',
                                                                                                               end='')
        print()


def get_user_choice() -> str:
    """Ask user input for direction choice

    This function is use to ask the user whether they wish to move up down left or right
    :postcondition: ask user to enter a direction choice
    :return: the entered direction choice as a string
    """
    user_choice = input('Please enter a direction that you want to move: ').lower()
    return user_choice


def validate_move(board: list, character: dict, direction: str) -> bool:
    """Check if user can move in specific direction

    :param board: must be a list
    :param character: must be a dictionary
    :param direction: must be a string
    :precondition: board must be a list containing all game coordinates; character must be a dictionary that contains
                    character coordinates
    :postcondition: conclude a boolean result if the movement of the user choice is valid or not
    :return: a boolean result
    >>> board = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],[1, 0], [1, 1], [1, 2], [1, 3], [1, 4],[2, 0]]
    >>> character = {'x':0, 'y':0}
    >>> direction = 'nonsense'
    >>> validate_move(board, character, direction)
    This is not a valid input.
    False

    >>> board = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],[1, 0], [1, 1], [1, 2], [1, 3], [1, 4],[2, 0]]
    >>> character = {'x':0, 'y':0}
    >>> direction = 'n'
    >>> validate_move(board, character, direction)
    You have reached the wall
    False

    """

    valid_input_list = ['north', 'south', 'west', 'east', 'n', 's', 'w', 'e']
    while True:
        if direction in valid_input_list:
            if character['x'] == board[0][0]:
                if direction == 'north' or direction == 'n':
                    print('You have reached the wall')
                    return False
            if character['x'] == board[-1][0]:
                if direction == 'south' or direction == 's':
                    print('You have reached the wall')
                    return False
            if character['y'] == board[0][1]:
                if direction == 'west' or direction == 'w':
                    print('You have reached the wall')
                    return False
            if character['y'] == board[-1][1]:
                if direction == 'east' or direction == 'e':
                    print('You have reached the wall')
                    return False
            if character['y'] == board[-1][1] and character['x'] == board[-1][0]:
                if direction == 'north' or direction == 'n' or direction == 'west' or direction == 'w':
                    return True
            else:
                return True
        else:
            print('This is not a valid input.')
            return False


def move_character(direction: str, character: dict) -> dict:
    """ Change character's x and y coordinates base on user's input

    :param direction: a string
    :param character: a dictionary
    :precondition: direction must be a string; character must be a dictionary containing 'x' and 'y' as keys
    :postcondition: change the character coordinate base on the direction user wish to move
    :return: a modified character dictionary as a dictionary with changed character coordinates
    >>> user_direction = 'e'
    >>> user_character = {'x':2, 'y':2}
    >>> move_character(user_direction, user_character)
    {'x': 2, 'y': 3}

    >>> user_direction = 'north'
    >>> user_character = {'x':2, 'y':2}
    >>> move_character(user_direction, user_character)
    {'x': 1, 'y': 2}

    """
    if direction == 'east' or direction == 'e':
        if character['y'] != 4:
            character['y'] += 1
    elif direction == 'west' or direction == 'w':
        if character['y'] != 0:
            character['y'] += -1
    elif direction == 'north' or direction == 'n':
        if character['x'] != 0:
            character['x'] += -1
    elif direction == 'south' or direction == 's':
        if character['x'] != 4:
            character['x'] += 1

    return character


def check_if_exit_reached(character: dict) -> bool:
    """ Check if the user has reached the exist or not

    :param character: must be a dictionary
    :precondition:
    :postcondition: conclude a boolean result of whether the user has reached the exit or not
    :return: a boolean result
    """
    character_location = [character['x'], character['y']]
    if character_location == [4, 4]:
        print('You have reached the exist congratulation!')
        return True


def game():
    board = make_board()
    character = make_character()
    found_exist = False
    while not found_exist:
        print(character)
        print_location(character)
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        print(valid_move)
        if valid_move:
            move_character(direction, character)
            found_exist = check_if_exit_reached(character)
        else:
            print('Please re-enter.')
    print('***********************************')
    print('*                                 *')
    print('*            Game Over            *')
    print('*                                 *')
    print('***********************************')


def main() -> None:
    """ Initiate game
    """
    doctest.testmod()
    game()


if __name__ == "__main__":
    main()
