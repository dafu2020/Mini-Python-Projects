def make_board() -> list:
    """Make a 5*5 game board

    :postcondition: create a list contain coordination for a 5*5 game board
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
            print(' $ ', end='') if [character_dictionary['x'], character_dictionary['y']] == [x, y] else print(' . ',
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


def validate_move(my_board: list, my_character: dict, my_direction: str) -> bool:
    """Check if user can move in specific direction

    :param my_board: must be a list
    :param my_character: must be a dictionary
    :param my_direction: must be a string
    :precondition: board must be a list containing all game coordinates; character must be a dictionary that contains
                    character coordinates
    :postcondition: conclude a boolean result if the movement of the user choice is valid or not
    :return: a boolean result
    """
    valid_input_list = ['north', 'south', 'west', 'east']
    while True:
        if my_direction in valid_input_list:
            if my_character['x'] == 0 and my_direction == 'north':
                print('You have reached the boundary, you cannot move this way.')
                return False
            if my_character['x'] == 4 and my_direction == 'south':
                print('You have reached the boundary, you cannot move this way.')
                return False
            if my_character['y'] == 0 and my_direction == 'west':
                print('You have reached the boundary, you cannot move this way.')
                return False
            if my_character['y'] == 4 and my_direction == 'east':
                print('You have reached the boundary, you cannot move this way.')
                return False
            else:
                return True
        else:
            print('This is not a valid input for direction, please enter: \'north\' or \'south\' or \'west\' or \'east\'')
            my_direction = get_user_choice()
            continue


def game():
    board = make_board()
    character = make_character()
    found_exist = False
    while not found_exist:
        print_location(character)
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if validate_move:
            move_character()
            found_exit = check_if_exit_reached()


game()
