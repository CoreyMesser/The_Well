from models import CharacterModels, PlayerCharacter

class GetCharacter(object):

    def __init__(self):
        self.cm = CharacterModels()

    def initialize_character(self, char_id):
        player_move_dict = self.cm.PLAYER_MOVE_DICT
        player_move_dict['character_id'] = char_id
        # establish skills/stats
        # establish combat tables
        # establish move tables
        return player_move_dict

class InventoryServices(object):

    def __init__(self):
        self.player_move_dict = CharacterModels.PLAYER_MOVE_DICT
        self.player_inventory_dict = CharacterModels.PLAYER_INVENTORY_DICT
        self.player_skills_dict = PlayerCharacter.skills_dict

    def print_inventory(self, something=None):
        print("Purse: {} \n ᗘᗘᗘᗛᗛᗛ \n Inventory: {} \n ᗘᗘᗘᗛᗛᗛ \n Equipped: ".format(
            self.print_contents(contents=self.player_inventory_dict['purse']),
            self.print_contents(contents=self.player_inventory_dict['bag'])))

    def print_contents(self, contents):
        if len(contents) > 0:
            for k, v in contents.items():
                return "[{}] : {} \n".format(k.upper(), v)
        else:
            return '0'
