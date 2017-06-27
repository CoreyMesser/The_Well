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
    DIRECTIONS_DICT = {'NORTH': 'NORTH', 'SOUTH': 'SOUTH', 'EAST':'EAST', 'WEST': 'WEST', 'N': 'NORTH', 'S': 'SOUTH', 'E':'EAST', 'W': 'WEST'}
    MOVE_CONVERTER_DICT = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}

class MapConstants(object):
    LEVEL_00 = 'MAP_LEVEL_00'
    LEVEL_00_ITEMS = 'MAP_LEVEL_00_ITEMS'