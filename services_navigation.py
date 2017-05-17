import os
from templates.templates import Templates, CharacterControlTemplates
from constants import NavigationConstants
from level_maps.map_model import MapTemplate, Maps, MapConstants

class CharacterNavigation(object):

    def __init__(self):
        self.cctemp = CharacterControlTemplates()
        self.nc = NavigationConstants()
        self.templates = Templates()
        self.mps = Maps()
        self.mpstemp = MapTemplate()
        self.mpsc = MapConstants()
        self.player_move_dict = {'location': None, 'path': [], 'direction': 'NORTH', 'current_level': 'LEVEL_00'}

    def clear_screen(self):
        pass

    def start_location(self):
        # returns starting location based on level
        pass

    def get_player_direction(self, player_choice):
        return_menu = False
        directions = self.nc.DIRECTIONS_DICT
        while return_menu is False:
            if player_choice in directions:
                self.player_move_dict['direction'] = player_choice
                return_menu = True
            else:
                print(self.templates.VALID_ENTRY)
                player_choice = input(self.cctemp.PLAYER_DIRECTIONS).upper()

    def get_player_moves(self, player_choice):
        directions = self.nc.DIRECTIONS_DICT
        player_list = list(player_choice)
        player_move = 0
        for direction_check in player_list:
            if direction_check in directions:
                if directions[direction_check] == self.player_move_dict['direction']:
                    break
                else:
                    self.player_move_dict['direction'] = directions[direction_check]
                    break
        for move_check in player_list:
            if move_check in self.nc.MOVE_CONVERTER_DICT:
                player_move = self.nc.MOVE_CONVERTER_DICT[move_check]
                break
        return player_move

    def move_player(self, player_choice):
        return_menu = False

        move = self.get_player_moves(player_choice=player_choice)
        player_direction = self.player_move_dict['direction']
        x, y = self.player_move_dict['location']
        player_move = x, y

        while return_menu is False:
            if player_direction == 'NORTH':
                player_move = x, y - move
                return_menu = True
            if player_direction == 'SOUTH':
                player_move = x, y + move
                return_menu = True
            if player_direction == 'EAST':
                player_move = x - move, y
                return_menu = True
            if player_direction == 'WEST':
                player_move = x + move, y
                return_menu = True

        vaild_move = self.valid_player_move(player_move=player_move)
        if vaild_move is True:
            self.player_move_dict['location'] = player_move
            self.player_move_dict['path'].append(player_move)

    def valid_player_move(self, player_move):
        """
        Basic collision detection of level map
        :param player_move: passed in from move_player
        :return: returns a True or a value appropriate to notify the player of obstacle
        """
        valid_move = False
        current_level = self.player_move_dict['current_level']
        level_map = self.get_current_level_map(current_level=current_level)

        if player_move in self.mpstemp.MAP_COORDINATES:
            move_index = self.mpstemp.MAP_COORDINATES.index(player_move)
            level_map_check = level_map[move_index]
            if level_map_check == 0:
                valid_move = True
            if level_map_check == 1:
                # check what they ran into
                pass
            if level_map_check == 2:
                # searchable area
                pass

        return valid_move

    def get_current_level_map(self, current_level):
        level_map = current_level
        if current_level == 'LEVEL_00':
            level_map = self.mps.MAP_LEVEL_00
        return level_map


        # moves player based on input and direction


    pass


class CharacterInteraction(object):

    def __init__(self):
        pass

    def character_look(self):
        pass

    def character_serach(self):
        pass

    def character_use(self):
        pass

    def character_take(self):
        pass


class NPCNavigation(object):
    pass



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
