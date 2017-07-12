# -*- coding: utf-8 -*-
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Numeric, Text, text, Time
from sqlalchemy import CheckConstraint
from sqlalchemy.orm import relationship
from database_service import Base, db_session
from constants import MapConstants, ObjectConstants, WeaponConstant

from flask_login import LoginManager
from flask_bcrypt import generate_password_hash, check_password_hash

metadata = Base.metadata


class CharacterModels(object):
    PLAYER_MOVE_DICT = {'character_id': 9,
                        'location': (1, 5),
                        'path': [(0, 0)],
                        'direction': 'NORTH',
                        'current_level': MapConstants.LEVEL_00}

class Navigation(object):
    pass


class Inventory(object):
    def bag(self):
        # dict
        pass

    def drop(self, item, slot):
        pass


class PCGear(object):
    def equip(self, item, slot):
        pass

    def unequip(self, item, slot):
        pass


class PCSlots(object):
    def __init__(self):
        self.left_hand_slot = ''
        self.right_hand_slot = ''
        self.shoulder_slot = ''
        self.chest_slot = ''
        self.belt_slot = ''
        self.leggings_slot = ''
        self.boots_slot = ''
        self.ring_1_slot = ''
        self.ring_2_slot = ''
        self.neck_slot = ''
        self.head_slot = ''


class Character(Base):
    __tablename__ = 'character'
    __table_args__ = (
        CheckConstraint("date_part('timezone'::text, created_at) = '0'::double precision"),
        CheckConstraint("date_part('timezone'::text, updated_at) = '0'::double precision")
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('character_id_seq'::regclass)"))
    user_id = Column(Integer, nullable=False)
    code = Column(Text, nullable=False)
    name = Column(Text, nullable=False)
    species = Column(Text, nullable=False)
    species_size = Column(Text, nullable=False)
    sex = Column(Text, nullable=False)
    faction = Column(Text)
    alg = Column(Text, nullable=False)
    pocc = Column(ForeignKey('pocc_db.id'), nullable=False)
    socc = Column(ForeignKey('socc_db.id'))
    exp_total = Column(Integer, nullable=False)
    exp_remaining = Column(Integer, nullable=False)
    natural_hp = Column(Integer, nullable=False)
    hp = Column(Integer, nullable=False)
    soak = Column(Integer, nullable=False)
    stuffing = Column(Integer, nullable=False)
    sanity = Column(Integer, nullable=False)
    str = Column(Integer, nullable=False)
    int = Column(Integer, nullable=False)
    dex = Column(Integer, nullable=False)
    con = Column(Integer, nullable=False)
    wis = Column(Integer, nullable=False)
    cha = Column(Integer, nullable=False)
    updated_at = Column(DateTime(True), nullable=False, server_default=text("now_utc()"))
    created_at = Column(DateTime(True), nullable=False, server_default=text("now_utc()"))

    pocc_db = relationship('PoccDb')
    socc_db = relationship('SoccDb')


class CharacterCode(Base):
    __tablename__ = 'character_code'
    __table_args__ = (
        CheckConstraint("date_part('timezone'::text, created_at) = '0'::double precision"),
        CheckConstraint("date_part('timezone'::text, updated_at) = '0'::double precision")
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('character_code_id_seq'::regclass)"))
    code = Column(Text, nullable=False)
    display_name = Column(Text)
    updated_at = Column(DateTime(True), nullable=False, server_default=text("now_utc()"))
    created_at = Column(DateTime(True), nullable=False, server_default=text("now_utc()"))


class CharacterMeritsFlaws(Base):
    __tablename__ = 'character_merits_flaws'
    __table_args__ = (
        CheckConstraint("date_part('timezone'::text, created_at) = '0'::double precision"),
        CheckConstraint("date_part('timezone'::text, updated_at) = '0'::double precision")
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('character_merits_flaws_id_seq'::regclass)"))
    code = Column(Text)
    character_id = Column(ForeignKey('character.id'), nullable=False)
    merits_01 = Column(ForeignKey('merits_flaws.id'))
    merits_02 = Column(ForeignKey('merits_flaws.id'))
    merits_03 = Column(ForeignKey('merits_flaws.id'))
    merits_04 = Column(ForeignKey('merits_flaws.id'))
    merits_05 = Column(ForeignKey('merits_flaws.id'))
    flaws_01 = Column(ForeignKey('merits_flaws.id'))
    flaws_02 = Column(ForeignKey('merits_flaws.id'))
    flaws_03 = Column(ForeignKey('merits_flaws.id'))
    flaws_04 = Column(ForeignKey('merits_flaws.id'))
    flaws_05 = Column(ForeignKey('merits_flaws.id'))
    updated_at = Column(DateTime(True), nullable=False, server_default=text("now_utc()"))
    created_at = Column(DateTime(True), nullable=False, server_default=text("now_utc()"))

    character = relationship('Character')
    merits_flaw = relationship('MeritsFlaws', primaryjoin='CharacterMeritsFlaws.flaws_01 == MeritsFlaws.id')
    merits_flaw1 = relationship('MeritsFlaws', primaryjoin='CharacterMeritsFlaws.flaws_02 == MeritsFlaws.id')
    merits_flaw2 = relationship('MeritsFlaws', primaryjoin='CharacterMeritsFlaws.flaws_03 == MeritsFlaws.id')
    merits_flaw3 = relationship('MeritsFlaws', primaryjoin='CharacterMeritsFlaws.flaws_04 == MeritsFlaws.id')
    merits_flaw4 = relationship('MeritsFlaws', primaryjoin='CharacterMeritsFlaws.flaws_05 == MeritsFlaws.id')
    merits_flaw5 = relationship('MeritsFlaws', primaryjoin='CharacterMeritsFlaws.merits_01 == MeritsFlaws.id')
    merits_flaw6 = relationship('MeritsFlaws', primaryjoin='CharacterMeritsFlaws.merits_02 == MeritsFlaws.id')
    merits_flaw7 = relationship('MeritsFlaws', primaryjoin='CharacterMeritsFlaws.merits_03 == MeritsFlaws.id')
    merits_flaw8 = relationship('MeritsFlaws', primaryjoin='CharacterMeritsFlaws.merits_04 == MeritsFlaws.id')
    merits_flaw9 = relationship('MeritsFlaws', primaryjoin='CharacterMeritsFlaws.merits_05 == MeritsFlaws.id')


class CharacterSkills(Base):
    __tablename__ = 'character_skills'
    __table_args__ = (
        CheckConstraint("date_part('timezone'::text, created_at) = '0'::double precision"),
        CheckConstraint("date_part('timezone'::text, updated_at) = '0'::double precision")
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('character_skills_id_seq'::regclass)"))
    character_id = Column(ForeignKey('character.id'), nullable=False)
    code = Column(Text)
    academics = Column(Integer)
    computer = Column(Integer)
    concentration = Column(Integer)
    crafting = Column(Integer)
    investigation = Column(Integer)
    medicine = Column(Integer)
    occult = Column(Integer)
    politics = Column(Integer)
    science = Column(Integer)
    athletics = Column(Integer)
    brawl = Column(Integer)
    demolitions = Column(Integer)
    drive = Column(Integer)
    firearms = Column(Integer)
    larceny = Column(Integer)
    ranged_weaponry = Column(Integer)
    ride = Column(Integer)
    stealth = Column(Integer)
    survival = Column(Integer)
    weaponry = Column(Integer)
    animal_kinship = Column(Integer)
    bluff = Column(Integer)
    empathy = Column(Integer)
    expression = Column(Integer)
    intimidate = Column(Integer)
    persuasion = Column(Integer)
    social_contacts = Column(Integer)
    streetwise = Column(Integer)
    subterfuge = Column(Integer)
    updated_at = Column(DateTime(True), nullable=False, server_default=text("now_utc()"))
    created_at = Column(DateTime(True), nullable=False, server_default=text("now_utc()"))

    character = relationship('Character')


class InventoryPc(Base):
    __tablename__ = 'inventory_pc'
    __table_args__ = (
        CheckConstraint("date_part('timezone'::text, created_at) = '0'::double precision"),
        CheckConstraint("date_part('timezone'::text, updated_at) = '0'::double precision")
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('inventory_pc_id_seq'::regclass)"))
    code = Column(Text, nullable=False)
    character_id = Column(Text, nullable=False)
    updated_at = Column(DateTime(True), nullable=False, server_default=text("now_utc()"))
    created_at = Column(DateTime(True), nullable=False, server_default=text("now_utc()"))


class LoginResult(Base):
    __tablename__ = 'login_result'
    __table_args__ = (
        CheckConstraint("date_part('timezone'::text, created_at) = '0'::double precision"),
        CheckConstraint("date_part('timezone'::text, updated_at) = '0'::double precision")
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('login_result_id_seq'::regclass)"))
    name = Column(Text, nullable=False)
    updated_at = Column(DateTime(True), nullable=False, server_default=text("now_utc()"))
    created_at = Column(DateTime(True), nullable=False, server_default=text("now_utc()"))


class LoginType(Base):
    __tablename__ = 'login_type'
    __table_args__ = (
        CheckConstraint("date_part('timezone'::text, created_at) = '0'::double precision"),
        CheckConstraint("date_part('timezone'::text, updated_at) = '0'::double precision")
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('login_type_id_seq'::regclass)"))
    name = Column(Text, nullable=False)
    updated_at = Column(DateTime(True), nullable=False, server_default=text("now_utc()"))
    created_at = Column(DateTime(True), nullable=False, server_default=text("now_utc()"))


class MeritsFlaws(Base):
    __tablename__ = 'merits_flaws'
    __table_args__ = (
        CheckConstraint("date_part('timezone'::text, created_at) = '0'::double precision"),
        CheckConstraint("date_part('timezone'::text, updated_at) = '0'::double precision")
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('merits_flaws_id_seq'::regclass)"))
    merits_flaws = Column(Text, nullable=False)
    merits_flaws_type_id = Column(ForeignKey('merits_flaws_type.id'), nullable=False)
    merits_flaws_cost = Column(Integer, nullable=False)
    attribute = Column(Text, nullable=False)
    attribute_modifier = Column(Integer, nullable=False)
    updated_at = Column(DateTime(True), nullable=False, server_default=text("now_utc()"))
    created_at = Column(DateTime(True), nullable=False, server_default=text("now_utc()"))

    merits_flaws_type = relationship('MeritsFlawsType')


class MeritsFlawsType(Base):
    __tablename__ = 'merits_flaws_type'
    __table_args__ = (
        CheckConstraint("date_part('timezone'::text, created_at) = '0'::double precision"),
        CheckConstraint("date_part('timezone'::text, updated_at) = '0'::double precision")
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('merits_flaws_type_id_seq'::regclass)"))
    type = Column(Text, nullable=False)
    type_id = Column(Integer, nullable=False)
    updated_at = Column(DateTime(True), nullable=False, server_default=text("now_utc()"))
    created_at = Column(DateTime(True), nullable=False, server_default=text("now_utc()"))


class PoccDb(Base):
    __tablename__ = 'pocc_db'
    __table_args__ = (
        CheckConstraint("date_part('timezone'::text, created_at) = '0'::double precision"),
        CheckConstraint("date_part('timezone'::text, updated_at) = '0'::double precision")
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('pocc_db_id_seq'::regclass)"))
    pocc = Column(Text, nullable=False)
    attribute_modifier_01 = Column(Integer, nullable=False)
    attribute_01 = Column(Text, nullable=False)
    attribute_modifier_02 = Column(Integer, nullable=False)
    attribute_02 = Column(Text, nullable=False)
    updated_at = Column(DateTime(True), nullable=False, server_default=text("now_utc()"))
    created_at = Column(DateTime(True), nullable=False, server_default=text("now_utc()"))


class SoccDb(Base):
    __tablename__ = 'socc_db'
    __table_args__ = (
        CheckConstraint("date_part('timezone'::text, created_at) = '0'::double precision"),
        CheckConstraint("date_part('timezone'::text, updated_at) = '0'::double precision")
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('socc_db_id_seq'::regclass)"))
    socc = Column(Text, nullable=False)
    attribute_modifier = Column(Integer, nullable=False)
    attribute = Column(Text, nullable=False)
    updated_at = Column(DateTime(True), nullable=False, server_default=text("now_utc()"))
    created_at = Column(DateTime(True), nullable=False, server_default=text("now_utc()"))


class UserLogin(Base):
    __tablename__ = 'user_login'
    __table_args__ = (
        CheckConstraint("date_part('timezone'::text, created_at) = '0'::double precision"),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('user_login_id_seq'::regclass)"))
    user_id = Column(ForeignKey('users.id'))
    username_raw = Column(Text)
    login_type_id = Column(ForeignKey('login_type.id'), nullable=False)
    login_result_id = Column(ForeignKey('login_result.id'), nullable=False)
    message = Column(Text)
    ip_address = Column(Text, nullable=False)
    ua_browser = Column(Text)
    ua_os = Column(Text)
    created_at = Column(DateTime(True), nullable=False, server_default=text("now_utc()"))

    login_result = relationship('LoginResult')
    login_type = relationship('LoginType')
    user = relationship('User')


class UserRoll(Base):
    __tablename__ = 'user_roll'
    __table_args__ = (
        CheckConstraint("date_part('timezone'::text, created_at) = '0'::double precision"),
        CheckConstraint("date_part('timezone'::text, updated_at) = '0'::double precision")
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('user_roll_id_seq'::regclass)"))
    name = Column(Text, nullable=False)
    updated_at = Column(DateTime(True), nullable=False, server_default=text("now_utc()"))
    created_at = Column(DateTime(True), nullable=False, server_default=text("now_utc()"))


class User(Base):
    __tablename__ = 'users'
    __table_args__ = (
        CheckConstraint("date_part('timezone'::text, created_at) = '0'::double precision"),
        CheckConstraint("date_part('timezone'::text, updated_at) = '0'::double precision")
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('users_id_seq'::regclass)"))
    active = Column(Boolean, nullable=False, server_default=text("false"))
    user_name = Column(Text)
    password_hash = Column(Text)
    forgot_password_data = Column(Text)
    user_email = Column(Text, nullable=False)
    user_roll = Column(ForeignKey('user_roll.id'), nullable=False)
    updated_at = Column(DateTime(True), nullable=False, server_default=text("now_utc()"))
    created_at = Column(DateTime(True), nullable=False, server_default=text("now_utc()"))

    user_roll1 = relationship('UserRoll')

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    def get_id(self):
        return self.id

    def get_characters(self):
        pass

    def get_friends(self):
        pass

    # def following(self):
    #     """The users that we are following."""
    #     return (
    #         User.select().join(
    #             Relationship, on=Relationship.to_user
    #         ).where(
    #             Relationship.from_user == self
    #         )
    #     )
    #
    # def followers(self):
    #     """Get users following the current user"""
    #     return (
    #         User.select().join(
    #             Relationship, on=Relationship.from_user
    #         ).where(
    #             Relationship.to_user == self
    #         )
    #     )

    @classmethod
    def create_user(self, username, email, password, user_roll=4):
        db = db_session()
        user = User()
        user.active = True
        user.user_name = username
        user.user_email = email
        user.password_hash = password
        user.user_roll = user_roll
        db.add(user)
        db.commit()


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


class FloorModel(object):
    floor_type = 'all'
    breakable = False
    floor_dc = (5, 10)
    floor_soak = 3
    search_level = 0

class FloorStone(FloorModel):
    floor_type = 'stone'
    search_level = 0


class WallModel(object):
    wall_type = 'all'
    breakable = False
    wall_dc = (5, 10)
    wall_soak = 3
    search_level = 0


class WallStone(WallModel):
    wall_type = 'stone'
    breakable = False
    wall_dc = (5, 10)
    wall_soak = 3


class WallEarth(WallModel):
    wall_type = 'earthen'
    breakable = False
    wall_dc = (5, 10)
    wall_soak = 3


class WallCrumbling(WallModel):
    wall_type = 'crumbling'
    breakable = True
    wall_dc = (3, 3)
    wall_soak = 2


class ContainerModel(object):

    container_description = ''
    container_size = ''
    container_weight = 0
    container_dc = (1, 1)
    container_soak = 0
    container_inventory = {}
    container_keywords = {}
    search_level = 1


    def get_description(self):
        return self.container_description

    def unpack_inventory(self):
        for entry in self.container_inventory:
            print(entry, '\n')


class ContainerCrate(ContainerModel):

    container_description = 'This small rotten crate looks as if it was dropped into the well long ago.'
    container_size = ObjectConstants.SMALL
    container_weight = 3
    container_inventory = {'knife': '0'}
    container_keywords = {'crate', 'box', 'chest'}
    search_level = 0


class WeaponMeleeModel(object):

    weapon_description = ''
    weapon_name = ''
    weapon_type = WeaponConstant.MELEE
    weapon_atk = 0
    weapon_dmg = 1
    weapon_dc = (3, 2)
    weapon_modifier = 0
    weapon_limiter = ''

    def get_description(self):
        return self.weapon_description

    def get_name(self):
        return self.weapon_name


class WeaponKnife(WeaponMeleeModel):

    weapon_description = 'This simple carving knife had been forgotten, left to rust, lost perhaps by accident into the darkness.'
    weapon_name = 'Rusted Knife'
    weapon_dc = (2, 2)


class WeaponRangedModel(object):

    weapon_description = ''
    weapon_name = ''
    weapon_type = WeaponConstant.RANGED
    weapon_atk = 0
    weapon_dmg = 1
    weapon_dc = (3, 2)
    weapon_range = (10, 20, 40)
    weapon_rate_of_fire = 1
    weapon_ammo_capacity = 1
    weapon_modifier = 0
    weapon_limiter = ''


class WeaponBow(WeaponRangedModel):

    weapon_description = 'This primitive bow looks as if it could be as much a danger to you as it could be for your target.'
    weapon_name = 'Waterlogged Bow'
    weapon_dmg = 2
    weapon_dc = (2, 2)
    weapon_range = (5, 10, 15)
    
    




class SpeciesDict(object):
    SPECIES_DICT = {'LAND': {'APE': ['M/O', 1, 'wis'],
                             'BADGER': ['M/O', 1, 'con'],
                             'BEAR': ['L/O', 1, 'str'],
                             'BOVINE': ['L/H', 1, 'con'],
                             'BOAR': ['M/H', 1, 'hp'],
                             'CAT': ['M/C', 1, 'dex'],
                             'CAMEL': ['L/H', 2, 'con'],
                             'CHEETAH': ['M/C', 2, 'dex'],
                             'DOG': ['M/C', 1, 'dex'],
                             'DEER': ['M/H', 1, 'cha'],
                             'ELEPHANT': ['L/H', 2, 'wis'],
                             'EMU': ['M/H', 1, 'dex'],
                             'FERRET': ['M/H', 1, 'dex'],
                             'FOX': ['M/O', 1, 'cha'],
                             'GIRAFFE': ['L/H', 1, 'wis'],
                             'GOAT': ['M/H', 1, 'wis'],
                             'HAMSTER': ['S/H', 1, 'con'],
                             'HIPPO': ['L/H', 1, 'con'],
                             'HORSE': ['L/H', 1, 'str'],
                             'HYENA': ['M/C', 1, 'con'],
                             'KANGAROO': ['M/H', 1, 'con'],
                             'KOALA': ['M/H', 1, 'wis'],
                             'LEMUR': ['M/H', 1, 'wis'],
                             'LEOPARD': ['M/C', 1, 'dex'],
                             'LION': ['M/C', 1, 'str'],
                             'LYNX': ['M/C', 1, 'con'],
                             'MANED WOLF': ['M/C', 1, 'dex'],
                             'MEERKAT': ['S/H', 1, 'dex'],
                             'MICE': ['S/H', 1, 'dex'],
                             'MINK': ['S/H', 1, 'cha'],
                             'MONGOOSE': ['S/H', 1, 'dex'],
                             'MONKEY': ['M/O', 1, 'int'],
                             'OSTRICH': ['M/H', 1, 'con'],
                             'OTTER': ['M/O', 1, 'con'],
                             'PIG': ['M/H', 1, 'con'],
                             'PLATYPUS': ['M/H', 1, 'con'],
                             'PUMA': ['M/C', 1, 'dex'],
                             'RABBIT': ['M/H', 1, 'dex'],
                             'RACCOON': ['M/O', 1, 'int'],
                             'RAT': ['M/O', 1, 'dex'],
                             'RED PANDA': ['M/O', 1, 'int'],
                             'RHINO': ['L/H', 1, 'str'],
                             'SEAL': ['M/C', 1, 'con'],
                             'SHREW': ['S/H', 1, 'int'],
                             'SLOTH': ['M/H', 1, 'con'],
                             'SKUNK': ['M/H', 1, 'con'],
                             'SQUIRREL': ['M/H', 1, 'dex'],
                             'TIGER': ['M/C', 1, 'str'],
                             'TURTLE': ['M/O', 1, 'soak'],
                             'WEASEL': ['M/C', 1, 'dex'],
                             'WOLF': ['M/C', 1, 'int'],
                             'ZEBRA': ['L/H', 1, 'wis']
                             },
                    'AIR': {'BAT': ['S/O', 1, 'dex'],
                            'BALD/WHITE TAILED EAGLE': ['L/C', 1, 'str'],
                            'BLUE BIRD': ['S/H', 1, 'int'],
                            'BLUE JAY': ['M/H', 1, 'int'],
                            ' CARDINAL': ['M/H', 1, 'int'],
                            'CHICKEN': ['M/H', 1, 'con'],
                            'CRANE': ['M/H', 1, 'int'],
                            ' CROW': ['M/O', 1, 'con'],
                            ' DOVE': ['S/H', 1, 'cha'],
                            'DUCK': ['M/H', 1, 'wis'],
                            'EAGLE': ['M/C', 1, 'str'],
                            'FLAMINGO': ['M/H', 1, 'cha'],
                            'GRAY JAY': ['M/H', 1, 'con'],
                            'HERON': ['M/H', 1, 'wis'],
                            'HUMMINGBIRD': ['S/H', -1, 'con'],
                            'SEA EAGLE': ['L/C', 1, 'con'],
                            ' SEAGULL': ['M/C', 1, 'dex'],
                            ' SWAN': ['M/H', 1, 'cha'],
                            'SWALLOW': ['S/H', 1, 'dex'],
                            'PENGUIN': ['M/C', 1, 'int'],
                            'PEACOCK': ['M/H', 1, 'cha'],
                            'PUFFIN': ['M/C', 1, 'cha'],
                            'RAVEN': ['M/O', 1, 'int'],
                            ' RED TAIL HAWK': ['M/C', 1, 'str']
                            }
                    }


class MeritsFlawsDicts(object):
    FLAWS = {'MENTAL': {'curiosity': [3, 'search', 2],
                        'hydrophobia': [3, 'water', 2],
                        'naive': [3, 'academics', 1],
                        'prude': [3, 'persuasion', 1],
                        'phobia': [3, 'mental', 2],
                        'stutter': [3, 'cha', 1],
                        'afraid of combat': [4, 'initiative', 2],
                        'combat rage': [4, 'rage', 2],
                        'dead inside': [4, 'empathy', 1],
                        'delusional paranoia': [4, 'cha', 1],
                        'inept': [4, 'knowledge', 2],
                        'memory loss': [4, 'int', 1],
                        'mental scars': [4, 'empathy', 1],
                        'obsessed': [4, 'distracted', 2],
                        'ocd': [4, 'distracted', 2],
                        'over confident': [4, 'social', 2],
                        'primitive heritage': [4, 'knowledge', 2],
                        'short circuit': [4, 'computer', 2],
                        'short temper': [4, 'rage', 2],
                        'curiosity 2': [6, 'search', 4],
                        'epileptic cataleptic': [6, 'mental', 4],
                        'anti-science': [6, 'science', 4],
                        'hero complex': [6, 'alg', 4],
                        'hydrophobia 2': [6, 'water', 4],
                        'quack': [6, 'medicine', 4],
                        'nyctophobia': [6, 'darkness', 4],
                        'phobia 2': [6, 'mental', 4],
                        'species racist': [6, 'species', 4],
                        'superiority complex': [6, 'social', 4],
                        'villain complex': [6, 'alg', 4],
                        'blind': [8, 'perception', 4],
                        'jinx': [8, 'probability', 6]
                        },
             'PHYSICAL': {'allergies': [3, 'physical', 1],
                          'clutz': [3, 'physical', 1],
                          'facial body tick': [3, 'dex', 1],
                          'glutton': [3, 'survival', 1],
                          'one eye': [3, 'attack_power', 1],
                          'odious habit': [3, 'persuasion', 1],
                          'sluggish': [3, 'vitality', 1],
                          'ugly': [3, 'social', 1],
                          'addiction': [4, 'addiction', 1],
                          'blood frenzy': [4, 'rage', 1],
                          'body tremor': [4, 'physical', 1],
                          'combat fear': [4, 'attack_power', 2],
                          'fragile': [4, 'vitality', 1],
                          'low alcohol tolerance': [4, 'alcohol', 1],
                          'mute': [4, 'social', 1],
                          'near far sighted': [4, 'ranged_attack_power', 1],
                          'sickly': [4, 'survival', 1],
                          'weak fragile': [4, 'dmg', 1],
                          'alcoholic': [6, 'social', 2],
                          'allergies 2': [6, 'physical', 2],
                          'addiction 2': [6, 'addiction', 2],
                          'combat terror': [6, 'attack_power', 3],
                          'missing limb': [6, 'stuffing', 1],
                          'lazy': [6, 'con', 2],
                          'naturally low stuffing': [6, 'stuffing', 1],
                          'no alcohol tolerance': [6, 'alcohol', 2],
                          'patchy': [6, 'social', 2],
                          'brittle bones': [8, 'dmg', 2],
                          'patchwork': [8, 'stuffing', 3],
                          'no limbs': [10, 'physical', 6]
                          },
             'STATS': {'imbecile': [4, 'int', 1],
                       'nit-wit': [6, 'int', 2],
                       'wit-less': [8, 'int', 3],
                       'weak': [4, 'str', 1],
                       'feeble': [6, 'str', 2],
                       'powerless': [8, 'str', 3],
                       'lame': [4, 'con', 1],
                       'decrepit': [6, 'con', 2],
                       'debilitated': [8, 'con', 3],
                       'slow': [4, 'dex', 1],
                       'sluggish': [6, 'dex', 2],
                       'torpid': [8, 'dex', 3],
                       'ignorant': [4, 'wis', 1],
                       'obtuse': [6, 'wis', 2],
                       'bewildered': [8, 'wis', 3],
                       'foul': [4, 'cha', 1],
                       'homely': [6, 'cha', 2],
                       'grotesque': [8, 'cha', 3]
                       }
             }
    MERITS = {'MENTAL': {'danger sense': [3, 'perception', 1],
                       'encyclopedic knowledge': [3, 'academics', 1],
                       'iron mind': [3, 'concentration', 1],
                       'speed reader': [3, 'academics', 1],
                       'puzzle solver': [3, 'search', 1],
                       'unseen sense': [3, 'perception', 1],
                       'diamond mind': [4, 'concentration', 2],
                       'linguist': [4, 'academics', 1],
                       'lucky': [4, 'probability', 2],
                       'math savant': [4, 'science', 2],
                       'photographic memory': [4, 'perception', 2],
                       'quick stitch': [4, 'medicine', 1],
                       'quick thinker': [4, 'knowledge', 2],
                       'spell prodigy': [4, 'concentration', 2],
                       'tech savvy': [4, 'computer', 2],
                       'the brain': [6, 'int', 1],
                       'cypher cracker': [6, 'computer', 3],
                       'silver tongue': [6, 'cha', 1],
                       'weaver': [6, 'medicine', 2]
                       },
              'PHYSICAL': {'ambidextrous': [3, 'offhand', 2],
                           'brawler': [3, 'brawl', 1],
                           'dodge': [3, 'dodge', 1],
                           'iron will': [3, 'hp', 1],
                           'quick draw': [3, 'initiative', 2],
                           'quick healer': [3, 'medicine', 1],
                           'quick load': [3, 'initiative', 1],
                           'dirty mouth': [4, 'brawl', 1],
                           'high alcohol tolerance': [4, 'poison resistance', 2],
                           'nimble': [4, 'dex', 1],
                           'throw anything': [4, 'weaponry', 2],
                           'ariel acrobat': [6, 'fly', 2],
                           'blind fighting': [6, 'brawl', 2],
                           'cool under pressure': [6, 'initiative', 3],
                           'dodge 2': [6, 'dodge', 2],
                           'echo location': [6, 'darkness', 2],
                           'endurance': [6, 'athletics', 2],
                           'heighten sense': [6, 'stat', 1],
                           'hard worker': [6, 'con', 1],
                           'hard scales': [6, 'soak', 1],
                           'high jumper': [6, 'physical', 2],
                           'high pain threshold': [6, 'soak', 1],
                           'iron marrow': [6, 'hollow bone', 1],
                           'night vision': [6, 'darkness', 2],
                           'quick shot': [6, 'firearms', 2],
                           'physical prowess': [6, 'str', 2],
                           'prehensile tail': [6, 'dex', 1],
                           'parkour': [6, 'physical', 2],
                           'stunt driver': [6, 'drive', 2],
                           'sprinter': [6, 'physical', 2],
                           'sticky paws': [6, 'physical', 2],
                           'poison tolerance': [6, 'poison resistance', 3],
                           'utilitarian': [6, 'crafting', 3],
                           'weapon specialty': [6, 'weapon spec', 2],
                           'dodge 3': [8, 'dodge', 3],
                           'jack of all trades': [8, 'skills', 1],
                           'poison resistance 2': [8, 'poison resistance', 4],
                           'unbreakable': [8, 'soak', 2],
                           'poison resistance 3': [10, 'poison resistance', 6],
                           'regenerate': [10, 'hp', 1],
                           'only survivor': [10, 'hp', 1]
                           },
              'SOCIAL': {'charismatic': [3, 'cha', 1],
                         'dance fiend': [3, 'expression', 2],
                         'evil eye': [4, 'intimidate', 1],
                         'friend': [3, 'social contacts', 1],
                         'network': [3, 'social contacts', 1],
                         'singer': [3, 'expression', 2],
                         'actor actress': [3, 'cha', 1],
                         'alluring': [4, 'persuasion', 2],
                         'body language': [4, 'persuasion', 2],
                         'beautiful handsome': [4, 'cha', 1],
                         'money': [4, 'money', 2],
                         'prominent fangs': [4, 'intimidate', 2],
                         'master of disguise': [6, 'bluff', 2],
                         'resources': [6, 'streetwise', 3],
                         'sneaky': [6, 'subterfuge', 2],
                         'witty': [6, 'bluff', 2],
                         'loaded': [8, 'money', 5],
                         'most interesting plush in the world': [10, 'cha', 3]}
              }


class OCCs(object):
    SECONDARY_OCC = {
                    'SOLDIER': {'recon': [2, 'investigation'], 'brute': [2, 'brawl'], 'sniper': [2, 'concentration'], 'weapon specialist': [2, 'weaponry'],
                                'motor specialist': [2, 'drive'], 'air specialist': [2, 'fly'], 'combat medic': [2, 'medicine'],
                                'demolitions': [2, 'demolitions']},
                    'MEDIC': {'surgeon': [2, 'medicine'], 'weaver': [2, 'crafting'], 'stuffist': [2, 'science'], 'chemist': [2, 'crafting']},
                    'TECH': {'programmer': [2, 'computer'], 'hacker': [2, 'subterfuge'], 'IT Specialist': [2, 'crafting'],
                             'Security Specialist': [2, 'investigation']},
                    'LAW ENFORCEMENT': {'swat': [2, 'survival'], 'weapon specialist': [2, 'firearms'], 'vice': [2, 'streetwise'],
                                        'detective': [2, 'investigation'], 'private eye': [2, 'social contacts']},
                    'CRIMINAL': {'safe cracker': [2, 'demolitions'], 'nightwalker': [2, 'stealth'], 'thief': [2, 'larceny'],
                                 'smuggler': [2, 'subterfuge'], 'drug dealer': [1, 'social contacts'], 'mob enforcer': [2, 'intimidation'],
                                 'con artist': [2, 'persuasion']},
                    'OCCULTIST': {'ancient lore': [2, 'academics'], 'demonologist': [2, 'occult'], 'ancient catographer': [2, 'crafting'],
                                  'treasure hunter': [2, 'investigation']},
                    'SCHOLAR': {'historian': [2, 'academics'], 'journalist': [2, 'persuasion'], 'investigative reporter': [2, 'investigation'],
                                'information': [2, 'subterfuge']},
                    'MAGICIAN': {},
                    'PSI': {},
                    'ATHLETE': {'marathoner': [2, 'athletics'], 'swimmer': [2, 'swim'], 'Football-NFL': [2, 'brawl'],
                                'Football-FIFA': [2, 'dodge'], 'boxer': [2, 'brawl'], 'olympian': [1, 'str']}
                    }

    PRIMARY_OCC = {'soldier': [1, 'firearms', 1, 'survival'],
                   'medic': [1, 'medicine', 1, 'academics'],
                   'tech': [1, 'computer', 1, 'science'],
                   'law enforement': [1, 'firearms', 1, 'investigation'],
                   'criminal': [1, 'larceny', 1, 'streetwise'],
                   'occultist': [1, 'occult', 1, 'investigation'],
                   'scholar': [1, 'academics', 1, 'science'],
                   'PSI': [1, 'concentration', 1, 'empathy'],
                   'mage': [1, 'concentration', 1, 'academics'],
                   'athlete': [2, 'athletics', 0, 'athletics']
                   }

