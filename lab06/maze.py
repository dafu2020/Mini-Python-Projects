"""
Function to model a simple game, finding the exit.
"""
import doctest


# make a game board using nested lists
def make_board(size: int) -> list:
    """Make a game board

    :param size: a non-zero positive integer
    :precondition: size must be a non-zero positive integer
    :postcondition: creates a list containing coordination for a certain size game board
    :return: the successfully created game board as a list
    >>> make_board(3)
    [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    >>> make_board(2)
    [[0, 0], [0, 1], [1, 0], [1, 1]]
    """
    game_board = []
    for x in range(size):
        for y in range(size):  # the game board is always a square
            game_board.append([x, y])
    return game_board


# make a defaulted character
def make_character() -> dict:
    """Make a character

    :postcondition: create a dictionary with character information at initial location
    :return: store character information as a dictionary
    """
    # the defaulted character always start at (0,0)
    character_dict = {
        'x': 0,
        'y': 0
    }
    return character_dict


# print the location of the character on the game board for player to interact
def print_location(length: int, character_dictionary: dict) -> None:
    """Print the location of the character on the game board

    :param length: a non-zero positive integer
    :param character_dictionary: must be a dictionary
    :precondition: length must be a positive non-zero integer;
                    character_dictionary must be a dictionary containing two integers as the x and y coordinates
                   of the character
    :postcondition: print the location of the character on the game board base on the x and y coordinates
    >>> length = 5
    >>> character_dictionary = {'x': 0,'y': 0}
    >>> print_location(length, character_dictionary)
     $ . . . .
     . . . . .
     . . . . .
     . . . . .
     . . . . .
    >>> length = 5
    >>> character_dictionary = {'x':4, 'y':4}
    >>> print_location(length, character_dictionary)
     . . . . .
     . . . . .
     . . . . .
     . . . . .
     . . . . $
    """
    for x in range(length):
        for y in range(length):  # using a ternary expression to print game board
            print(' $', end='') if [character_dictionary['x'], character_dictionary['y']] == [x, y] else print(' .',
                                                                                                               end='')
        print()


# ask player for commands
def get_user_choice() -> str:
    """Ask user input for direction choice

    This function is use to ask the user whether they wish to move north, south, west or east.
    :postcondition: ask user to enter a direction choice
    :return: the entered direction choice as a string
    """
    user_choice = input('Please enter a direction that you want to move: ').lower()
    if user_choice == 'quit':  # player can quit game when he/she wants
        print("You choose to end the game!")
        print('***********************************')
        print('*            Game Over            *')
        print('***********************************')
        quit()
    else:
        return user_choice


def validate_move(game_board: list, game_character: dict, game_direction: str) -> bool:
    """Check if user can move in specific direction

    :param game_board:  a list
    :param game_character: a dictionary
    :param game_direction: a string
    :precondition: game_board must be a list containing all game coordinates;
                    game_character must be a dictionary that contains character coordination;
                    game_direction must be a string
    :postcondition: determine the movement of the user is valid or not
    :return: if the user movement is valid return True, else return False
    >>> board = [[0, 0], [0, 1], [1,0], [1,1]]
    >>> character = {'x':0, 'y':0}
    >>> direction = 'nonsense'
    >>> validate_move(board, character, direction)
    This is not a valid input.
    False

    >>> board = [[0, 0], [0, 1], [1,0], [1,1]]
    >>> character = {'x':0, 'y':0}
    >>> direction = 'n'
    >>> validate_move(board, character, direction)
    You have reached the wall
    False

    """

    valid_input_list = ['north', 'south', 'west', 'east', 'n', 's', 'w', 'e']
    while True:
        if game_direction in valid_input_list:
            if game_character['x'] == game_board[0][0]:
                # when character is at the north boundary of the board
                if game_direction == 'north' or game_direction == 'n':
                    print('You have reached the wall')
                    return False
            if game_character['x'] == game_board[-1][0]:
                # when character is at the south boundary of the board
                if game_direction == 'south' or game_direction == 's':
                    print('You have reached the wall')
                    return False
            if game_character['y'] == game_board[0][1]:
                # when character is at the west boundary of the board
                if game_direction == 'west' or game_direction == 'w':
                    print('You have reached the wall')
                    return False
            if game_character['y'] == game_board[-1][1]:
                # when character is at the east boundary of the board
                if game_direction == 'east' or game_direction == 'e':
                    print('You have reached the wall')
                    return False
            if game_character['y'] == game_board[-1][1] and game_character['x'] == game_board[-1][0]:
                # when character is at the last cell of the board
                if game_direction == 'north' or game_direction == 'n' or game_direction == 'west' or game_direction == \
                        'w':
                    return True
            else:
                return True
        else:  # use to validate if the command that player entered is a direction or not
            print('This is not a valid input.')
            return False


def move_character(my_board: list, my_direction: str, my_character: dict) -> dict:
    """ Move character

    A function to change character's x and y coordinates base on user's input on the game board.
    :param my_board: a list
    :param my_direction: a string
    :param my_character: a dictionary
    :precondition: my_board must be a list; my_direction must be a string;
                   my_character must be a dictionary containing 'x' and 'y' as keys
    :postcondition: change the character coordinate base on the direction user wish to move
    :return: a modified character dictionary as a dictionary with changed character coordinates
    >>> game_board = [[0, 0], [0, 1], [1,0], [1,1]]
    >>> user_direction = 'e'
    >>> user_character = {'x':0, 'y':0}
    >>> move_character(game_board, user_direction, user_character)
    {'x': 0, 'y': 1}

    >>> game_board = [[0, 0], [0, 1], [1,0], [1,1]]
    >>> user_direction = 'north'
    >>> user_character = {'x':1, 'y':0}
    >>> move_character(game_board, user_direction, user_character)
    {'x': 0, 'y': 0}

    """
    character_location = [my_character['x'], my_character['y']]
    if character_location in my_board:
        if my_direction == 'east' or my_direction == 'e':
            # character move east if has not reached the eastern boundary
            if my_character['y'] != my_board[-1][1]:
                my_character['y'] += 1
        elif my_direction == 'west' or my_direction == 'w':
            # character move west if has not reached the western boundary
            if my_character['y'] != my_board[0][1]:
                my_character['y'] -= 1
        elif my_direction == 'north' or my_direction == 'n':
            # character move north if has not reached the northern boundary
            if my_character['x'] != my_board[0][0]:
                my_character['x'] -= 1
        elif my_direction == 'south' or my_direction == 's':
            # character move south if has not reached the southern boundary
            if my_character['x'] != my_board[-1][0]:
                my_character['x'] += 1

        return my_character
    else:
        pass


def check_if_exit_reached(my_board: list, my_character: dict) -> bool:
    """ Check if the user has reached the exit or not

    :param my_board: must be a list
    :param my_character: must be a dictionary
    :precondition: my_board must be a non-empty list; my_character must be a dictionary containing 'x' and 'y' as keys
    :postcondition: conclude a boolean result of whether the user has reached the exit or not
    :return: a boolean result
    >>> board = [[0, 0], [0, 1], [1,0], [1,1]]
    >>> character = {'x':0, 'y':0}
    >>> check_if_exit_reached(board, character)
    False

    >>> board = [[0, 0], [0, 1], [1,0], [1,1]]
    >>> character = {'x':1, 'y':1}
    >>> check_if_exit_reached(board, character)
    You have reached the exit, congratulation!
    True

    """
    character_location = [my_character['x'], my_character['y']]
    game_exit = [my_board[-1][0], my_board[-1][1]]
    # check if the character is at the last cell of the game board
    if character_location == game_exit:
        print('You have reached the exit, congratulation!')
        return True
    else:
        return False


def game() -> None:
    """Run the game

    :postcondition: create a game board；create a character; receive input from user and execute them accordingly;
                    print guiding messages accordingly.
    """
    # print game start message
    print('***********************************')
    print('*            Game Start           *')
    print('***********************************')
    # print game direction
    print('You wake up remembering nothing but finding the exit of this forest.... \n'
          'Please enter \'(N)orth\', \'(S)outh\', \'(W)est\', \'(E)ast\' for direction')

    # create a game board
    board_size = 5
    board = make_board(board_size)
    # make a character
    character = make_character()
    found_exist = False
    # before find the exist
    while not found_exist:
        print_location(board_size, character)  # print the location of the character on board
        direction = get_user_choice()  # ask user for direction
        valid_move = validate_move(board, character, direction)  # validate the direction
        if valid_move:
            move_character(board, direction, character)  # make character if the direction is true
            found_exist = check_if_exit_reached(board, character)  # exist the loop if the exist is found
        else:
            print('Please re-enter.')
    # display game over message
    print('***********************************')
    print('*            Game Over            *')
    print('***********************************')


def main() -> None:
    """ Initiate game and run doctests

    """
    doctest.testmod()
    game()


if __name__ == "__main__":
    main()
