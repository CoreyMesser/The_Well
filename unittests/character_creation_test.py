import unittest
from unittest import TestCase
from models import Character, CharacterMeritsFlaws, CharacterSkills, SpeciesDict, MeritsFlawsDicts, OCCs, MeritsFlaws, PoccDb, SoccDb
from database_service import db_session
from templates.templates import Templates, CharacterControlTemplates
from constants import NavigationConstants
from level_maps.map_model import MapTemplate, Maps, MapConstants




class MockCharacterData(unittest.TestCase):
    character_dict = {'name': 'Lucy',
                      'species': 'DOG',
                      'species_size': 'M/C',
                      'sex': 'Female',
                      'faction': None,
                      'alg': 'CG',
                      'pocc': {'tech': 1},
                      'socc': {'hacker': 1},
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
                      'merits': {'weaver': 1, 'lucky': 1, 'witty': 1},
                      'flaws': {}
                      }

    skills_dict = {"academics": 0,
                   "computer": 3,
                   "concentration": 0,
                   "crafting": 3,
                   "investigation": 0,
                   "medicine": 0,
                   "occult": 0,
                   "politics": 0,
                   "science": 3,
                   "athletics": 0,
                   "brawl": 0,
                   "demolitions": 0,
                   "drive": 0,
                   "firearms": 3,
                   "larceny": 3,
                   "ranged weaponry": 0,
                   "ride": 0,
                   "stealth": 0,
                   "survival": 0,
                   "weaponry": 3,
                   "animal kinship": 0,
                   "bluff": 3,
                   "empathy": 0,
                   "expression": 0,
                   "intimidate": 0,
                   "persuasion": 3,
                   "social contacts": 0,
                   "streetwise": 0,
                   "subterfuge": 3
                   }

    def test_db_merits_insert(self, char_id):
        db = db_session()
        db_cmf = CharacterMeritsFlaws()
        # merits = 'weaver'
        # merit_instance = db.query(MeritsFlaws).filter_by(merits_flaws=merits).first()
        # db_cmf.character_id = 1
        # db_cmf.merits_01 = merit_instance.id
        db_cmf.character_id = char_id
        merit_counter = 1
        for merits in self.character_dict['merits']:
            merit_instance = db.query(MeritsFlaws).filter_by(merits_flaws=merits).first()
            if merit_counter == 1:
                db_cmf.merits_01 = merit_instance.id
            elif merit_counter == 2:
                db_cmf.merits_02 = merit_instance.id
            elif merit_counter == 3:
                db_cmf.merits_03 = merit_instance.id
            elif merit_counter == 4:
                db_cmf.merits_04 = merit_instance.id
            elif merit_counter == 5:
                db_cmf.merits_05 = merit_instance.id
            merit_counter += 1
        db.add(db_cmf)
        db.commit()

    def test_db_merits_query(self):
        db = db_session()
        db_cmf = CharacterMeritsFlaws()
        cmf_m_id = CharacterMeritsFlaws.merits_01
        merit_instance = db.query(MeritsFlaws).filter_by(id=cmf_m_id).first()
        print(merit_instance.merits_flaws, merit_instance.merits_flaws_cost, merit_instance.attribute, merit_instance.attribute_modifier)
        
    def test_store_character_skills_session(self, char_id):
        db = db_session()
        db_sk = CharacterSkills()
        db_sk.character_id = char_id
        db_sk.academics = self.skills_dict['academics']
        db_sk.computer = self.skills_dict['computer']
        db_sk.concentration = self.skills_dict['concentration']
        db_sk.crafting = self.skills_dict['crafting']
        db_sk.investigation = self.skills_dict['investigation']
        db_sk.medicine = self.skills_dict['medicine']
        db_sk.occult = self.skills_dict['occult']
        db_sk.politics = self.skills_dict['politics']
        db_sk.science = self.skills_dict['science']
        db_sk.athletics = self.skills_dict['athletics']
        db_sk.brawl = self.skills_dict['brawl']
        db_sk.demolitions = self.skills_dict['demolitions']
        db_sk.drive = self.skills_dict['drive']
        db_sk.firearms = self.skills_dict['firearms']
        db_sk.larceny = self.skills_dict['larceny']
        db_sk.ranged_weaponry = self.skills_dict['ranged weaponry']
        db_sk.ride = self.skills_dict['ride']
        db_sk.stealth = self.skills_dict['stealth']
        db_sk.survival = self.skills_dict['survival']
        db_sk.weaponry = self.skills_dict['weaponry']
        db_sk.animal_kinship = self.skills_dict['animal kinship']
        db_sk.bluff = self.skills_dict['bluff']
        db_sk.empathy = self.skills_dict['empathy']
        db_sk.expression = self.skills_dict['expression']
        db_sk.intimidate = self.skills_dict['intimidate']
        db_sk.persuasion = self.skills_dict['persuasion']
        db_sk.social_contacts = self.skills_dict['social contacts']
        db_sk.streetwise = self.skills_dict['streetwise']
        db_sk.subterfuge = self.skills_dict['subterfuge']
        db.add(db_sk)
        db.commit()


    def test_store_character_session(self):
        db = db_session()
        db_char = Character()
        db_char.name = self.character_dict['name']
        db_char.species = self.character_dict['species']
        db_char.species_size = self.character_dict['species_size']
        db_char.sex = self.character_dict['sex']
        db_char.faction = self.character_dict['faction']
        db_char.alg = self.character_dict['alg']
        pocc = ''.join(self.character_dict['pocc'].keys())
        pocc_instance = db.query(PoccDb).filter_by(pocc=pocc).first()
        db_char.pocc = pocc_instance.id
        socc = ''.join(self.character_dict['socc'].keys())
        socc_instance = db.query(SoccDb).filter_by(socc=socc).first()
        db_char.socc = socc_instance.id
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

        char_id = db_char.id

        self.test_db_merits_insert(char_id=char_id)
        self.test_store_character_skills_session(char_id=char_id)

    def test_row_to_dict(self):
        db = db_session()
        for c in db.query(Character).filter(Character.id == 9):
            character_dict = c.__dict__
        print(character_dict)
        for s in db.query(CharacterSkills).filter(Character.id == 9):
            skills_dict = s.__dict__
        print(skills_dict)
        for mf in db.query(CharacterMeritsFlaws).filter(CharacterMeritsFlaws.id == 9):
            mf_dict = mf.__dict__
        print(mf_dict)



class PrintCompletedCharacterSheet(object):
    character_sheet = Character()
    db = db_session()

    def create_character_dict_from_db(self, char_id=None):
        db = db_session()
        # char_id = char_id
        for c in db.query(Character).filter(Character.id == 9):
            character_dict = c.__dict__
        for s in db.query(CharacterSkills).filter(Character.id == 9):
            skills_dict = s.__dict__
        for mf in db.query(CharacterMeritsFlaws).filter(CharacterMeritsFlaws.id == 9):
            mf_dict = mf.__dict__

        return character_dict, skills_dict, mf_dict

    def create_character_stats(self, character_dict):
        db = db_session()
        pocc_select = db.query(PoccDb).filter_by(id=character_dict['pocc']).first()
        pocc_entry = ''.join([pocc_select.pocc.upper(), ': ', pocc_select.attribute_01, ' ', str(pocc_select.attribute_modifier_01),
                              ', ', pocc_select.attribute_02, ' ', str(pocc_select.attribute_modifier_02)])
        socc_select = db.query(SoccDb).filter_by(id=character_dict['socc']).first()
        if socc_select is not None:
            socc_entry = ''.join([socc_select.socc.upper(), ': ', socc_select.attribute, ' ', str(socc_select.attribute_modifier)])
        else:
            socc_entry = 'None'

        main_sheet = ["NAME:  {name} \n" \
                     "SPECIES:  {species} \n" \
                     "  SPECIES SZIE:  {species_size} \n" \
                     "SEX: {sex} \n" \
                     "FACTION:  {faction} \n" \
                     "ALIGNMENT:  {alg} \n".format(**character_dict),
                     "PRIMARY OCCUPATION: {} \n" \
                     "   SECOND OCCUPATION:  {} \n".format(pocc_entry, socc_entry),
                     "\n" \
                     "HP: {hp} \n" \
                     "STUFFING: {stuffing} \n" \
                     "SANITY: {sanity} \n" \
                     "SOAK: {soak} \n" \
                     "\n" \
                     "  ᗘᗘᗘ STATS  ᗛᗛᗛ\n" \
                     "ᗘ[STR] : {str} \n" \
                     " ᗘ[INT] : {int} \n" \
                     "ᗘ[DEX] : {dex} \n" \
                     " ᗘ[CON] : {con} \n" \
                     " ᗘ[WIS] : {wis} \n" \
                     " ᗘ[CHA] : {cha} \n" \
                     "\n".format(**character_dict)]
        return ''.join(main_sheet)

    def create_skills_stats(self, skills_dict):
        skills_sheet = ['\nᗘᗘᗘ SKILLS  ᗛᗛᗛ\n',
                        'ᗘᗘ MENTAL ᗛᗛ\n',
                        'ᗘ {academics} : [Academics]\n'.format(**skills_dict),
                        'ᗘ {computer} : [Computer]\n'.format(**skills_dict),
                        'ᗘ {concentration} : [Concentration]\n'.format(**skills_dict),
                        'ᗘ {crafting} : [Crafting]\n'.format(**skills_dict),
                        'ᗘ {investigation} : [Investigation]\n'.format(**skills_dict),
                        'ᗘ {medicine} : [Medicine]\n'.format(**skills_dict),
                        'ᗘ {occult} : [Occult]\n'.format(**skills_dict),
                        'ᗘ {politics} : [Politics]\n'.format(**skills_dict),
                        'ᗘ {science} : [Science ]\n \n'.format(**skills_dict),
                        'ᗘᗘ PHYSICAL ᗛᗛ\n'
                        'ᗘ {athletics} : [athletics]\n'.format(**skills_dict),
                        'ᗘ {brawl} : [brawl]\n'.format(**skills_dict),
                        'ᗘ {demolitions} : [demolitions]\n'.format(**skills_dict),
                        'ᗘ {drive} : [drive]\n'.format(**skills_dict),
                        'ᗘ {firearms} : [firearms]\n'.format(**skills_dict),
                        'ᗘ {larceny} : [larceny]\n'.format(**skills_dict),
                        'ᗘ {ranged_weaponry} : [ranged weaponry]\n'.format(**skills_dict),
                        'ᗘ {ride} : [ride]\n'.format(**skills_dict),
                        'ᗘ {stealth} : [stealth]\n'.format(**skills_dict),
                        'ᗘ {survival} : [survival]\n'.format(**skills_dict),
                        'ᗘ {weaponry} : [weaponry]\n \n'.format(**skills_dict),
                        'ᗘᗘ SOCIAL ᗛᗛ\n',
                        'ᗘ {bluff} : [bluff]\n'.format(**skills_dict),
                        'ᗘ {empathy} : [empathy]\n'.format(**skills_dict),
                        'ᗘ {expression} : [expression]\n'.format(**skills_dict),
                        'ᗘ {intimidate} : [intimidate]\n'.format(**skills_dict),
                        'ᗘ {persuasion} : [persuasion]\n'.format(**skills_dict),
                        'ᗘ {social_contacts} : [social contacts]\n'.format(**skills_dict),
                        'ᗘ {streetwise} : [streetwise]\n'.format(**skills_dict),
                        'ᗘ {subterfuge} : [subterfuge]\n'.format(**skills_dict)
                        ]
        return ''.join(skills_sheet)

    def create_mf_stats(self, mf_dict):
        db = db_session()
        merits_list = []
        flaws_list = []
        merit_counter = 1
        while merit_counter <=5:
            merit_row = mf_dict['merits_0{}'.format(merit_counter)]
            if merit_row is not None:
                mfd = db.query(MeritsFlaws).filter_by(id=merit_row).first()
                merits_list.append(''.join([mfd.merits_flaws.upper(), ': ', mfd.attribute, ', ', str(mfd.attribute_modifier), '\n']))

            flaw_row = mf_dict['flaws_0{}'.format(merit_counter)]
            if flaw_row is not None:
                ffd = db.query(MeritsFlaws).filter_by(id=flaw_row).first()
                flaws_list.append(''.join([ffd.merits_flaws.upper(), ': ', ffd.attribute, ', ', str(ffd.attribute_modifier), '\n']))

            merit_counter += 1

        merits_flaws_sheet = ''.join(['\nᗘᗘᗘ MERITS  ᗛᗛᗛ\n', ''.join(merits_list),
                        '\n \nᗘᗘᗘ FLAWS  ᗛᗛᗛ\n', ''.join(flaws_list)])

        return merits_flaws_sheet

    def print_character_sheet_from_db(self):
        character_dict, skills_dict, mf_dict = self.create_character_dict_from_db()
        char_stats = self.create_character_stats(character_dict=character_dict)
        char_skills = self.create_skills_stats(skills_dict=skills_dict)
        char_mf = self.create_mf_stats(mf_dict=mf_dict)
        print(char_stats, char_skills, char_mf)
        character = char_stats + char_skills + char_mf
        file_name = input('Please enter a file name: >>')
        f = open(file_name + '.txt', 'w')
        f.write(character)
        f.close()

class NavigationTEST(object):

    templates = Templates()
    cctemp = CharacterControlTemplates()
    nc = NavigationConstants()
    mps = Maps()
    mpsc = MapConstants()
    mpstemp = MapTemplate()
    player_move_dict = {'location': (1, 4), 'path': [], 'direction': 'NORTH', 'current_level': 'LEVEL_00'}

    def get_player_moves(self, player_choice):
        directions = self.nc.DIRECTIONS_DICT
        player_list = list(player_choice)
        player_move = 0
        for direction_check in player_list:
            if direction_check in directions:
                if directions[direction_check] == self.player_move_dict['direction']:
                    break
                else:
                    self.player_move_dict['direction'] = directions[direction_check]
                    break
        for move_check in player_list:
            if move_check in self.nc.MOVE_CONVERTER_DICT:
                player_move = self.nc.MOVE_CONVERTER_DICT[move_check]
                break
        return player_move

    def move_player(self):
        player_choice = '1:NORTH'
        return_menu = False

        move = self.get_player_moves(player_choice=player_choice)
        player_direction = self.player_move_dict['direction']
        x, y = self.player_move_dict['location']
        player_move = x, y

        while return_menu is False:
            if player_direction == 'NORTH':
                player_move = x, y - move
                return_menu = True
            if player_direction == 'SOUTH':
                player_move = x, y + move
                return_menu = True
            if player_direction == 'EAST':
                player_move = x - move, y
                return_menu = True
            if player_direction == 'WEST':
                player_move = x + move, y
                return_menu = True

        vaild_move = self.valid_player_move(player_move=player_move)
        if vaild_move is True:
            self.player_move_dict['location'] = player_move

    def valid_player_move(self, player_move):
        # self.player_move_dict['path'].append((x, y))
        valid_move = False
        current_level = self.player_move_dict['current_level']
        level_map = self.get_current_level_map(current_level=current_level)

        if player_move in self.mpstemp.MAP_COORDINATES:
            move_index = self.mpstemp.MAP_COORDINATES.index(player_move)
            level_map_check = level_map[move_index]
            if level_map_check == 0:
                valid_move = True
            if level_map_check == 1:
                # check what they ran into
                pass
            if level_map_check == 2:
                # searchable area
                pass

        return valid_move

    def get_current_level_map(self, current_level):
        level_map = current_level
        if current_level == 'LEVEL_00':
            level_map = self.mps.MAP_LEVEL_00
        return level_map

class MapRender(object):
    mps = Maps()
    mpsc = MapConstants()
    mpstemp = MapTemplate()
    player_move_dict = {'location': (1, 4), 'path': [], 'direction': 'NORTH', 'current_level': 'LEVEL_00'}

    def get_map(self, current_level):
        level_map = current_level
        if current_level == 'LEVEL_00':
            level_map = self.mps.MAP_LEVEL_00
        return level_map

    def draw_map(self):
        current_level = self.player_move_dict['current_level']
        level_map = self.get_map(current_level=current_level)
        for cell in level_map:
            tiles = self.map_tiles(cell=cell)
            print(tiles)

    def map_tiles(self, cell):
        tile_dict = {0: ' ', 1: '#', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ',
                     8: {'NORTH': '^', 'SOUTH': 'v', 'WEST': '<', 'EAST': '>'}, 9: 'E'}
        if cell == 8:
            direction = self.player_move_dict['direction']
            tile = tile_dict[8][direction]
        else:
            tile = tile_dict[cell]
        return tile




if __name__ == '__main__':
    nt = MapRender()
    nt.draw_map()
    