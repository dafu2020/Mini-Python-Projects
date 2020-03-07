"""
Function to model a simple game, finding the exit.
"""
import doctest


def make_board(length: int) -> list:
    """Make a game board

    :param length: a non-zero positive integer
    :precondition: length must be a non-zero positive integer
    :postcondition: creates a list containing coordination for a 5*5 game board
    :return: the successfully created 5*5 game board as a list
    >>> make_board(1)
    [[0, 0]]
    >>> make_board(2)
    [[0, 0], [0, 1], [1, 0], [1, 1]]
    """
    game_board = []
    for x in range(length):
        for y in range(length):
            game_board.append([x, y])
    return game_board


def make_character() -> dict:
    """Make a character

    :postcondition: create a dictionary with character information
    :return: store character information as a dictionary
    """
    character_dict = {
        'x': 0,
        'y': 0
    }
    return character_dict


def print_location(length: int, character_dictionary: dict) -> None:
    """Print the location of the character on the game board

    :param length: a non-zero positive integer
    :param character_dictionary: must be a dictionary
    :precondition: length must ve a positive non-zero integer;
                    character_dictionary must be a dictionary containing two integers as the x and y coordinates
                   of the character
    :postcondition: print the location of the character on the game board base on the x and y coordinates
    >>> length = 5
    >>> character_dictionary = {'x': 0,'y': 0,}
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
        for y in range(length):
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
    if user_choice == 'quit':
        print("You choose to end the game!")
        print('***********************************')
        print('*            Game Over            *')
        print('***********************************')
        quit()
    else:
        return user_choice


def validate_move(game_board: list, game_character: dict, game_direction: str) -> bool:
    """Check if user can move in specific direction

    :param game_board: must be a list
    :param game_character: must be a dictionary
    :param game_direction: must be a string
    :precondition: board must be a list containing all game coordinates; character must be a dictionary that contains
                    character coordinates
    :postcondition: conclude a boolean result if the movement of the user choice is valid or not
    :return: a boolean result
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
                if game_direction == 'north' or game_direction == 'n':
                    print('You have reached the wall')
                    return False
            if game_character['x'] == game_board[-1][0]:
                if game_direction == 'south' or game_direction == 's':
                    print('You have reached the wall')
                    return False
            if game_character['y'] == game_board[0][1]:
                if game_direction == 'west' or game_direction == 'w':
                    print('You have reached the wall')
                    return False
            if game_character['y'] == game_board[-1][1]:
                if game_direction == 'east' or game_direction == 'e':
                    print('You have reached the wall')
                    return False
            if game_character['y'] == game_board[-1][1] and game_character['x'] == game_board[-1][0]:
                if game_direction == 'north' or game_direction == 'n' or game_direction == 'west' or game_direction == \
                        'w':
                    return True
            else:
                return True
        else:
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
            if my_character['y'] != my_board[-1][1]:
                my_character['y'] += 1
        elif my_direction == 'west' or my_direction == 'w':
            if my_character['y'] != my_board[0][1]:
                my_character['y'] -= 1
        elif my_direction == 'north' or my_direction == 'n':
            if my_character['x'] != my_board[0][0]:
                my_character['x'] -= 1
        elif my_direction == 'south' or my_direction == 's':
            if my_character['x'] != my_board[-1][0]:
                my_character['x'] += 1

        return my_character
    else:
        pass


def check_if_exit_reached(my_board: list, my_character: dict) -> bool:
    """ Check if the user has reached the exit or not

    :param my_board: must be a list
    :param my_character: must be a dictionary
    :precondition: board must be a non-empty list; character must be a dictionary containing 'x' and 'y' as keys
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
    if character_location == game_exit:
        print('You have reached the exit, congratulation!')
        return True
    else:
        return False


def game():
    """Run the game

    :postcondition: create a game board；create a character; receive input from user and execute them  accordingly;
                    print guiding messages accordingly.
    """
    print('***********************************')
    print('*            Game Start           *')
    print('***********************************')
    print('You wake up remembering nothing but finding the exit of this forest.... \n'
          'Please enter \'(N)orth\', \'(S)outh\', \'(W)est\', \'(E)ast\' for direction')

    board_size = 5
    board = make_board(board_size)
    character = make_character()
    found_exist = False
    while not found_exist:
        print_location(board_size, character)
        # print(character)
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(board, direction, character)
            found_exist = check_if_exit_reached(board, character)
        else:
            print('Please re-enter.')
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
