import random, os
from templates.templates import Templates

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
                      'skills': {'MENTAL': {}, 'PHYSICAL': {}, 'SOCIAL': {}},
                      'merits': {},
                      'flaws': {}
                      }
    # 'flaws_counter': 3
    character_stats = ['str', 'int', 'dex', 'con', 'wis', 'cha']

    template = Templates()
    species_dict = template.species_dict
    # return_to_menu = return_to_menu()

    def attack(self):
        roll = random.randint(1, self.attack_limit)
        # if self.weapon == 'sword':
        #     roll += 1
        return roll

    def get_species(self):
        species = input(self.template.SPECIES).upper()
        self.template.print_species_list(species)
        species_l = self.species_dict[species]
        species_l_choice = input('Please enter a species name, \n or [SWITCH] to switch Species Lists, '
                                 '\n or [SHEET] to return to you character sheet. \n \n >>>: ').upper()
        if species_l_choice == 'SWITCH':
            self.switch_species()
        elif species_l_choice == 'SHEET':
            return_menu = True
            return return_menu
        else:
            species_a = species_l[species_l_choice]
            species_size, species_bonus, species_bonus_type = species_a
            self.character_dict['species_size'] = species_size
            self.character_dict[species_bonus_type] += species_bonus
            self.character_dict['species'] = species_l_choice
            return_menu = True
            return return_menu

    def switch_species(self, species):
        if species == 'LAND':
            species = 'AIR'
        else:
            species = 'LAND'
        return species

    def update_hp(self):
        current_hp = self.character_dict['hp']
        con_bonus = self.character_dict['con']
        self.character_dict['hp'] = current_hp + con_bonus

    def hp_bonuses(self):
        con_bonus = self.character_dict['con']
        try:
            athletics_bonus = self.character_dict['skills']['PHYSICAL']['athletics']
        except KeyError:
            athletics_bonus = 0
        try:
            survival_bonus = self.character_dict['skills']['PHYSCIAL']['survival']
        except KeyError:
            survival_bonus = 0
        bonus = con_bonus + athletics_bonus + survival_bonus
        return bonus



    def get_hp(self):
        hp_cost = 4
        hp_cost_total = 4
        current_hp = self.character_dict['hp']

        print(self.template.HEALTH_POINTS)
        print("Current HP: {} \n".format(current_hp))

        hp_adjust = input("ᗘᗘᗘ Health Points: ")
        exp_cost = int(hp_adjust) * 4
        exp_check = self.exp_remaining_check(exp_cost=exp_cost)

        if exp_check is True:
            if int(hp_adjust) > current_hp:
                self.character_dict['exp_remaining'] -= exp_cost
                hp_cost_total = exp_cost + hp_cost_total
                hp = (hp_cost_total / hp_cost) + self.hp_bonuses()
                if hp_cost_total > 40:
                    soak_check = ((hp *4) - 40) / 3
                    soak = soak_check / 3
                    self.character_dict['hp'] = 10
                    self.character_dict['soak'] = int(soak)
                else:
                    self.character_dict['hp'] = hp
            else:
                self.character_dict['exp_remaining'] += exp_cost
                hp_cost_total = exp_cost + hp_cost_total
                hp = (hp_cost_total / hp_cost) + self.hp_bonuses()
                self.character_dict['hp'] = hp

    def get_stuffing(self):
        pass

    def get_stats(self, player_choice):
        stat = player_choice
        print(self.template.STATS)
        stat_adjust = int(input('Enter a number [1 - 5]: '))
        self.get_stat_cost(stat=stat, stat_adjust=stat_adjust)

    def get_stat_cost(self, stat, stat_adjust):
        stat_cost = [0, 2, 3, 4, 5]
        stat_cost_add = 0
        current_stat = self.character_dict[stat]
        stat_climb = stat_adjust - current_stat
        if stat_climb > 0 and current_stat <= 5:
            while stat_climb > 0:
                stat_cost_add = stat_cost[current_stat] + stat_cost_add
                stat_climb -= 1
                current_stat = current_stat + 1
            exp_check = self.exp_remaining_check(exp_cost=stat_cost_add)
            if exp_check is True:
                self.character_dict['exp_remaining'] -= stat_cost_add
                self.character_dict[stat] = stat_adjust
        elif stat_climb < 0 and current_stat >= 1:
            while stat_climb < 0:
                stat_cost_add = stat_cost[current_stat - 1] + stat_cost_add
                stat_climb += 1
                current_stat = current_stat - 1
            exp_check = self.exp_remaining_check(exp_cost=stat_cost_add)
            if exp_check is True:
                self.character_dict['exp_remaining'] += stat_cost_add
                self.character_dict[stat] = stat_adjust

    def print_skills(self):
        # skills = self.character_dict['skills']
        skills = self.template.skills_dict
        print("=" * 5, ">>> SKILLS <<<", "=" * 5)
        for l, j in skills.items():
            print('\n{} : \n'.format(l))
            for k,v in j.items():
                print('   {} : {}'.format(k, v).upper())

    def get_skills(self):
        self.print_skills()
        skill_select = input(self.template.SKILLS).lower()
        skills_dict = self.template.skills_dict
        skills = self.character_dict['skills']
        for l, j in skills_dict.items():
            if skill_select in j.keys():
                skill_dict_key = l
                if skill_select not in skills:
                    current_skill = j[skill_select]
                else:
                    current_skill = skills[skill_select]
                print('\n{}: {}'.format(skill_select, current_skill))
                skill_mini_dict = self.get_skill_adjust(current_skill, skill_dict_key, skill_select)
                if skill_mini_dict != 'cancel':
                    return_menu = self.get_skill_cost(skill_mini_dict=skill_mini_dict)
                else:
                    return_menu = True
                    return return_menu


    def get_skill_adjust(self, current_skill, skill_dict_key, skill_select):
        while True:
            try:
                skill_adjust = int(input('\nEnter a number [1 - 5]: '))
                if 0 < skill_adjust <= 5:
                    skill_mini_dict = {'key': skill_dict_key, 'skill': skill_select, 'points': current_skill, 'adjust': skill_adjust}
                    return skill_mini_dict
            except ValueError:
                print('Please enter a valid number.')

    def get_skill_cost(self, skill_mini_dict):
        skill_key = skill_mini_dict['key']
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
            exp_check = self.exp_remaining_check(exp_cost=skill_cost_add)
            if exp_check is True:
                self.character_dict['exp_remaining'] -= skill_cost_add
                skills = self.character_dict['skills']
                skill_sub_dict = skills[skill_key]
                skill_sub_dict[skill_select] = skill_adjust
                return_menu = True
                return return_menu
        elif skill_climb < 0 and current_skill >= 1:
            while skill_climb < 0:
                skill_cost_add = skill_cost[current_skill - 1] + skill_cost_add
                skill_climb += 1
                current_skill = current_skill - 1
            exp_check = self.exp_remaining_check(exp_cost=skill_cost_add)
            if exp_check is True:
                self.character_dict['exp_remaining'] += skill_cost_add
                skills = self.character_dict['skills']
                skill_sub_dict = skills[skill_key]
                skill_sub_dict[skill_select] = skill_adjust
                return_menu = True
                return return_menu

    def print_merits_flaws(self):
        pass

    def get_merits(self):
        pass

    def get_flaws(self):
        pass

    def exp_remaining_check(self, exp_cost):
        is_valid = True
        exp_cost_total = self.character_dict['exp_remaining'] - exp_cost
        if exp_cost_total <= 0:
            input("You do not have enough Exp remaining.  Press [RETURN] to continue.")
            is_valid = False
            return is_valid
        else:
            return is_valid

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
