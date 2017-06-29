import os


class Constants(object):
    CANCEL = 'CANCEL'
    SWITCH = 'SWITCH'

class MeritsFlawsConstants(object):
    MENTAL = 'MENTAL'
    PHYSICAL = 'PHYSICAL'
    SOCIAL = 'SOCIAL'
    STATS = 'STATS'
    CHANGE_LIST = 'CHANGE LIST'

class SpeciesConstants(object):
    LAND = 'LAND'
    AIR = 'AIR'

class NavigationConstants(object):
    NORTH = 'NORTH'
    SOUTH = 'SOUTH'
    EAST = 'EAST'
    WEST = 'WEST'
    UP = 'UP'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
    FORWARD = 'FORWARD'
    BACKWARDS = 'BACKWARDS'
    CENTER = 'CENTER'
    DIRECTIONS_LIST = [LEFT, RIGHT, CENTER, FORWARD, BACKWARDS, UP, DOWN]
    COMPASS_DIRECTIONS_LIST = [NORTH, EAST, SOUTH, WEST]
    DIRECTIONS_DICT = {NORTH: NORTH, SOUTH: SOUTH, EAST: EAST, WEST: WEST, 'N': NORTH, 'S': SOUTH, 'E':EAST, 'W': WEST}
    COMPASS_DIRECTIONS_INTERPRETER = {NORTH: {WEST: LEFT, EAST: RIGHT, SOUTH: BACKWARDS}, 
                                      EAST: {NORTH: LEFT, SOUTH: RIGHT, WEST: BACKWARDS},
                                      SOUTH: {EAST: LEFT, WEST: RIGHT, NORTH: BACKWARDS},
                                      WEST: {SOUTH: LEFT, NORTH: RIGHT, EAST: BACKWARDS}}
    MOVE_CONVERTER_DICT = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}

class MapConstants(object):
    LEVEL_00 = 'MAP_LEVEL_00'
    LEVEL_00_ITEMS = 'MAP_LEVEL_00_ITEMS'

class TileConstants(object):
    pass

class PlayerCommands(object):
    MOVE = 'MOVE'
    TURN = 'TURN'
    CLIMB = 'CLIMB'
    JUMP = 'JUMP'
    LOOK = 'LOOK'
    SEARCH = 'SEARCH'
    USE = 'USE'
    TAKE = 'TAKE'
    INVENTROY = 'INVENTORY'
    EQUIP = 'EQUIP'
    UNEQUIP = 'UNEQUIP'
    ATTACK = 'ATTACK'
    BLOCK = 'BLOCK'
    FLEE = 'FLEE'
    PLAYER_COMMANDS_SET = {'MOVE', 'TURN', 'JUMP', 'LOOK', 'SEARCH', 'USE', 'TAKE',
                           'INVENTORY', 'EQUIP', 'UNEQUIP', 'ATTACK', 'BLOCK', 'FLEE'}