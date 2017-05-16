import os

class CharacterNavigation(object):
    player_move_dict = {'location': None, 'path': []}

    def __init__(self):
        pass

    def clear_screen(self):
        pass

    def start_location(self):
        # returns starting location based on level
        pass

    def get_player_direction(self):
        # detects/turns character in a direction
        pass

    def get_player_moves(self):
        # gets nav input from player
        # direction
        # spaces moved
        pass

    def move_player(self):
        # moves player based on input and direction
        pass


    pass

class NPCNavigation(object):
    pass



# import random, os, logging
#
# CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0),
#          (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1),
#          (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2),
#          (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3),
#          (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4),
#          (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)]
#
# player = {'location': None, 'path': []}
#
# logging.basicConfig(filename='game.log.log', level=logging.DEBUG)
#
#
# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')
#
#
# def start_locations():
#     monster = random.choice(CELLS)
#     door = random.choice(CELLS)
#     start = random.choice(CELLS)
#
#     if monster == door or monster == start or door == start:
#         monster, door, start = start_locations()
#     return monster, door, start
#
#
# def get_moves(player):
#     moves = ["LEFT", "RIGHT", "UP", "DOWN"]
#     x, y = player
#     if x == 0:
#         moves.remove("LEFT")
#     if x == 5:
#         moves.remove("RIGHT")
#     if y == 0:
#         moves.remove("UP")
#     if y == 5:
#         moves.remove("DOWN")
#     return moves
#
#
# def move_player(player, move):
#     x, y = player['location']
#     player['path'].append((x, y))
#     if move == "LEFT":
#         player['location'] = x, y - 1
#     if move == "RIGHT":
#         player['location'] = x, y + 1
#     if move == "UP":
#         player['location'] = x - 1, y
#     if move == "DOWN":
#         player['location'] = x + 1, y
#
#     return player
#
#
# def move(player, direction):
#     x, y, hp = player
#     a, b = direction
#
#     x = x + a
#     y = y + b
#
#     if x < 0 or x > 5:
#         hp = hp - 5
#         if x < 0:
#             x += 1
#         elif x > 5:
#             x += -1
#     if y < 0 or y > 5:
#         hp = hp - 5
#         if y < 0:
#             y += 1
#         elif y > 5:
#             y += -1
#     print(x, y, hp)
#     return x, y, hp
#
#
# def draw_map(player):
#     print(" _"*6)
#     tile = "|{}"
#
#     for idx, cell in enumerate(CELLS):
#         if idx in [0, 1, 3, 4, 6, 7]:
#             if cell == player['location']:
#                 print(tile.format('X'), end='')
#             if cell == player['path']:
#                 print(tile.format('.'), end='')
#             else:
#                 print(tile.format('_'), end='')
#         else:
#             if cell == player:
#                 print(tile.format('X|'))
#             elif cell in player['path']:
#                 print(tile.format('.|'))
#             else:
#                 print(tile.format('_|'))
#
#     # OLD CELL DRAW
#     # for cell in CELLS:
#     #     x, y = cell
#     #     if x < 5:
#     #         line_end = ""
#     #         if cell == player:
#     #             output = tile.format("X")
#     #         else:
#     #             output = tile.format("_")
#     #     else:
#     #         line_end = "\n"
#     #         if cell == player:
#     #             output = tile.format("X|")
#     #         else:
#     #             output = tile.format("_|")
#     #     print(output, end=line_end)
#
#
# def game_loop():
#     monster, door, player['location'] = start_locations()
#     logging.info('monster: {}; door: {}; player: {}'.format(monster, door, player['location']))
#     logging.d
#     playing = True
#
#     while playing:
#         clear_screen()
#         draw_map(player)
#         valid_moves = get_moves(player)
#
#         print("You are in room {}".format(player))
#         print("you can move {}".format(", ".join(valid_moves)))
#         print("Enter QUIT to quit")
#
#         move = input("> ")
#         move = move.upper()
#
#         if move == 'QUIT':
#             print('You flee the dungeon as a coward.')
#             playing = False
#
#         if move in valid_moves:
#             player = move_player(player, move)
#             if player == monster:
#                 print("\n** A gru pounces on you from the dark and your screams fill the room. **\n")
#                 playing = False
#             elif player == door:
#                 print("\n** You stumble out the door into the light gasping for breath. **\n")
#                 playing = False
#         else:
#             input("\n ** walls are hard! **\n")
#
#     else:
#         if input("Play again [Y/N]").lower() != 'n':
#             game_loop()
#
#
#         # win_lose(monster=monster, door=door, player=player, valid_moves=valid_moves)
#
# clear_screen()
# print("Welcome")
# input("Press return to start")
# clear_screen()
# game_loop()
