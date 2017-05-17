from level_maps.map_model import Maps, MapTemplate
from services_get_character import GetCharacter

class MapRenderer(object):

    def __init__(self):
        self.mps = Maps()
        self.mpstemp = MapTemplate()
        self.mtc = MapTileConstants()
        self.gc = GetCharacter()
        self.player_move_dict = self.gc.player_move_dict

    def get_map(self, current_level):
        level_map = current_level
        if current_level == 'LEVEL_00':
            level_map = self.mps.MAP_LEVEL_00
        if current_level == 'LEVEL_01':
            level_map = self.mps.MAP_LEVEL_01
        return level_map

    def draw_character_position(self):
        current_level = self.player_move_dict['current_level']
        level_map = self.get_map(current_level=current_level)
        player_move = self.player_move_dict['location']

        move_index = self.mpstemp.MAP_COORDINATES.index(player_move)
        level_map.insert(move_index, 8)
        level_map.pop(move_index + 1)

        return level_map

    def draw_map(self):

        level_map = self.draw_character_position()

        cell_print_count = 0
        rendered_map = []

        for cell in level_map:
            tiles = self.map_tiles(cell=cell)
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

    def map_tiles(self, cell):
        tile_dict = {0: '  ', 1: '[]', 2: '  ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: '==', 8: ' ',
                     9: 'EN'}
        if cell == 8:
            direction = self.player_move_dict['direction']
            tile = self.mtc.PLAYER_ICON[direction]
        else:
            tile = tile_dict[cell]
        return tile

class MapTileConstants(object):

    BORDER = '|'
    NEW_LINE = '\n'
    PLAYER_ICON = {'NORTH': ' ^', 'SOUTH': 'v ', 'WEST': ' <', 'EAST': '> '}
