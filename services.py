from character_pc import PlayerCharacter
from models import Character, Skill
from database_service import db_session

class CharacterStoreSession(object):
    cc = PlayerCharacter()

    def store_character_session(self):
        db = db_session()
        db_char = Character()
        db_char.name = self.cc.character_dict['name']
        db_char.species = self.cc.character_dict['species']
        db_char.species_size = self.cc.character_dict['species_size']
        db_char.sex = self.cc.character_dict['sex']
        db_char.faction = self.cc.character_dict['faction']
        db_char.alg = self.cc.character_dict['alg']
        db_char.pocc = self.cc.character_dict['pocc']
        db_char.socc = self.cc.character_dict['socc']
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
        # db_char.merits = self.cc.character_dict['merits']
        # db_char.flaws = self.cc.character_dict['flaws']
        db_char.code = 1
        db.add(db_char)
        db.commit()

    def store_character_skills_session(self):
        db = db_session()
        db_sk = Skill()
        db_sk.academics = self.cc.character_dict['skills']['mental']['academics']
        db_sk.computer = self.cc.character_dict['skills']['mental']['computer']
        db_sk.concentration = self.cc.character_dict['skills']['mental']['concentration']
        db_sk.crafting = self.cc.character_dict['skills']['mental']['crafting']
        db_sk.investigation = self.cc.character_dict['skills']['mental']['investigation']
        db_sk.medicine = self.cc.character_dict['skills']['mental']['medicine']
        db_sk.occult = self.cc.character_dict['skills']['mental']['occult']
        db_sk.politics = self.cc.character_dict['skills']['mental']['politics']
        db_sk.science = self.cc.character_dict['skills']['mental']['science']
        db_sk.athletics = self.cc.character_dict['skills']['physical']['athletics']
        db_sk.brawl = self.cc.character_dict['skills']['physical']['brawl']
        db_sk.demolitions = self.cc.character_dict['skills']['physical']['demolitions']
        db_sk.drive = self.cc.character_dict['skills']['physical']['drive']
        db_sk.firearms = self.cc.character_dict['skills']['physical']['firearms']
        db_sk.larceny = self.cc.character_dict['skills']['physical']['larceny']
        db_sk.ranged_weaponry = self.cc.character_dict['skills']['physical']['ranged_weaponry']
        db_sk.ride = self.cc.character_dict['skills']['physical']['ride']
        db_sk.stealth = self.cc.character_dict['skills']['physical']['stealth']
        db_sk.survival = self.cc.character_dict['skills']['physical']['survival']
        db_sk.weaponry = self.cc.character_dict['skills']['physical']['weaponry']
        db_sk.animal_kinship = self.cc.character_dict['skills']['social']['animal_kinship']
        db_sk.bluff = self.cc.character_dict['skills']['social']['bluff']
        db_sk.empathy = self.cc.character_dict['skills']['social']['empathy']
        db_sk.expression = self.cc.character_dict['skills']['social']['expression']
        db_sk.intimidate = self.cc.character_dict['skills']['social']['intimidate']
        db_sk.persuasion = self.cc.character_dict['skills']['social']['persuasion']
        db_sk.social_contacts = self.cc.character_dict['skills']['social']['social_contacts']
        db_sk.streetwise = self.cc.character_dict['skills']['social']['streetwise']
        db_sk.subterfuge = self.cc.character_dict['skills']['social']['subterfuge']
        db.add(db_sk)

