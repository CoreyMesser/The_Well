import os

from character_pc import PlayerCharacter, Species, HealthPoints, Stats, CharacterSkillsGenerator, MeritsFlawsGenerator, POCC, SOCC, CharacterStoreSession
from templates.templates import Templates
from services import PrinterServices
from database_service import db_session


class Introduction(object):
    def intro(self):
        print(Templates.BANNER)
        print(Templates.INTRO)
        input('ᗛᗛᗛ Press Return to continue ᗘᗘᗘ')
        cc = CharacterCreation()
        cc.__init__()


class CharacterCreation(object):

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def __init__(self):
        self.template = Templates()
        self.hp = HealthPoints()
        self.pc = PlayerCharacter()
        self.sp = Species()
        self.sts = Stats()
        self.sk = CharacterSkillsGenerator()
        self.mf = MeritsFlawsGenerator()
        self.po = POCC()
        self.so = SOCC()
        self.ps = PrinterServices()
        self.db_cs = CharacterStoreSession()
        self.character_dict = self.pc.character_dict
        self.skills_dict = self.pc.skills_dict
        self.character_creation()

    def character_creation(self):
        finished = False

        while finished is False:
            return_menu = False
            self.clear_screen()
            self.hp.update_hp()
            print(self.ps.print_char_sheet(self.character_dict, self.skills_dict))
            print('\n'+'\/'*20+'\n \n')
            player_choice = input("ᗘᗘᗘ Please Enter the stat you would like to adjust: \n >> ").lower()
            if player_choice == 'name':
                self.character_dict['name'] = input(self.template.NAME)
            if player_choice == 'sex':
                self.character_dict['sex'] = input(self.template.SEX)
            if player_choice == 'species':
                species = input(self.template.SPECIES).upper()
                self.ps.print_species_list(species)
                species_l_choice = input(self.template.SPECIES_SELECT).upper()
                return_menu = self.sp.get_species(species=species, species_l_choice=species_l_choice)
            if player_choice == 'faction':
                self.character_dict['faction'] = input(self.template.FACTIONS)
            if player_choice == 'alg':
                self.character_dict['alg'] = input(self.template.ALIGNMENT)
            if player_choice == 'pocc':
                self.po.print_pocc()
                select_pocc = input(self.template.SELECT_POCC).lower()
                self.po.get_pocc(select_pocc=select_pocc)
            if player_choice == 'socc':
                self.so.check_required_pocc()
            if player_choice == 'hp':
                hp_adjust = self.hp.get_hp_player_choice()
                self.hp.get_hp(hp_adjust=hp_adjust)
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
