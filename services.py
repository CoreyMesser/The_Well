from models import SpeciesDict, Character, CharacterMeritsFlaws, CharacterSkills, MeritsFlaws, PoccDb, SoccDb
from database_service import db_session


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

class PrintCompletedCharacterSheet(object):
    character_sheet = Character()
    db = db_session()

    def create_character_dict_from_db(self, char_id):
        db = db_session()
        for c in db.query(Character).filter(Character.id == char_id):
            character_dict = c.__dict__
        for s in db.query(CharacterSkills).filter(Character.id == char_id):
            skills_dict = s.__dict__
        for mf in db.query(CharacterMeritsFlaws).filter(CharacterMeritsFlaws.id == char_id):
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

    def print_character_sheet_from_db(self, char_id):
        character_dict, skills_dict, mf_dict = self.create_character_dict_from_db(char_id=char_id)
        char_stats = self.create_character_stats(character_dict=character_dict)
        char_skills = self.create_skills_stats(skills_dict=skills_dict)
        char_mf = self.create_mf_stats(mf_dict=mf_dict)
        print(char_stats, char_skills, char_mf)
        character = char_stats + char_skills + char_mf
        file_name = input('Please enter a file name: >>')
        f = open(file_name + '.txt', 'w')
        f.write(character)
        f.close()


class CharacterCreationServices(object):
    pass
