import random, os
from character_pc import PlayerCharacter, Species, HealthPoints, Stats, Skills, MeritsFlaws, POCC
from templates.templates import Templates
from services import CharacterStoreSession
from models import Character, CharacterCode, Skill


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
        self.hp = HealthPoints()
        self.sp = Species()
        self.sts = Stats()
        self.sk = Skills()
        self.mf = MeritsFlaws()
        self.po = POCC()
        self.db_cs = CharacterStoreSession()
        self.character_dict = self.pc.character_dict
        self.skills_dict = self.pc.skills_dict
        self.setup()
        self.character_creation()

    def character_creation(self):
        finished = False

        while finished is False:
            return_menu = False
            self.clear_screen()
            self.hp.update_hp()
            print(self.template.print_char_sheet(self.character_dict, self.skills_dict))
            print('\n'+'\/'*20+'\n \n')
            player_choice = input("ᗘᗘᗘ Please Enter the stat you would like to adjust: \n >> ").lower()
            if player_choice == 'name':
                self.character_dict['name'] = input(self.template.NAME)
            if player_choice == 'sex':
                self.character_dict['sex'] = input(self.template.SEX)
            if player_choice == 'species':
                while self.character_dict['species'] is None or return_menu is False:
                    return_menu = self.sp.get_species()
            if player_choice == 'faction':
                self.character_dict['faction'] = input(self.template.FACTIONS)
            if player_choice == 'alg':
                self.character_dict['alg'] = input(self.template.ALIGNMENT)
            if player_choice == 'pocc':
                self.po.get_pocc()
            if player_choice == 'socc':
                self.character_dict['socc'] = input(self.template.SECONDARY_OCC)
            if player_choice == 'hp':
                self.hp.get_hp()
            if player_choice == 'stuff':
                print(self.template.STUFFING)
            if player_choice in self.pc.character_stats:
                self.sts.get_stats(player_choice)
            if player_choice == 'skills':
                while return_menu is False:
                    return_menu = self.sk.get_skills()
            if player_choice == 'merits':
                while return_menu is False:
                    return_menu = self.mf.get_merits()
            if player_choice == 'flaws':
                while return_menu is False:
                    return_menu = self.mf.get_flaws()
            if player_choice == 'finished':
                finished = True

        self.db_cs.store_character_session()
