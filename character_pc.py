import random, os
from templates.templates import Templates
from models import Character, CharacterMeritsFlaws, CharacterSkills, SpeciesDict, MeritsFlawsDicts, OCCs, MeritsFlaws
from services import PrinterServices
from database_service import db_session


class PlayerCharacter(object):
    character_dict = {'name': None,
                      'species': None,
                      'species_size': None,
                      'sex': None,
                      'faction': None,
                      'alg': None,
                      'pocc': None,
                      'socc': None,
                      'exp_total': 42,
                      'exp_remaining': 42,
                      'natural_hp': 1,
                      'bonus_hp': 0,
                      'hp': 0,
                      'soak': 0,
                      'stuffing': 10,
                      'sanity': 5,
                      'str': 1,
                      'int': 1,
                      'dex': 1,
                      'con': 1,
                      'wis': 1,
                      'cha': 1,
                      'merits': {},
                      'flaws': {}
                      }
    character_stats = ['str', 'int', 'dex', 'con', 'wis', 'cha']

    skills_dict = {"academics": 0,
                   "computer": 0,
                   "concentration": 0,
                   "crafting": 0,
                   "investigation": 0,
                   "medicine": 0,
                   "occult": 0,
                   "politics": 0,
                   "science": 0,
                   "athletics": 0,
                   "brawl": 0,
                   "demolitions": 0,
                   "drive": 0,
                   "firearms": 0,
                   "larceny": 0,
                   "ranged weaponry": 0,
                   "ride": 0,
                   "stealth": 0,
                   "survival": 0,
                   "weaponry": 0,
                   "animal kinship": 0,
                   "bluff": 0,
                   "empathy": 0,
                   "expression": 0,
                   "intimidate": 0,
                   "persuasion": 0,
                   "social contacts": 0,
                   "streetwise": 0,
                   "subterfuge": 0
                   }

    checks_dict = {'aim': 0,
                   'attack_power': 0,
                   'concentration': 0,
                   'dodge': 0,
                   'initiative': 0,
                   'knowledge': 0,
                   'mental': 0,
                   'money': 0,
                   'social': 0,
                   'perception': 0,
                   'physical': 0,
                   'poison_resistance': 0,
                   'probability': 0,
                   'rage': 0,
                   'ranged_attack_power': 0,
                   'resistance': 0,
                   'search': 0,
                   'vitality': 0}

    combat_dict = {'attacks_per_round': 0,
                   'aim': 0,
                   'armor_class': 0,
                   'initiative': 0,
                   'attack_power': 0,
                   'ranged_attack_power': 0,
                   'block': 0,
                   'dodge': 0,
                   'parry': 0,
                   'move': 10}

    template = Templates()


class Species(SpeciesDict):
    template = Templates()
    printer_services = PrinterServices()
    species_dict = SpeciesDict.SPECIES_DICT
    character_dict = PlayerCharacter.character_dict
    
    def get_species(self, species, species_l_choice):
        """
        allows player to switch lists
        allows player to return to the character sheet
        gets species and adds appropriate bonus to stats
        :return: 
        """
        species_end = False
        while species_end is False:
            species_l = self.species_dict[species]
            if species_l_choice == 'SWITCH':
                self.switch_species(species)
            elif species_l_choice == 'CANCEL':
                return_menu = True
                return return_menu
            else:
                species_a = species_l[species_l_choice]
                species_size, species_bonus, species_bonus_type = species_a
                self.character_dict['species_size'] = species_size
                self.character_dict[species_bonus_type] += species_bonus
                self.character_dict['species'] = species_l_choice
                species_end = True
        return_menu = True
        return return_menu

    def switch_species(self, species):
        """
        switches species list
        :param species: 
        :return: 
        """
        if species == 'LAND':
            species = 'AIR'
        else:
            species = 'LAND'
        return species


class HealthPoints(PlayerCharacter):
    template = Templates()
    character_dict = PlayerCharacter.character_dict

    def update_hp(self):
        """
        updates hp with bonuses
        :return: 
        """
        natural_hp = PlayerCharacter.character_dict['natural_hp']
        bonus_hp = self.hp_bonuses()
        current_hp = natural_hp + bonus_hp

        self.character_dict['hp'] = current_hp

    def hp_bonuses(self):
        """
        calculates bonus to hp based on skills and CON stat
        :return: 
        """
        con_bonus = PlayerCharacter.character_dict['con']
        try:
            athletics_bonus = PlayerCharacter.skills_dict['athletics']
        except Exception:
            athletics_bonus = 0
        try:
            survival_bonus = PlayerCharacter.skills_dict['survival']
        except Exception:
            survival_bonus = 0
        bonus = con_bonus + athletics_bonus + survival_bonus
        PlayerCharacter.character_dict['bonus_hp'] = bonus
        return bonus

    def get_hp_player_choice(self):
        exp = ExperienceCheck()
        bonus_hp = self.hp_bonuses()
        natural_hp = PlayerCharacter.character_dict['natural_hp']
        current_hp = PlayerCharacter.character_dict['hp']

        print(self.template.HEALTH_POINTS)
        print("\nNatural HP: {} \nCurrent Bonus: {} \nTotal HP: {}".format(natural_hp, bonus_hp, current_hp))
        print(exp.exp_current())
        hp_adjust = input("\nᗘᗘᗘ Health Points: ")

        return hp_adjust

    def get_hp(self, hp_adjust):
        """
        generates the hp based off natural hp so bonuses do not cost the player more than they should
        subtracts/adds exp appropriately
        :return: 
        """
        hp_cost = 4
        bonus_hp = self.hp_bonuses()
        natural_hp = PlayerCharacter.character_dict['natural_hp']
        exp = ExperienceCheck()

        hp_adjusted = int(hp_adjust) - natural_hp
        exp_cost = hp_adjusted * hp_cost
        exp_check = exp.exp_remaining_check(exp_cost=exp_cost)

        if exp_check is True:
            if int(hp_adjust) > natural_hp:
                PlayerCharacter.character_dict['exp_remaining'] -= exp_cost
                PlayerCharacter.character_dict['natural_hp'] = int(hp_adjust)
                hp_total = int(hp_adjust) + bonus_hp
                if hp_total > 10:
                    self.get_soak_check(hp_total=hp_total)
                else:
                    PlayerCharacter.character_dict['hp'] = hp_total
            else:
                hp_adjusted = natural_hp - int(hp_adjust)
                exp_cost = hp_adjusted * hp_cost
                PlayerCharacter.character_dict['exp_remaining'] += exp_cost
                PlayerCharacter.character_dict['natural_hp'] = int(hp_adjust)
                hp_total = int(hp_adjust) + bonus_hp
                PlayerCharacter.character_dict['hp'] = hp_total

    def get_soak_check(self, hp_total):
        soak_check = (hp_total - 10)
        if soak_check >= 1:
            soak = soak_check / 3
            PlayerCharacter.character_dict['hp'] = 10
            PlayerCharacter.character_dict['soak'] = int(soak)


class Stuffing(object):
    template = Templates()
    character_dict = PlayerCharacter.character_dict

    def get_stuffing(self):
        pass


class Stats(object):
    template = Templates()
    character_dict = PlayerCharacter.character_dict

    def get_stats(self, player_choice):
        """
        
        :param player_choice: 
        :return: 
        """
        stat = player_choice
        print(self.template.STATS)
        stat_adjust = int(input(self.template.SKILLS_STATS_ADJUST))
        self.get_stat_cost(stat=stat, stat_adjust=stat_adjust)

    def get_stat_cost(self, stat, stat_adjust):
        exp = ExperienceCheck()
        stat_cost = [0, 2, 3, 4, 5]
        stat_cost_add = 0
        current_stat = self.character_dict[stat]
        stat_climb = stat_adjust - current_stat
        if stat_climb > 0 and current_stat <= 5:
            while stat_climb > 0:
                stat_cost_add = stat_cost[current_stat] + stat_cost_add
                stat_climb -= 1
                current_stat = current_stat + 1
            exp_check = exp.exp_remaining_check(exp_cost=stat_cost_add)
            if exp_check is True:
                self.character_dict['exp_remaining'] -= stat_cost_add
                self.character_dict[stat] = stat_adjust
        elif stat_climb < 0 and current_stat >= 1:
            while stat_climb < 0:
                stat_cost_add = stat_cost[current_stat - 1] + stat_cost_add
                stat_climb += 1
                current_stat = current_stat - 1
            exp_check = exp.exp_remaining_check(exp_cost=stat_cost_add)
            if exp_check is True:
                self.character_dict['exp_remaining'] += stat_cost_add
                self.character_dict[stat] = stat_adjust


class CharacterSkillsGenerator(object):
    template = Templates()
    printer_services = PrinterServices()
    character_dict = PlayerCharacter.character_dict
    skills_dict = PlayerCharacter.skills_dict

    def print_skills(self):
        """
        prints list of skills
        :return: 
        """
        print("\n", "=" * 5, ">>> SKILLS <<<", "=" * 5)
        skill_list = self.printer_services.print_char_skills(skills_dict=self.skills_dict)
        print(skill_list)

    def get_skills(self):
        """
        gets skill from player input and creates skill_mini_dict
        :return: 
        """
        exp = ExperienceCheck()
        skills_end = False
        print(self.template.SKILLS)
        while skills_end is False:
            self.print_skills()
            print(exp.exp_current())
            skill_select = input(self.template.SKILLS_SELECT).lower()
            skills_dict = self.skills_dict
            if skill_select == 'cancel':
                skills_end = True
                return skills_end
            else:
                if skill_select in skills_dict.keys():
                    current_skill = skills_dict[skill_select]
                    skill_mini_dict = self.get_skill_adjust(current_skill, skill_select)
                    if skill_mini_dict != 'cancel':
                        self.get_skill_cost(skill_mini_dict=skill_mini_dict)
                    else:
                        skills_end = True
                        return skills_end
        return_menu = True
        return return_menu

    def get_skill_adjust(self, current_skill, skill_select):
        while True:
            try:
                skill_adjust = int(input(self.template.SKILLS_STATS_ADJUST))
                if 0 < skill_adjust <= 5:
                    skill_mini_dict = {'skill': skill_select, 'points': current_skill, 'adjust': skill_adjust}
                    return skill_mini_dict
            except ValueError:
                print(self.template.VALID_ENTRY)

    def get_skill_cost(self, skill_mini_dict):
        """
        takes skill_mini_dict generated by get_skills and calculates skill cost, skill adjust, and then writes the appropriate 
        value to the sppropriate skill in skill_dict
        :param skill_mini_dict: 
        :return: 
        """
        exp = ExperienceCheck()
        skill_select = skill_mini_dict['skill']
        current_skill = skill_mini_dict['points']
        skill_adjust = skill_mini_dict['adjust']
        skill_cost = [1, 2, 3, 4, 5]
        skill_cost_add = 0
        skill_climb = skill_adjust - current_skill
        if skill_climb > 0 and current_skill <= 5:
            while skill_climb > 0:
                skill_cost_add = skill_cost[current_skill] + skill_cost_add
                skill_climb -= 1
                current_skill = current_skill + 1
            exp_check = exp.exp_remaining_check(exp_cost=skill_cost_add)
            if exp_check is True:
                self.character_dict['exp_remaining'] -= skill_cost_add
                self.skills_dict[skill_select] = skill_adjust
        elif skill_climb < 0 and current_skill >= 1:
            while skill_climb < 0:
                skill_cost_add = skill_cost[current_skill - 1] + skill_cost_add
                skill_climb += 1
                current_skill = current_skill - 1
            exp_check = exp.exp_remaining_check(exp_cost=skill_cost_add)
            if exp_check is True:
                self.character_dict['exp_remaining'] += skill_cost_add
                self.skills_dict[skill_select] = skill_adjust


class MeritsFlawsGenerator(MeritsFlawsDicts):
    template = Templates()
    character_dict = PlayerCharacter.character_dict
    skills_dict = PlayerCharacter.skills_dict
    checks_dict = PlayerCharacter.checks_dict
    merits_flaws_dicts = MeritsFlawsDicts()

    def print_merits_flaws(self, select, mf_dict, mf):
        """
        prints list of merits/flaws depending on select
        :param select: param that determines sub list printed
        :param mf_dict: param that determines m or f dict
        :param mf: simple variable to determine - or + depending on m or f
        :return: 
        """
        print('\nᗘᗘ {} :\n'.format(select))
        for keys in mf_dict[select]:
            values = mf_dict[select][keys]
            cost, check, modifier = values
            if mf == 'merits':
                pm = '-'
            else:
                pm = '+'
            print('ᗘᗘᗘ {}:   [[COST ᗘᗘ {}{}] [ATTRIBUTE ᗘᗘ {}] [MODIFIER ᗘᗘ +{}]'.format(keys, pm, cost, check, modifier))
            
    def get_current_merits_flaws(self, mf):
        """
        prints current merit/flaws
        :param mf: simple variable to determine - or + depending on m or f
        :return: 
        """
        current_mf = self.character_dict[mf]
        print('Current {}: '.format(mf.upper()))
        for merit_flaw in current_mf:
            print('{}'.format(merit_flaw))

    def get_bonus_attribute(self, mf, values):
        """
        adds bonuses to appropriate attributes/skills depending on merit/flaw
        :param mf: simple variable to determine - or + depending on m or f
        :param values: attribute and adjust passed in from get
        :return: 
        """
        mf_a = mf
        bonus_attribute = values[1]
        bonus_attribute_adjust = values[2]
        if mf_a == 'merits':
            if bonus_attribute in self.skills_dict:
                self.skills_dict[bonus_attribute] += bonus_attribute_adjust
            elif bonus_attribute in self.character_dict:
                self.character_dict[bonus_attribute] += bonus_attribute_adjust
            else:
                self.checks_dict[bonus_attribute] += bonus_attribute_adjust
        else:
            if bonus_attribute in self.skills_dict:
                self.skills_dict[bonus_attribute] -= bonus_attribute_adjust
            elif bonus_attribute in self.character_dict:
                self.character_dict[bonus_attribute] -= bonus_attribute_adjust
            else:
                self.checks_dict[bonus_attribute] -= bonus_attribute_adjust

    def get_merits(self):
        """
        gets player input and drives merits
        :return: 
        """
        exp = ExperienceCheck()
        merits_end = False
        merits_limit = 0
        mf = 'merits'
        while merits_end is False:
            if merits_limit < 3:
                self.get_current_merits_flaws(mf=mf)
                merits_list_select = input(self.template.GET_MERITS).upper()
                if merits_list_select == 'CANCEL':
                    merits_end = True
                elif merits_list_select == 'MENTAL' or merits_list_select == 'PHYSICAL' or merits_list_select == 'SOCIAL':
                    merits_dict = self.merits_flaws_dicts.MERITS
                    self.print_merits_flaws(select=merits_list_select, mf_dict=merits_dict, mf=mf)
                    print(exp.exp_current())
                    merits_select = input(self.template.SELECT_MF).lower()
                    if merits_select == 'cancel':
                        merits_end = True
                    elif merits_select == 'change list':
                        continue
                    elif merits_select in merits_dict[merits_list_select]:
                        merit_values = merits_dict[merits_list_select][merits_select]
                        exp_cost = merit_values[0]
                        exp_check = exp.exp_remaining_check(exp_cost=exp_cost)
                        if exp_check is True:
                            merits_mini_dict = {merits_select: merits_dict[merits_list_select][merits_select]}
                            merits = self.character_dict['merits']
                            merits.update(merits_mini_dict)
                            self.get_bonus_attribute(mf=mf, values=merit_values)
                            self.character_dict['exp_remaining'] -= exp_cost
                            merits_limit += 1
                    else:
                        print(self.template.VALID_ENTRY)
                else:
                    print(self.template.VALID_ENTRY)
            else:
                merits_end = True

    def get_flaws(self):
        """
        gets player input and drives flaws
        :return: 
        """
        exp = ExperienceCheck()
        flaws_end = False
        flaws_limit = 0
        mf = 'flaws'
        while flaws_end is False:
            if flaws_limit < 3:
                self.get_current_merits_flaws(mf=mf)
                flaws_list_select = input(self.template.GET_FLAWS).upper()
                if flaws_list_select == 'CANCEL':
                    flaws_end = True
                elif flaws_list_select == 'MENTAL' or flaws_list_select == 'PHYSICAL' or flaws_list_select == 'STATS':
                    flaws_dict = self.merits_flaws_dicts.FLAWS
                    self.print_merits_flaws(select=flaws_list_select, mf_dict=flaws_dict, mf=mf)
                    print(exp.exp_current())
                    flaws_select = input(self.template.GET_FLAWS).lower()
                    if flaws_select == 'cancel':
                        flaws_end = True
                    elif flaws_select == 'change list':
                        continue
                    elif flaws_select in flaws_dict[flaws_list_select]:
                        flaws_values = flaws_dict[flaws_list_select][flaws_select]
                        exp_cost = flaws_values[0]
                        flaws_mini_dict = {flaws_select: flaws_dict[flaws_list_select][flaws_select]}
                        flaws = self.character_dict['flaws']
                        flaws.update(flaws_mini_dict)
                        self.get_bonus_attribute(mf=mf, values=flaws_values)
                        self.character_dict['exp_remaining'] += exp_cost
                        flaws_limit += 1
                    else:
                        print(self.template.VALID_ENTRY)
                else:
                    print(self.template.VALID_ENTRY)
            else:
                flaws_end = True

    def remove_merits_flaws(self):
        pass


class BonusChecks(object):
    character_dict = PlayerCharacter.character_dict
    skills_dict = PlayerCharacter.skills_dict
    checks_dict = PlayerCharacter.checks_dict

    def get_bonus_attribute(self, adjust, attribute):
        """
        service to calculate attribute/skill adjust
        :param adjust: 
        :param attribute: 
        :return: 
        """
        bonus_attribute = attribute
        bonus_attribute_adjust = adjust
        if bonus_attribute in self.skills_dict:
            self.skills_dict[bonus_attribute] = bonus_attribute_adjust
        elif bonus_attribute in self.character_dict:
            self.character_dict[bonus_attribute] = bonus_attribute_adjust
        else:
            self.checks_dict[bonus_attribute] = bonus_attribute_adjust


class POCC(OCCs, BonusChecks):
    template = Templates()
    character_dict = PlayerCharacter.character_dict
    skills_dict = PlayerCharacter.skills_dict
    checks_dict = PlayerCharacter.checks_dict

    def print_pocc(self):
        print(self.template.POCC)

    def get_pocc(self, select_pocc):
        """
        gets player input and adjusts attributes/skills accorndingly
        :return: 
        """
        pocc_end = False
        while pocc_end is False:
            pocc_list = OCCs.PRIMARY_OCC.keys()
            if select_pocc != 'cancel':
                if select_pocc in pocc_list:
                    pocc = OCCs.PRIMARY_OCC[select_pocc]
                    self.character_dict['pocc'] = {select_pocc: pocc}
                    bonus_adjust_sk1 = pocc[0]
                    bonus_attribute_sk1 = pocc[1]
                    BonusChecks.get_bonus_attribute(self, adjust=bonus_adjust_sk1, attribute=bonus_attribute_sk1)
                    bonus_adjust_sk2 = pocc[2]
                    bonus_attribute_sk2 = pocc[3]
                    BonusChecks.get_bonus_attribute(self, adjust=bonus_adjust_sk2, attribute=bonus_attribute_sk2)

                    pocc_end = True
            else:
                pocc_end = True


class SOCC(OCCs, BonusChecks):
    template = Templates()
    character_dict = PlayerCharacter.character_dict
    skills_dict = PlayerCharacter.skills_dict

    def print_socc(self, socc_req):
        """
        prints socc determined by the selection of pocc
        :param socc_req: 
        :return: 
        """
        socc = OCCs.SECONDARY_OCC[socc_req]
        for key, value in socc.items():
            print(key, value)

    def get_socc(self):
        """
        gets socc based on pocc and adjusts attribute/skill accordingly
        :return: 
        """
        pocc = self.character_dict['pocc']
        socc_req = "".join(pocc.keys()).upper()
        socc_end = False
        while socc_end is False:
            self.print_socc(socc_req=socc_req)
            select_socc = input(self.template.SELECT_SOCC).lower()
            socc_list = OCCs.SECONDARY_OCC[socc_req].keys()
            if select_socc != 'cancel':
                if select_socc in socc_list:
                    self.add_socc(select_socc, socc_req)
                    socc_end = True
            else:
                socc_end = True

    def add_socc(self, select_socc, socc_req):
        socc = OCCs.SECONDARY_OCC[socc_req][select_socc]
        self.character_dict['socc'] = {select_socc: socc}
        bonus_attributes = socc[1]
        bonus_adjust = socc[0]
        BonusChecks.get_bonus_attribute(self, adjust=bonus_adjust, attribute=bonus_attributes)
        # self.skills_dict[bonus_attributes] += bonus_adjust

    def check_required_pocc(self):
        """
        checks to make sure the player has chose a pocc before allowing them to chose an socc
        :return: 
        """
        if self.character_dict['pocc'] is None:
            input(self.template.SELECT_SOCC_ERROR)
        else:
            self.get_socc()
    

class ExperienceCheck(object):
    template = Templates()
    character_dict = PlayerCharacter.character_dict
    
    def exp_remaining_check(self, exp_cost):
        """
        checks to ensure the player has enough exp to spend on their choice
        :param exp_cost: 
        :return: 
        """
        is_valid = True
        exp_cost_total = self.character_dict['exp_remaining'] - exp_cost
        if exp_cost_total <= 0:
            input(self.template.NO_EXP_MSG)
            is_valid = False
            return is_valid
        else:
            return is_valid

    def exp_current(self):
        """
        displays current exp
        :return: 
        """
        current_exp = "\nᗘᗘᗘ Experience Points Remaining : {}\n".format(self.character_dict['exp_remaining'])
        return current_exp


class PCCombat(object):

    def attack(self):
        # roll = random.randint(1, self.attack_limit)
        # # if self.weapon == 'sword':
        # #     roll += 1
        # return roll
        pass

    # def __str__(self):
    #     return '{}, HP: {}, XP: {}'.format(self.name, self.hp, self.exp)
    #
    # def rest(self):
    #     if self.hp < self.base_hp:
    #         self.hp += 1
    #
    # def leveled_up(self):
    #     self.exp += self.monster.exp
    #     if self.exp == '5':
    #         self.level += 1
    #     elif self.exp == '10':
    #         if self.level != 2:
    #             self.level += 2
    #         self.level += 1
    #     elif self.exp == '15':
    #         self.level += 1
    #     print('Level {}! You\'ve leveled up!! Power courses through you'.format(self.level))


class CharacterStoreSession(object):
    cc = PlayerCharacter()
    db = db_session()

    def store_character_session(self):
        db_char = Character()
        pocc = self.cc.character_dict['pocc']
        socc = self.cc.character_dict['socc']

        db_char.name = self.cc.character_dict['name']
        db_char.species = self.cc.character_dict['species']
        db_char.species_size = self.cc.character_dict['species_size']
        db_char.sex = self.cc.character_dict['sex']
        db_char.faction = self.cc.character_dict['faction']
        db_char.alg = self.cc.character_dict['alg']
        db_char.pocc = str(pocc.keys())
        db_char.socc = str(socc.keys())
        db_char.exp_total = self.cc.character_dict['exp_total']
        db_char.exp_remaining = self.cc.character_dict['exp_remaining']
        db_char.natural_hp = self.cc.character_dict['natural_hp']
        db_char.hp = self.cc.character_dict['hp']
        db_char.soak = self.cc.character_dict['soak']
        db_char.stuffing = self.cc.character_dict['stuffing']
        db_char.sanity = self.cc.character_dict['sanity']
        db_char.str = self.cc.character_dict['str']
        db_char.int = self.cc.character_dict['int']
        db_char.dex = self.cc.character_dict['dex']
        db_char.con = self.cc.character_dict['con']
        db_char.wis = self.cc.character_dict['wis']
        db_char.cha = self.cc.character_dict['cha']
        db_char.code = 1
        self.db.add(db_char)
        self.db.commit()
        # self.store_character_session()

    def store_character_skills_session(self):
        db_sk = CharacterSkills()
        db_sk.academics = self.cc.skills_dict['academics']
        db_sk.computer = self.cc.skills_dict['computer']
        db_sk.concentration = self.cc.skills_dict['concentration']
        db_sk.crafting = self.cc.skills_dict['crafting']
        db_sk.investigation = self.cc.skills_dict['investigation']
        db_sk.medicine = self.cc.skills_dict['medicine']
        db_sk.occult = self.cc.skills_dict['occult']
        db_sk.politics = self.cc.skills_dict['politics']
        db_sk.science = self.cc.skills_dict['science']
        db_sk.athletics = self.cc.skills_dict['athletics']
        db_sk.brawl = self.cc.skills_dict['brawl']
        db_sk.demolitions = self.cc.skills_dict['demolitions']
        db_sk.drive = self.cc.skills_dict['drive']
        db_sk.firearms = self.cc.skills_dict['firearms']
        db_sk.larceny = self.cc.skills_dict['larceny']
        db_sk.ranged_weaponry = self.cc.skills_dict['ranged weaponry']
        db_sk.ride = self.cc.skills_dict['ride']
        db_sk.stealth = self.cc.skills_dict['stealth']
        db_sk.survival = self.cc.skills_dict['survival']
        db_sk.weaponry = self.cc.skills_dict['weaponry']
        db_sk.animal_kinship = self.cc.skills_dict['animal kinship']
        db_sk.bluff = self.cc.skills_dict['bluff']
        db_sk.empathy = self.cc.skills_dict['empathy']
        db_sk.expression = self.cc.skills_dict['expression']
        db_sk.intimidate = self.cc.skills_dict['intimidate']
        db_sk.persuasion = self.cc.skills_dict['persuasion']
        db_sk.social_contacts = self.cc.skills_dict['social contacts']
        db_sk.streetwise = self.cc.skills_dict['streetwise']
        db_sk.subterfuge = self.cc.skills_dict['subterfuge']
        self.db.add(db_sk)
        self.db.commit()

    def store_merits_flaws(self):
        db_cmf = CharacterMeritsFlaws()
        pc = PlayerCharacter()
        merit_counter = 1
        flaw_counter = 1
        db_cmf.character_id = Character.id
        for merits in pc.character_dict['merits']:
            merit_instance = self.db.query(MeritsFlaws).filter_by(merits_flaws=merits).first()
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
        for flaws in pc.character_dict['flaws']:
            flaw_instance = self.db.query(MeritsFlaws).filter_by(merits_flaws=flaws).first()
            if flaw_counter == 1:
                db_cmf.flaws_01 = flaw_instance.id
            elif flaw_counter == 2:
                db_cmf.flaws_02 = flaw_instance.id
            elif flaw_counter == 3:
                db_cmf.flaws_03 = flaw_instance.id
            elif flaw_counter == 4:
                db_cmf.flaws_04 = flaw_instance.id
            elif flaw_counter == 5:
                db_cmf.flaws_05 = flaw_instance.id
            flaw_counter += 1

        self.db.add(db_cmf)
        self.db.commit()
