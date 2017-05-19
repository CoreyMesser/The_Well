from level_maps.map_model import Maps, MapTemplate
from services_get_character import GetCharacter
import copy

class MapRenderer(object):

    def __init__(self):
        self.mps = Maps()
        self.mpstemp = MapTemplate()
        self.mtc = MapTileConstants()
        self.mps_clean = copy.deepcopy(Maps())
        self.gc = GetCharacter()
        # self.player_move_dict = self.gc.player_move_dict

    def get_map(self, player_move_dict):
        current_level = player_move_dict['current_level']
        clean_map = 0
        if current_level == 'LEVEL_00':
            clean_map = self.mps.MAP_LEVEL_00
        if current_level == 'LEVEL_01':
            clean_map = self.mps.MAP_LEVEL_01
        return clean_map

    def level_map_list(self, player_move_dict):
        level_map = []
        level_map_list = self.get_map(player_move_dict=player_move_dict)
        for entry in level_map_list:
            level_map.append(entry)
        return level_map

    def draw_character_position(self, player_move_dict):
        level_map = self.level_map_list(player_move_dict=player_move_dict)
        clean_map = self.get_map(player_move_dict=player_move_dict)

        player_move = player_move_dict['location']
        path = player_move_dict['path']

        move_index = self.mpstemp.MAP_COORDINATES.index(player_move)

        previous_move = path[-2]
        previous_index = self.mpstemp.MAP_COORDINATES.index(previous_move)
        previous_tile = clean_map[previous_index]

        level_map.insert(move_index, 8)
        level_map.pop(move_index + 1)

        level_map.insert(previous_index, previous_tile)
        level_map.pop(previous_index + 1)

        return level_map

    def draw_map(self, player_move_dict):

        level_map = self.draw_character_position(player_move_dict=player_move_dict)

        cell_print_count = 0
        rendered_map = []

        for cell in level_map:
            tiles = self.map_tiles(cell=cell, direction=player_move_dict['direction'])
            if cell_print_count == 0:
                rendered_map.append(self.mtc.BORDER)
                rendered_map.append(tiles)
            elif cell_print_count <= 5:
                rendered_map.append(tiles)
            else:
                rendered_map.append(self.mtc.BORDER)
                rendered_map.append(self.mtc.NEW_LINE)
                rendered_map.append(self.mtc.BORDER)
                rendered_map.append(tiles)
                cell_print_count = 0
            cell_print_count += 1
        rendered_map.append((self.mtc.BORDER))
        for tile in rendered_map:
            print(tile, end='')

    def map_tiles(self, cell, direction):
        tile_dict = {0: '  ', 1: '[]', 2: '  ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: '==', 8: ' ',
                     9: 'EN'}
        if cell == 8:
            direction = direction
            tile = self.mtc.PLAYER_ICON[direction]
        else:
            tile = tile_dict[cell]
        return tile

class MapTileConstants(object):

    BORDER = '|'
    NEW_LINE = '\n'
    PLAYER_ICON = {'NORTH': ' ^', 'SOUTH': 'v ', 'WEST': ' <', 'EAST': '> '}
