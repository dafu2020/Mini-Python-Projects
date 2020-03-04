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

