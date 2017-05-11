import unittest
from unittest import TestCase
from mock import patch, sentinel, MagicMock
from character_pc import HealthPoints
from models import Character, CharacterMeritsFlaws, CharacterSkills, SpeciesDict, MeritsFlawsDicts, OCCs, MeritsFlaws
from services import PrinterServices
from database_service import db_session



class MockCharacterData(unittest.TestCase):
    character_dict = {'name': 'Lucy',
                      'species': 'DOG',
                      'species_size': 'M/C',
                      'sex': 'Female',
                      'faction': None,
                      'alg': 'CG',
                      'pocc': 'temp',
                      'socc': 'temp',
                      'exp_total': 42,
                      'exp_remaining': 42,
                      'natural_hp': 4,
                      'bonus_hp': 1,
                      'hp': 5,
                      'soak': 0,
                      'stuffing': 10,
                      'sanity': 5,
                      'str': 1,
                      'int': 4,
                      'dex': 1,
                      'con': 1,
                      'wis': 1,
                      'cha': 3,
                      'merits': {},
                      'flaws': {}
                      }

    def test_db_merits_insert(self):
        db = db_session()
        db_cmf = CharacterMeritsFlaws()
        merits = 'weaver'
        merit_instance = db.query(MeritsFlaws).filter_by(merits_flaws=merits).first()
        db_cmf.character_id = 1
        db_cmf.merits_01 = merit_instance.id
        db.add(db_cmf)
        db.commit()

    def test_db_merits_query(self):
        db = db_session()
        db_cmf = CharacterMeritsFlaws()
        cmf_m_id = CharacterMeritsFlaws.merits_01
        merit_instance = db.query(MeritsFlaws).filter_by(id=cmf_m_id).first()
        print(merit_instance.merits_flaws, merit_instance.merits_flaws_cost, merit_instance.attribute, merit_instance.attribute_modifier)

    def test_store_character_session(self):
        db = db_session()
        db_char = Character()
        db_char.name = self.character_dict['name']
        db_char.species = self.character_dict['species']
        db_char.species_size = self.character_dict['species_size']
        db_char.sex = self.character_dict['sex']
        db_char.faction = self.character_dict['faction']
        db_char.alg = self.character_dict['alg']
        db_char.pocc = self.character_dict['pocc']
        db_char.socc = self.character_dict['socc']
        db_char.exp_total = self.character_dict['exp_total']
        db_char.exp_remaining = self.character_dict['exp_remaining']
        db_char.natural_hp = self.character_dict['natural_hp']
        db_char.hp = self.character_dict['hp']
        db_char.soak = self.character_dict['soak']
        db_char.stuffing = self.character_dict['stuffing']
        db_char.sanity = self.character_dict['sanity']
        db_char.str = self.character_dict['str']
        db_char.int = self.character_dict['int']
        db_char.dex = self.character_dict['dex']
        db_char.con = self.character_dict['con']
        db_char.wis = self.character_dict['wis']
        db_char.cha = self.character_dict['cha']
        db_char.code = 1
        db.add(db_char)
        db.commit()


if __name__ == '__main__':
    m_cd = MockCharacterData()
    m_cd.test_store_character_session()
