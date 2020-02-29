def game_map() -> list:
    coordinates = [(x, y) for x in range(5) for y in range(5)]
    return coordinates

print(game_map())

def print_map(player_coordinates:dict) -> None:
    for x in range(5):
        for y in range(5):
            if (player_coordinates['x'], player_coordinates['y']) == (x,y):
                print('P')
            else:
                print