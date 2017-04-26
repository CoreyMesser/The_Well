import random, os
from character_pc import PlayerCharacter
from templates.templates import Templates


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
        #write to db each loop
        pass

if __name__ == '__main__':
    ch = CharacterCreation()
    ch.__init__()

