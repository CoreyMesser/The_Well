# from character_pc import PlayerCharacter
from models import Character, Skill, SpeciesDict, MeritsFlawsDicts, OCCs

from database_service import db_session

# class CharacterStoreSession(object):
#     cc = PlayerCharacter()
#
#     def store_character_session(self):
#         db = db_session()
#         db_char = Character()
#         db_char.name = self.cc.character_dict['name']
#         db_char.species = self.cc.character_dict['species']
#         db_char.species_size = self.cc.character_dict['species_size']
#         db_char.sex = self.cc.character_dict['sex']
#         db_char.faction = self.cc.character_dict['faction']
#         db_char.alg = self.cc.character_dict['alg']
#         db_char.pocc = self.cc.character_dict['pocc']
#         db_char.socc = self.cc.character_dict['socc']
#         db_char.exp_total = self.cc.character_dict['exp_total']
#         db_char.exp_remaining = self.cc.character_dict['exp_remaining']
#         db_char.natural_hp = self.cc.character_dict['natural_hp']
#         db_char.hp = self.cc.character_dict['hp']
#         db_char.soak = self.cc.character_dict['soak']
#         db_char.stuffing = self.cc.character_dict['stuffing']
#         db_char.sanity = self.cc.character_dict['sanity']
#         db_char.str = self.cc.character_dict['str']
#         db_char.int = self.cc.character_dict['int']
#         db_char.dex = self.cc.character_dict['dex']
#         db_char.con = self.cc.character_dict['con']
#         db_char.wis = self.cc.character_dict['wis']
#         db_char.cha = self.cc.character_dict['cha']
#         # db_char.merits = self.cc.character_dict['merits']
#         # db_char.flaws = self.cc.character_dict['flaws']
#         db_char.code = 1
#         db.add(db_char)
#         db.commit()
#
#     def store_character_skills_session(self):
#         db = db_session()
#         db_sk = Skill()
#         db_sk.academics = self.cc.character_dict['skills']['mental']['academics']
#         db_sk.computer = self.cc.character_dict['skills']['mental']['computer']
#         db_sk.concentration = self.cc.character_dict['skills']['mental']['concentration']
#         db_sk.crafting = self.cc.character_dict['skills']['mental']['crafting']
#         db_sk.investigation = self.cc.character_dict['skills']['mental']['investigation']
#         db_sk.medicine = self.cc.character_dict['skills']['mental']['medicine']
#         db_sk.occult = self.cc.character_dict['skills']['mental']['occult']
#         db_sk.politics = self.cc.character_dict['skills']['mental']['politics']
#         db_sk.science = self.cc.character_dict['skills']['mental']['science']
#         db_sk.athletics = self.cc.character_dict['skills']['physical']['athletics']
#         db_sk.brawl = self.cc.character_dict['skills']['physical']['brawl']
#         db_sk.demolitions = self.cc.character_dict['skills']['physical']['demolitions']
#         db_sk.drive = self.cc.character_dict['skills']['physical']['drive']
#         db_sk.firearms = self.cc.character_dict['skills']['physical']['firearms']
#         db_sk.larceny = self.cc.character_dict['skills']['physical']['larceny']
#         db_sk.ranged_weaponry = self.cc.character_dict['skills']['physical']['ranged_weaponry']
#         db_sk.ride = self.cc.character_dict['skills']['physical']['ride']
#         db_sk.stealth = self.cc.character_dict['skills']['physical']['stealth']
#         db_sk.survival = self.cc.character_dict['skills']['physical']['survival']
#         db_sk.weaponry = self.cc.character_dict['skills']['physical']['weaponry']
#         db_sk.animal_kinship = self.cc.character_dict['skills']['social']['animal_kinship']
#         db_sk.bluff = self.cc.character_dict['skills']['social']['bluff']
#         db_sk.empathy = self.cc.character_dict['skills']['social']['empathy']
#         db_sk.expression = self.cc.character_dict['skills']['social']['expression']
#         db_sk.intimidate = self.cc.character_dict['skills']['social']['intimidate']
#         db_sk.persuasion = self.cc.character_dict['skills']['social']['persuasion']
#         db_sk.social_contacts = self.cc.character_dict['skills']['social']['social_contacts']
#         db_sk.streetwise = self.cc.character_dict['skills']['social']['streetwise']
#         db_sk.subterfuge = self.cc.character_dict['skills']['social']['subterfuge']
#         db.add(db_sk)


class PrinterServices(SpeciesDict):

    def print_char_sheet(self, character_dict, skills_dict):
        """
        prints main character sheet with updated parameters passed in by player
        :param character_dict: 
        :param skills_dict: 
        :return: 
        """
        main_sheet = "[NAME]    NAME:  {name} \n" \
                     "[SPECIES] SPECIES:  {species} \n" \
                     "          SPECIES SZIE:  {species_size} \n" \
                     "[SEX]     SEX: {sex} \n" \
                     "[ FACTION] FACTION:  {faction} \n" \
                     "[ALG]     ALIGNMENT:  {alg} \n" \
                     "[POCC]    PRIMARY OCCUPATION: {pocc} \n" \
                     " [SOCC]    SECOND OCCUPATION:  {socc} \n" \
                     "\n" \
                     "  [HP]      HP: {natural_hp} + {bonus_hp} = {hp} \n" \
                     "[STUFF]   STUFFING: {stuffing} \n" \
                     "          SANITY: {sanity} \n" \
                     "          SOAK: {soak} \n" \
                     "\n" \
                     "  ᗘᗘᗘ STATS  ᗛᗛᗛ\n" \
                     "ᗘ[STR] : {str} \n" \
                     " ᗘ[INT] : {int} \n" \
                     "ᗘ[DEX] : {dex} \n" \
                     " ᗘ[CON] : {con} \n" \
                     " ᗘ[WIS] : {wis} \n" \
                     " ᗘ[CHA] : {cha} \n" \
                     "\n".format(**character_dict)


        skills_sheet = self.print_char_skills(skills_dict=skills_dict)
        merits_sheet = self.print_char_merits(character_dict=character_dict)
        flaws_sheet = self.print_char_flaws(character_dict=character_dict)
        exp_sheet = "\n \nᗘᗘᗘ XP POINTS TOTAL {exp_total} ᗛᗛᗛ\n" \
                    "ᗘᗘᗘ XP POINTS REMAINING {exp_remaining} ᗛᗛᗛ\n".format(**character_dict)

        sheet = main_sheet + skills_sheet + merits_sheet + flaws_sheet + exp_sheet
        return sheet

    def print_char_skills(self, skills_dict):
        """
        skills template for character sheet
        :param skills_dict: 
        :return: 
        """
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
                        'ᗘ {ranged weaponry} : [ranged weaponry]\n'.format(**skills_dict),
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
                        'ᗘ {social contacts} : [social contacts]\n'.format(**skills_dict),
                        'ᗘ {streetwise} : [streetwise]\n'.format(**skills_dict),
                        'ᗘ {subterfuge} : [subterfuge]\n'.format(**skills_dict)
                        ]
        return ''.join(skills_sheet)

    def print_char_merits(self, character_dict):
        """
        prints merits list for character sheet
        :param character_dict: 
        :return: 
        """
        if len(character_dict['merits']) > 0:
            merits_sheet = ["\n[MERITS]  MERITS:", ]
            merits = character_dict['merits']
            for l, j in merits.items():
                merits_sheet.append('\nᗘᗘ{}: {}\n'.format(l, j))
            return "".join(merits_sheet)
        else:
            merits_sheet = "   \n[MERITS]  MERITS: \n"
            return merits_sheet

    def print_char_flaws(self, character_dict):
        """
        prints flaws list for character sheet
        :param character_dict: 
        :return: 
        """
        if len(character_dict['flaws']) > 0:
            flaws_sheet = ["\n[FLAWS]  FLAWS:", ]
            flaws = character_dict['flaws']
            for l, j in flaws.items():
                flaws_sheet.append('\nᗘᗘ{}: {}\n'.format(l, j))
            return "".join(flaws_sheet)
        else:
            flaws_sheet = "   \n[FLAWS]  FLAWS: \n"
            return flaws_sheet

    def print_species_list(self, species):
        species_class = self.SPECIES_DICT[species]
        for k in species_class:
            print(k, species_class[k])