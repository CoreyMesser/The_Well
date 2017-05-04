import unittest
from unittest import TestCase
from mock import patch, sentinel, MagicMock
from character_pc import HealthPoints



class MockCharacterData(unittest.TestCase):
    character_dict = {'name': 'Lucy',
                      'species': 'DOG',
                      'species_size': 'M/C',
                      'sex': 'Female',
                      'faction': 'Loom',
                      'alg': 'CG',
                      'pocc': '',
                      'socc': None,
                      'exp_total': 42,
                      'exp_remaining': 5,
                      'natural_hp': 3,
                      'bonus_hp': 1,
                      'hp': 4,
                      'soak': 0,
                      'stuffing': 10,
                      'sanity': 5,
                      'str': 1,
                      'int': 3,
                      'dex': 1,
                      'con': 1,
                      'wis': 2,
                      'cha': 3,
                      # 'skills': {'MENTAL': {"athletics": 1},
                      #            'PHYSICAL': {"drive": 1},
                      #            'SOCIAL': {"animal kinship": 2,
                      #                       "bluff": 2,
                      #                       "empathy": 2,
                      #                       "streetwise": 2,
                      #                       "persuasion": 2}},
                      # 'merits': {{'the brain': [6, 'int', 1]}, {'lucky': [4, 'probability', 2]}},
                      # 'flaws': {{'one eye': [3, 'attack_power', 1]}, {'clutz': [3, 'physical', 1]}, {'weak': [4, 'str', 1]}}
                      }

class HealthPointsUT(MockCharacterData):
    # # @patch('character_pc.HealthPoints.get_hp', 'hp_adjust', sentinel.hp_adjust)
    # @patch('character_pc.HealthPoints', 'HealthPoints')
    # @patch('character_pc.HealthPoints.character_dict', 'character_dict', sentinel.character_dict)
    # def test_get_hp(self, m):
    #     sentinel.character_dict = MockCharacterData.character_dict
    #     m.hp_adjust = 5
    #     HealthPoints.get_hp('HealthPoints_mock')
    #     assert MockCharacterData.character_dict['hp'] == 6
    #
    @patch('character_pc.HealthPoints')
    # @patch('character_pc.HealthPoints.character_dict')
    def test_bonus_hp(self, mock_health_points):

        mock_health_points.get_hp.return_value = 3





    # def test_bonus_hp(self):
    #     hp_test = HealthPoints(MockCharacterData)
    #     result = hp_test.hp_bonuses()
    #     print(result)



if __name__ == '__main__':
    hp_ut = HealthPointsUT()
    hp_ut.test_bonus_hp()
