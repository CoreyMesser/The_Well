import random, os
from character_pc import PlayerCharacter
from templates.templates import Templates
from database_service import Database
from models import Character, CharacterCode


class CharacterCreation(object):
    def setup(self):
        print(self.template.BANNER)
        print(self.template.INTRO)
        input('ᗛᗛᗛ Press Return to continue ᗘᗘᗘ')

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def __init__(self):
        self.template = Templates()
        self.pc = PlayerCharacter()
        self.character_dict = self.pc.character_dict
        self.setup()
        self.character_creation()

    def character_creation(self):
        finished = False

        while finished is False:
            return_menu = False
            self.clear_screen()
            self.pc.update_hp()
            print(self.template.print_char_sheet(self.character_dict))
            print('\n'+'\/'*20+'\n \n')
            player_choice = input("ᗘᗘᗘ Please Enter the stat you would like to adjust: \n >> ").lower()
            if player_choice == 'name':
                self.character_dict['name'] = input(self.template.NAME)
            if player_choice == 'sex':
                self.character_dict['sex'] = input(self.template.SEX)
            if player_choice == 'species':
                while self.character_dict['species'] is None or return_menu is False:
                    return_menu = self.pc.get_species()
            if player_choice == 'faction':
                self.character_dict['faction'] = input(self.template.FACTIONS)
            if player_choice == 'alg':
                self.character_dict['alg'] = input(self.template.ALIGNMENT)
            if player_choice == 'pocc':
                self.character_dict['pocc'] = input(self.template.PRIMARY_OCC)
            if player_choice == 'socc':
                self.character_dict['socc'] = input(self.template.SECONDARY_OCC)
            if player_choice == 'hp':
                self.pc.get_hp()
            if player_choice == 'stuff':
                print(self.template.STUFFING)
            if player_choice in self.pc.character_stats:
                self.pc.get_stats(player_choice)
            if player_choice == 'skills':
                while return_menu is False:
                    return_menu = self.pc.get_skills()
            if player_choice == 'merits':
                self.pc.get_merits()
            if player_choice == 'finished':
                finished = True

            self.store_session()

    def store_session(self):
        db = Database
        db.get_db()
        cc = PlayerCharacter()
        db_char = Character()
        db_char_code = CharacterCode()
        db_char.name = cc.character_dict['name']
        db_char.species = cc.character_dict['species']
        db_char.species_size = cc.character_dict['species_size']
        db_char.sex = cc.character_dict['sex']
        db_char.faction = cc.character_dict['faction']
        db_char.alg = cc.character_dict['alg']
        db_char.pocc = cc.character_dict['pocc']
        db_char.socc = cc.character_dict['socc']
        db_char.exp_total = cc.character_dict['exp_total']
        db_char.exp_remaining = cc.character_dict['exp_remaining']
        db_char.hp = cc.character_dict['hp']
        db_char.soak = cc.character_dict['soak']
        db_char.stuffing = cc.character_dict['stuffing']
        db_char.sanity = cc.character_dict['sanity']
        db_char.str = cc.character_dict['str']
        db_char.int = cc.character_dict['int']
        db_char.dex = cc.character_dict['dex']
        db_char.con = cc.character_dict['con']
        db_char.wis = cc.character_dict['wis']
        db_char.cha = cc.character_dict['cha']
        db_char.skills = cc.character_dict['skills']
        db_char.merits = cc.character_dict['merits']
        db_char.flaws = cc.character_dict['flaws']
        db_char_code.code = 1
        db.add(db_char)
        db.add(db_char_code)
        db.commit()

