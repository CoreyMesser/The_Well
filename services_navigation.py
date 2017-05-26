import os
from templates.template_text import Templates, CharacterControlTemplates
from constants import NavigationConstants
from level_maps.map_model import MapTemplate, Maps, MapConstants
from models import CharacterModels
from services_map_rendering import MapRenderer

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
        current_level = player_move_dict['current_level']
        level_map = self.get_current_level_map(current_level=current_level)
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
            if player_direction == 'NORTH':
                player_move = x, y - move
                return_menu = True
            if player_direction == 'SOUTH':
                player_move = x, y + move
                return_menu = True
            if player_direction == 'EAST':
                player_move = x + move, y
                return_menu = True
            if player_direction == 'WEST':
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

