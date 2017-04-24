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
                      'skills': {},
                      'merits': {},
                      'flaws': {}
                      }
    # 'flaws_counter': 3
    character_stats = ['str', 'int', 'dex', 'con', 'wis', 'cha']

    template = Templates()
    species_dict = template.species_dict

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
            pass
        else:
            species_a = species_l[species_l_choice]
            species_size, species_bonus, species_bonus_type = species_a
            self.character_dict['species_size'] = species_size
            self.character_dict[species_bonus_type] += species_bonus
            self.character_dict['species'] = species_l_choice

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

    def get_hp(self):
        hp_cost = 4
        hp_cost_total = 4
        current_hp = self.character_dict['hp']
        con_bonus = self.character_dict['con']

        print(self.template.HEALTH_POINTS)
        print("Current HP: {} \n".format(current_hp))

        hp_adjust = input("ᗘᗘᗘ Health Points: ")
        exp_cost = int(hp_adjust) * 4
        exp_check = self.exp_remaining_check(exp_cost=exp_cost)

        if exp_check is True:
            if int(hp_adjust) > current_hp:
                self.character_dict['exp_remaining'] -= exp_cost
                hp_cost_total = exp_cost + hp_cost_total

                hp = (hp_cost_total / hp_cost) + con_bonus
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
                hp = (hp_cost_total / hp_cost) + con_bonus
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
        skills = self.character_dict['skills']
        skills.update(self.template.skills_dict)
        print("=" * 5, ">>> SKILLS <<<", "=" * 5)
        for k,v in skills:
            print('{} : {}'.format(k, v))

    def get_skills(self):
        pass

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

    def __str__(self):
        return '{}, HP: {}, XP: {}'.format(self.name, self.hp, self.exp)

    def rest(self):
        if self.hp < self.base_hp:
            self.hp += 1

    def leveled_up(self):
        self.exp += self.monster.exp
        if self.exp == '5':
            self.level += 1
        elif self.exp == '10':
            if self.level != 2:
                self.level += 2
            self.level += 1
        elif self.exp == '15':
            self.level += 1
        print('Level {}! You\'ve leveled up!! Power courses through you'.format(self.level))
