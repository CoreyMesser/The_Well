import os
from templates.template_text import Templates, CharacterControlTemplates
from constants import NavigationConstants, MapConstants, PlayerCommands
from level_maps.map_model import MapTemplate, Maps
from models import CharacterModels, SearchablesModel
from services_map_rendering import MapRenderer
from game_text.in_game_text import LookSearchMessages

class CharacterNavigation(object):

    def __init__(self):
        self.cctemp = CharacterControlTemplates()
        self.nc = NavigationConstants()
        self.templates = Templates()
        self.mps = Maps()
        self.mpstemp = MapTemplate()
        self.mpsc = MapConstants()
        self.mpren = MapRenderer()
        self.player_move_dict = CharacterModels.PLAYER_MOVE_DICT

    def clear_screen(self):
        pass

    def start_location(self, player_move_dict):
        level_map, _ = self.mpren.get_map(player_move_dict=player_move_dict)
        starting_position = level_map.index(9)
        starting_coordinates = self.mpstemp.MAP_COORDINATES[starting_position]
        self.update_player_location_and_path(location=starting_coordinates, path=starting_coordinates)

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
            if player_direction == NavigationConstants.NORTH:
                player_move = x, y - move
                return_menu = True
            if player_direction == NavigationConstants.SOUTH:
                player_move = x, y + move
                return_menu = True
            if player_direction == NavigationConstants.EAST:
                player_move = x + move, y
                return_menu = True
            if player_direction == NavigationConstants.WEST:
                player_move = x - move, y
                return_menu = True

        vaild_move = self.valid_player_move(player_move=player_move)
        if vaild_move is True:
            self.update_player_location_and_path(location=player_move, path=player_move)
            self.mpren.draw_map(player_move_dict=self.player_move_dict)

    def update_player_location_and_path(self, location, path):
        """
        updates both dict entries
        :param location: 
        :param path: 
        :return: 
        """
        self.player_move_dict['location'] = location
        self.player_move_dict['path'].append(path)

    def valid_player_move(self, player_move):
        """
        Basic collision detection of level map
        :param player_move: passed in from move_player
        :return: returns a True or a value appropriate to notify the player of obstacle
        """
        valid_move = False
        level_map, _ = self.mpren.get_map(player_move_dict=self.player_move_dict)

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


class CharacterInteraction(object):

    def __init__(self):
        self.search = SearchablesModel()
        self.character_services = CharacterServices()
        pass

    def character_look(self, look_direction, object_item=None):
        # where am I
        location, direction = self.character_services.get_player_position_and_directon()

        # what direction am I pointed
        look_direction = self.character_services.look_direction_interpreter(look_direction=look_direction, direction=direction)

        # what is around me
        self.character_services.look_see(look_direction=look_direction,location=location, direction=direction)


    def character_serach(self):
        pass

    def character_use(self):
        pass

    def character_take(self):
        pass


class NPCNavigation(object):
    pass

class CharacterServices(object):
    
    def __init__(self):
        self.looksearchmsg = LookSearchMessages()
        self.player_move_dict = CharacterModels.PLAYER_MOVE_DICT
        self.mpstemp = MapTemplate()
        self.player_commands = PlayerCommands()
        self.nav_constants = NavigationConstants()
        self.mpren = MapRenderer()

    def get_player_position_and_directon(self):
        player_position = self.player_move_dict['location']
        player_direction = self.player_move_dict['direction']
        return player_position, player_direction

    def get_range_of_view(self, location, direction):
        x, y = location
        range_of_view_dict = {'tile_center': {'NORTH': (0, -1), 'SOUTH': (0, +1), 'EAST': (+1, 0), 'WEST': (-1, 0)},
                              'tile_left': {'NORTH': (-1, 0), 'SOUTH': (+1, 0), 'EAST': (0, -1), 'WEST': (0, +1)},
                              'tile_right': {'NORTH': (+1, 0), 'SOUTH': (-1, 0), 'EAST': (0, +1), 'WEST': (0, -1)}}
        tile_center_adjust, tile_left_adjust, tile_right_adjust = range_of_view_dict['tile_center'][direction], \
                                                                  range_of_view_dict['tile_left'][direction], \
                                                                  range_of_view_dict['tile_right'][direction]
        tile_center = (x + tile_center_adjust[0], y + tile_center_adjust[1])
        tile_left = (x + tile_left_adjust[0], y + tile_left_adjust[1])
        tile_right = (x + tile_right_adjust[0], y + tile_right_adjust[1])
        return tile_center, tile_left, tile_right

    def get_map_tile(self, tile_x_y):
        tile_key = 1
        level_map, items_map = self.mpren.get_map(player_move_dict=self.player_move_dict)
        if tile_x_y in self.mpstemp.MAP_COORDINATES:
            tile_key = items_map[self.mpstemp.MAP_COORDINATES.index(tile_x_y)]
        return tile_key

    def get_tile_message(self, tile_position, tile_key, object_item=None):
        tile_message = self.looksearchmsg.build_message(tile_key=tile_key, tile_position=tile_position, object_item=object_item)
        return tile_message

    def look_direction_interpreter(self, look_direction, direction):
        if look_direction in self.nav_constants.COMPASS_DIRECTIONS_INTERPRETER.keys():
            if look_direction == direction:
                look_direction = self.nav_constants.FORWARD
                return look_direction
            else:
                look_direction = self.nav_constants.COMPASS_DIRECTIONS_INTERPRETER[direction][look_direction]
                return look_direction
        else:
            return look_direction


    def look_see(self, look_direction, location, direction):
        tile_center, tile_left, tile_right = self.get_range_of_view(location=location, direction=direction)
        look_direction_dict = {'RIGHT': tile_right, 'LEFT': tile_left, 'FORWARD': tile_center, 'BACKWARDS': tile_center,
                               'AROUND': [tile_center, tile_left, tile_right]}
        tile_key = self.get_map_tile(tile_x_y=look_direction_dict[look_direction])

        print(self.get_tile_message(tile_position=look_direction, tile_key=tile_key))


    def player_command_breakdown(self, player_choice):
        # choice_list = player_choice.split('')
        # choice = [entry
        #           for entry in choice_list
        #           if entry in self.player_commands.PLAYER_COMMANDS_SET]
        pass
