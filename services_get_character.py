from models import CharacterModels

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
