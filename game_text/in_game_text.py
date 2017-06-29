import random

class GameMessages(object):
    """
    message id is composed of three parts, where, what, id
    ie 00008001
    000 - generic
    08 - item
    001 - message id
    """

    TO_YOUR = "To your"
    AHEAD_OF_YOU = "Ahead of you"
    BEHIND_YOU = "Behind you"
    LEFT = " left"
    RIGHT = " right"

class InGameMessages(object):
    messages = {}
    color = {}
    search = {}

class WallMessages(InGameMessages):
    messages = {'stone': ["is a rough hewn stone wall marked with faint echos of chisel bits.",
                          "is a wall composed of large slabs of speckled gray stone."],
                'damp_stone': ["is a damp stone wall streaked with crawling moss.",
                               "water trickles down the stone wall making it dark with wet."],
                'earthen': ["is a crumbling earthen wall.", "is a wall that seems to have been carved out of the earth."]}

    color = {'none': ['', ''],
             'hard': ["Solidity is its very nature.",
                      "Even with a pick you'd be hard pressed to turn it to mineral."],
             'soft': ["It looks to buckle any moment.", "A sneeze may bring it down at any time."]}

class FloorMessages(InGameMessages):
    messages = {'stone': ["the floor is strewn with bits of chunky gravel over hard rough stone.",
                          "brutal scores left the flagstones of the floor cracked and shattered."],
                'damp_stone': ["a slick substance coats the floor making footing treacherous.",
                               "water trickles across the floor disappearing into the darkness."],
                'earthen': ["soft earth makes up the floor.", "loose gravel covers the floor."]}

    color = {'none': ['', ''],
             'hard': ["Your feet already complain about the punishment.",
                      "As if someone had designed the floor after hearing the description from a bedridden octogenarian."],
             'soft': ["You can't imagine staying upright on it for too long.", "You will never take boots for granted again."]}

class EntranceMessages(InGameMessages):
    messages = {'start': ["the muddy soup trails after you all that is left of a once deep well.",
                          "the foul mud clings to you with fervor."]}

    color = {'grateful': ["You can't decide whether to be grateful for the slop, or concerned that it is caked in your wounds.",
             "You wipe the stinking mess from your face wishing ironically for the very thing in which you sway."]}


class LookSearchMessages(object):
    TILE_KEY_CONSTANTS_DICT = {'0': {'messages': FloorMessages.messages, 'color': FloorMessages.color},
                                '1': {'messages': WallMessages.messages, 'color': WallMessages.color},
                                '10': {'messages': WallMessages.messages['stone'], 'color': WallMessages.color['hard']},
                                '9': {'messages': EntranceMessages.messages, 'color': EntranceMessages.color}}


    def get_prefix(self, tile_position):
        tile_set = {'LEFT': [GameMessages.TO_YOUR, GameMessages.LEFT],
                    'RIGHT': [GameMessages.TO_YOUR, GameMessages.RIGHT],
                    'CENTER': [GameMessages.AHEAD_OF_YOU]}
        prefix = "".join(tile_set[tile_position])
        return prefix

    def build_message(self, tile_position, tile_key, object_item):
        look_message = "{} {} {}".format(self.get_prefix(tile_position=tile_position),
                                          self.get_tile_object(tile_key=tile_key, object_item=object_item),
                                          self.get_message_color(tile_key=tile_key))
        return look_message

    def get_tile_object(self, tile_key, object_item=None):
        object_message_type = self.TILE_KEY_CONSTANTS_DICT[str(tile_key)]
        if object_item != None:
            item_message = random.choice(object_message_type['messages'][object_item])
        else:
            if tile_key > 9:
                item_message = random.choice(object_message_type['messages'])
            else:
                item_type = random.choice(list(object_message_type['messages']))
                item_message = random.choice(object_message_type['messages'][item_type])
        return item_message

    def get_message_color(self, tile_key):
        object_message_type = self.TILE_KEY_CONSTANTS_DICT[str(tile_key)]
        if tile_key > 9:
            message_color = random.choice(list(object_message_type['color']))
        else:
            color_type = random.choice(list(object_message_type['color']))
            message_color = random.choice(object_message_type['color'][color_type])
        return message_color


