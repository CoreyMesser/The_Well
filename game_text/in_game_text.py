from constants import MessagesConstants, ObjectConstants
from models import ContainerCrate, WeaponKnife, FloorModel


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
    model = None
    messages = {}
    color = {}
    search = {}

    def print_inventory(self, object_model):
        inventory = object_model.container_inventory
        if len(object_model.container_inventory) > 0:
            print(['{} Inside you find: \n'.format(ContainerCrate().get_description())])
            for k, v in inventory.items():
                print('[{}]: {}\n'.format(k.upper(), v))
        else:
            print('{}. But the {} is empty.'.format(ContainerCrate().get_description(), object_model.model))


class CollissionMessages(InGameMessages):

    messages = {'wall': ["Your face cracks hard against the unyeilding product of thousands of years of compression.",
                         "You grunt as you rebound off the wall, flushed with momentary embarassment until you "
                         "realize there is no one there to see your folly."]}
    color = {'none': ['', ''], 'wall': ["You should probably consider walking around solid objects from now on.",
                                        "Perhaps you need to pay a bit more attention to your surroundings."]}

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

    search = {'default': {
        'stone': ["Only a geologist would search cold stone for answers...", "Perhaps erosion will unveil something within...",
                  "Looks like... granite? You wished you would have paid more attention to uncle Susan's mineral obsession."],
        'earth': ["You are already underground, is there a point to digging further?",
                  "Smells like... damp soil with a hint of despair",
                  "Uncle Susan would have paid handsomely for this rich earth."]}
    }


class FloorMessages(InGameMessages):
    model = FloorModel()

    messages = {'stone': ["the floor is strewn with bits of chunky gravel over hard rough stone.",
                          "brutal scores left the flagstones of the floor cracked and shattered."],
                'damp_stone': ["a slick substance coats the floor making footing treacherous.",
                               "water trickles across the floor disappearing into the darkness."],
                'earthen': ["soft earth makes up the floor.", "loose gravel covers the floor."]}

    color = {'none': ['', ''],
             'hard': ["Your feet already complain about the punishment.",
                      "As if someone had designed the floor after hearing the description from a bedridden octogenarian."],
             'soft': ["You can't imagine staying upright on it for too long.", "You will never take boots for granted again."]}

    search = {'keywords': (ObjectConstants.FLOOR, ObjectConstants.GROUND, ObjectConstants.TILE),
              'contents': None,
              'default': {
        'stone': ["Only a geologist would search cold stone for answers...", "Perhaps erosion will unveil something within...",
                  "Looks like... granite? You wished you would have paid more attention to uncle Susan's mineral obsession."],
        'earth': ["You are already underground, is there a point to digging further?",
                  "Smells like... damp soil with a hint of despair",
                  "Uncle Susan would have paid handsomely for this rich earth."]}
    }


class ContainerMessages(InGameMessages):
    model = ContainerCrate()

    messages = {'crate': ["Rotted and waterlogged a near formless mass of wood rests against a wall."]}

    color = {'crate': ["In a surrealists eye the shape generally resembles a box."]}

    search = {'keywords': ContainerCrate.keywords, 'inventory': {WeaponKnife},
              'contents': InGameMessages().print_inventory,
              'default': {'crate': ["You are not quite sure what you are looking at, but you can be sure your search yielded little results",
                          "You would have probably found something if you had been paying attention."]}}

class EntranceMessages(InGameMessages):
    messages = {'start': ["the muddy soup trails after you all that is left of a once deep well.",
                          "the foul mud clings to you with fervor."]}

    color = {'grateful': ["You can't decide whether to be grateful for the slop, or concerned that it is caked in your wounds.",
             "You wipe the stinking mess from your face wishing ironically for the very thing in which you sway."]}


class TileKeyConstants(object):
    TILE_KEY_CONSTANTS_DICT = {'0': {MessagesConstants.MODEL: FloorMessages.model,
                                     MessagesConstants.MESSAGES: FloorMessages.messages,
                                     MessagesConstants.COLOR: FloorMessages.color,
                                     MessagesConstants.SEARCH: FloorMessages.search},
                               '1': {MessagesConstants.MODEL: WallMessages.model,
                                     MessagesConstants.MESSAGES: WallMessages.messages,
                                     MessagesConstants.COLOR: WallMessages.color,
                                     MessagesConstants.SEARCH: WallMessages.search},
                               '10': {MessagesConstants.MESSAGES: WallMessages.messages['stone'],
                                      MessagesConstants.COLOR: WallMessages.color['hard'],
                                      MessagesConstants.SEARCH: WallMessages.search},
                               '2': {MessagesConstants.MODEL: ContainerMessages.model,
                                     MessagesConstants.MESSAGES: ContainerMessages.messages,
                                     MessagesConstants.COLOR: ContainerMessages.color,
                                     MessagesConstants.SEARCH: ContainerMessages.search},
                               '9': {MessagesConstants.MESSAGES: EntranceMessages.messages,
                                     MessagesConstants.COLOR: EntranceMessages.color}}