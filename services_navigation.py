import random
import re

from constants import NavigationConstants, MapConstants, PlayerCommands, MessagesConstants, ObjectConstants, WeaponConstant
from game_text.in_game_text import GameMessages, TileKeyConstants
from level_maps.map_model import MapTemplate, Maps
from models import CharacterModels, PlayerCharacter
from services_map_rendering import MapRenderer
from services_get_character import InventoryServices
from templates.template_text import Templates, CharacterControlTemplates


class CharacterNavigation(object):

    def __init__(self):
        self.cctemp = CharacterControlTemplates()
        self.templates = Templates()
        self.mps = Maps()
        self.mpstemp = MapTemplate()
        self.mpsc = MapConstants()
        self.mpren = MapRenderer()
        self.player_move_dict = CharacterModels.PLAYER_MOVE_DICT
        self.nav_constants = NavigationConstants()
        self.look_search = LookSearchServices()
        self.character_services = CharacterServices()

    def clear_screen(self):
        pass

    def start_location(self, player_move_dict):
        level_map, _ = self.mpren.get_map(player_move_dict=player_move_dict)
        starting_position = level_map.index(9)
        starting_coordinates = self.mpstemp.MAP_COORDINATES[starting_position]
        self.update_player_location_and_path(location=starting_coordinates, path=starting_coordinates)

    def get_player_direction(self, player_choice):
        if player_choice in self.nav_constants.DIRECTIONS_LIST:
            self.player_move_dict['direction'] = player_choice
        elif player_choice['direction'] in self.nav_constants.DIRECTIONS_LIST:
            self.player_move_dict['direction'] = player_choice['direction']
        else:
            self.player_move_dict['direction'] = self.nav_constants.COMPASS_DIRECTIONS_INTERPRETER[self.player_move_dict['direction']][
                player_choice['direction']]

    def get_player_moves(self, player_choice):
        try:
            player_move = player_choice['move']
            if player_choice['direction']:
                if self.player_move_dict['direction'] != player_choice['direction']:
                    if player_choice['direction'] in self.nav_constants.COMPASS_DIRECTIONS_LIST:
                        self.player_move_dict['direction'] = player_choice['direction']
                    else:
                        self.player_move_dict['direction'] = self.nav_constants.COMPASS_DIRECTIONS_INTERPRETER[self.player_move_dict['direction']][player_choice['direction']]
        except:
            directions = self.nav_constants.DIRECTIONS_DICT
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
                if move_check in self.nav_constants.MOVE_CONVERTER_DICT:
                    player_move = self.nav_constants.MOVE_CONVERTER_DICT[move_check]
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
        else:
            # incorrect use, currently pulls fromm the message generation system and should pull from the collissions messages
            print(self.look_search.build_collission_message(
                tile_key=self.character_services.get_map_tile_ahead(tile_x_y=self.player_move_dict['location'])))

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
        self.character_services = CharacterServices()
        self.player_move_dict = CharacterModels.PLAYER_MOVE_DICT
        self.player_character_dict = PlayerCharacter.character_dict
        self.player_skills_dict = PlayerCharacter.skills_dict
        self.nav_constants = NavigationConstants()
        self.look_search = LookSearchServices()


    def character_look(self, player_choice, object_item=None):
        if player_choice in self.nav_constants.DIRECTIONS_LIST:
            look_direction = player_choice
        else:
            look_direction = player_choice['direction']

        location, direction = self.character_services.get_player_position_and_directon()
        look_direction = self.character_services.look_direction_interpreter(look_direction=look_direction, direction=direction)
        self.character_services.look_see(look_direction=look_direction, location=location, direction=direction)

        # detect if a hallway/room exists floor id 00 - basic hall, 01 - basic room 02 - basic nook/alcove
        # detect doors/stairs/portals/etc  7 - generic portal, 70 - basic door, 71 basic stairs


    def character_serach(self, search_object):
        tile_center, _, _ = self.character_services.get_range_of_view(location=self.player_move_dict['location'],
                                                                      direction=self.player_move_dict['direction'])
        object_message, tile_key = self.character_services.search_object(object_tile=tile_center, search_object=search_object['object_item'])

        print(object_message)

        self.character_services.open_container(tile_key=tile_key)

        # take subroutine


    def character_use(self):
        pass

    def character_take(self, player_choice, object_model=None):
        if object_model:
            if player_choice in object_model.container_inventory.keys():
                self.character_services.take_object_item(player_choice=player_choice, object_model=object_model)
            else:
                # invalid selection
                pass
        else:
            object_model = self.look_search.get_object_model(tile_key=self.character_services.get_map_tile_ahead(tile_x_y=self.player_move_dict['location']))
            self.character_services.take_object_item(player_choice=player_choice, object_model=object_model)
        # single item vs all items

        # keep a container open if container
        # take an item
        # detect object_item


class NPCNavigation(object):
    pass

class CharacterServices(object):
    
    def __init__(self):
        self.cctemp = CharacterControlTemplates()
        self.look_search = LookSearchServices()
        self.player_move_dict = CharacterModels.PLAYER_MOVE_DICT
        self.player_inventory_dict = CharacterModels.PLAYER_INVENTORY_DICT
        self.player_skills_dict = PlayerCharacter.skills_dict
        self.mpstemp = MapTemplate()
        self.player_commands = PlayerCommands()
        self.nav_constants = NavigationConstants()
        self.mpren = MapRenderer()

    def take_object_item(self, player_choice, object_model):
        if player_choice in object_model.container_inventory.keys():
            if object_model.model == ObjectConstants.VALUABLES:
                # adding algoritm for different valuable amounts
                self.player_inventory_dict['purse'].update({player_choice: object_model.container_inventory[player_choice]})
                del object_model.container_inventory[player_choice]
            elif object_model.model == WeaponConstant.WEAPON:
                #choice to equip
                pass
            else:
                self.player_inventory_dict['bag'].update({player_choice: object_model.container_inventory[player_choice]})
                del object_model.container_inventory[player_choice]

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

    def get_map_tile_ahead(self, tile_x_y):
        x, y = tile_x_y
        direction_step = {NavigationConstants.NORTH: (0, -1), NavigationConstants.SOUTH: (0, +1),
                          NavigationConstants.EAST: (+1, 0), NavigationConstants.WEST: (-1, 0)}

        xx, yy = direction_step[self.player_move_dict['direction']][0], direction_step[self.player_move_dict['direction']][1]
        tile_ahead = self.get_map_tile(tile_x_y=((x + xx), (y + yy)))
        return tile_ahead

    def get_tile_message(self, tile_position, tile_key, object_item=None):
        tile_message = self.look_search.build_message(tile_key=tile_key, tile_position=tile_position, object_item=object_item)
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

    def search_object(self, object_tile, search_object=None):
        tile_key = self.get_map_tile(tile_x_y=object_tile)
        tile_object = self.look_search.get_tile_object(tile_key=tile_key, object_item=search_object)
        object_message = ("{}".format(tile_object))
        return object_message, tile_key

    def open_container(self, tile_key):
        object_model = self.look_search.get_object_model(tile_key=tile_key)
        if object_model.model == ObjectConstants.CONTAINER:
            is_open = True
            while is_open is True:
                # print inventory
                # self.print_inventory(object_model=object_model)

                player_choice = input(self.cctemp.PLAYER_TAKE).upper()

                # take
                if len(object_model.container_inventory) == 0:
                    print('close')
                    is_open = False
                elif player_choice in PlayerCommands.PLAYER_EXIT:
                    print('close')
                    is_open = False
                else:
                    self.take_object_item(player_choice=player_choice, object_model=object_model)
                    is_open = False

    def print_inventory(self, object_model):
        inventory = object_model.container_inventory
        for k, v in inventory.items():
            print('[{}]: {}\n'.format(k, v))

class LookSearchServices(TileKeyConstants):
    def __init__(self):
        self.player_checks_dict = PlayerCharacter.checks_dict

    def skill_check(self, skill, dificulty_check):
        if skill >= dificulty_check:
            return True
        else:
            return False

    def get_prefix(self, tile_position):
        tile_set = {NavigationConstants.LEFT: [GameMessages.TO_YOUR, GameMessages.LEFT],
                    NavigationConstants.RIGHT: [GameMessages.TO_YOUR, GameMessages.RIGHT],
                    NavigationConstants.CENTER: [GameMessages.AHEAD_OF_YOU],
                    NavigationConstants.FORWARD: [GameMessages.AHEAD_OF_YOU]}
        prefix = "".join(tile_set[tile_position])
        return prefix

    def build_message(self, tile_position, tile_key, object_item):
        look_message = "{} {} {}".format(self.get_prefix(tile_position=tile_position),
                                         self.get_tile_object(tile_key=tile_key, object_item=object_item),
                                         self.get_message_color(tile_key=tile_key))
        return look_message

    def build_collission_message(self, tile_key):
        collission_message = "{} {}".format(self.get_tile_object(tile_key=tile_key),
                                         self.get_message_color(tile_key=tile_key))
        return collission_message

    def get_tile_object(self, tile_key, object_item=None):
        object_message_type = self.TILE_KEY_CONSTANTS_DICT[str(tile_key)]
        if object_item != None:
            if object_item in object_message_type[MessagesConstants.SEARCH][MessagesConstants.KEYWORDS]:
                skill_check = self.skill_check(skill=self.player_checks_dict['search'],
                                               dificulty_check=object_message_type['model'].search_level)
                if skill_check is True:
                    if object_message_type[MessagesConstants.SEARCH][MessagesConstants.CONTENTS] is None:
                        item_type = random.choice(list(object_message_type[MessagesConstants.SEARCH][MessagesConstants.DEFAULT]))
                        item_message = random.choice(object_message_type[MessagesConstants.SEARCH][MessagesConstants.DEFAULT][item_type])
                    else:
                        item_message = object_message_type[MessagesConstants.SEARCH][MessagesConstants.CONTENTS](object_model=object_message_type['model'])
                else:
                    item_message = random.choice(object_message_type[MessagesConstants.SEARCH][MessagesConstants.DEFAULT])
            else:
                item_message = random.choice(object_message_type[MessagesConstants.SEARCH][MessagesConstants.DEFAULT])
        else:
            if tile_key > 9:
                item_message = random.choice(object_message_type[MessagesConstants.MESSAGES])
            else:
                item_type = random.choice(list(object_message_type[MessagesConstants.MESSAGES]))
                item_message = random.choice(object_message_type[MessagesConstants.MESSAGES][item_type])
        return item_message

    def get_message_color(self, tile_key):
        object_message_type = self.TILE_KEY_CONSTANTS_DICT[str(tile_key)]
        if tile_key > 9:
            message_color = random.choice(list(object_message_type[MessagesConstants.COLOR]))
        else:
            color_type = random.choice(list(object_message_type[MessagesConstants.COLOR]))
            message_color = random.choice(object_message_type[MessagesConstants.COLOR][color_type])
        return message_color

    def get_object_model(self, tile_key):
        object_model = self.TILE_KEY_CONSTANTS_DICT[str(tile_key)][MessagesConstants.MODEL]
        return object_model


class CommandServices(object):

    def __init__(self):
        self.cn = CharacterNavigation()
        self.ch_interaction = CharacterInteraction()
        self.cctemp = CharacterControlTemplates()
        self.templates = Templates()
        self.inventory_services = InventoryServices()

    def player_command_breakdown(self, player_choice):

        player_command_dict = {'command': None, 'direction': None, 'move': None, 'object_item': None}

        player_split = re.split(': | |, |,', player_choice)
        for split in player_split:
            if split in PlayerCommands.PLAYER_COMMANDS_SET:
                player_command_dict['command'] = split

            if split in NavigationConstants.COMPASS_DIRECTIONS_LIST or split in NavigationConstants.DIRECTIONS_LIST:
                player_command_dict['direction'] = split

            if split in NavigationConstants.MOVE_CONVERTER_DICT.keys():
                player_command_dict['move'] = NavigationConstants.MOVE_CONVERTER_DICT[split]

            if split in ObjectConstants.OBJECTS_SET:
                player_command_dict['object_item'] = split

        return player_command_dict

    def player_command_execute(self, player_choice):
        is_single = True
        player_command_dict = self.player_command_breakdown(player_choice=player_choice)
        if player_command_dict['command']:
            if player_command_dict['direction'] or player_command_dict['object_item'] or player_command_dict['move']:
                is_single = False
            self.player_commands(player_command=player_command_dict, is_single=is_single)
        else:
            print(self.templates.VALID_ENTRY)

    def player_commands(self, player_command, is_single):
        command = player_command['command']

        player_command_dict = {'LOOK':  {'template': self.cctemp.PLAYER_LOOK,
                                     'command': self.ch_interaction.character_look
                                     },
                               'TURN': {'template': self.cctemp.PLAYER_DIRECTIONS,
                                        'command': self.cn.get_player_direction
                                        },
                               'SEARCH': {'template': self.cctemp.PLAYER_SEARCH,
                                        'command': self.ch_interaction.character_serach
                                        },
                               'MOVE': {'template': self.cn.move_player,
                                     'command': self.cn.move_player
                                     },
                               'TAKE': {'template': self.cctemp.PLAYER_TAKE,
                                        'command': self.ch_interaction.character_take
                                        },
                               'INVENTORY': {'template': self.cctemp.PLAYER_INVENTORY,
                                        'command': self.inventory_services.print_inventory
                                        },
                               'EXIT': {'template': self.cctemp.PLAYER_EXIT,
                                        'command': ''
                                        }
                               }

        if is_single is False:
            return player_command_dict[command]['command'](player_command)
        else:
            template = player_command_dict[command]['template']
            return player_command_dict[command]['command'](self.player_input(template=template))

    def player_input(self, template):
        player_input = input(template).upper()
        return player_input