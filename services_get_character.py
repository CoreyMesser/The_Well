from models import CharacterModels

class GetCharacter(object):

    def __init__(self):
        self.cm = CharacterModels()
        self.player_move_dict = self.cm.PLAYER_MOVE_DICT

    def get_character(self, char_id):
        self.player_move_dict['character_id'] = char_id
        # establish skills/stats
        # establish combat tables
        # establish move tables
