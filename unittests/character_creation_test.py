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

class HealthPointsUT(unittest.TestCase):
    def some_return(self):
        return [1, 2, 3]

    def other_return(self):
        return [4, 5, 6]

    @patch('__main__.ProductionClass.something')
    @patch('__main__.ProductionClass.otherthing')
    def test_production_class(self, other_mock, some_mock):
        some_mock.return_value = self.some_return()
        other_mock.return_value = self.other_return()

        p = ProductionClass()

        z = p.method()
        print('done: {}'.format(str(z)))



if __name__ == '__main__':
    hp_ut = HealthPointsUT()
    hp_ut.test_bonus_hp()
