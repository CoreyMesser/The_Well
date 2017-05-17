from level_maps.map_model import Maps, MapTemplate
from services_get_character import GetCharacter

class MapRenderer(object):

    def __init__(self):
        self.mps = Maps()
        self.mpstemp = MapTemplate()
        self.gc = GetCharacter()
        self.player_move_dict = self.gc.player_move_dict

    def get_map(self, current_level):
        level_map = current_level
        if current_level == 'LEVEL_00':
            level_map = self.mps.MAP_LEVEL_00
        return level_map

    def draw_map(self):
        current_level = self.player_move_dict['current_level']
        level_map = self.get_map(current_level=current_level)
        for cell in level_map:
            print()

        pass

    def map_tiles(self, cell):
        tile_dict = {0: ' ', 1: '#', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ',
                     8: {'NORTH': '^', 'SOUTH': 'v', 'WEST': '<', 'EAST': '>'}, 9: 'E'}
        if cell == 8:
            direction = self.player_move_dict['direction']
            tile = tile_dict[8][direction]
        else:
            tile = tile_dict[cell]
        return tile


