from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Numeric, Text, text, Time
from sqlalchemy import CheckConstraint
from sqlalchemy import Date
from sqlalchemy import and_
from sqlalchemy import func
from sqlalchemy import null
from sqlalchemy import or_
from sqlalchemy.orm import relationship
from database_service import Base

metadata = Base.metadata

class Navigation(object):
    def grid_coor(self, coor_x, coor_y, coor_z):
        pass

    def moveNorth(self, move):
        '''

        :param move: takes an int
        :return: grid_coor incremented + on coor_y
        '''
        # y+
        pass

    def moveSouth(self, move):
        '''

        :param move: int
        :return: grid_coor incremented - on coor_y
        '''
        # y-
        pass

    def moveEast(self, move):
        '''

        :param move: int
        :return: grid_coor incremented on coor_y
        '''
        # x+
        pass

    def moveWest(self, move):
        '''

        :param move: int
        :return: grid_coor incremented on coor_y 
        '''
        # x-
        pass

    def moveDown(self, move):
        '''

        :param move: int
        :return: grid_coor incremented on coor_y 
        '''
        # z+
        pass

    def moveUp(self, move):
        '''

        :param move: int
        :return:grid_coor incremented on coor_y 
        '''
        # z-
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

    id = Column(Integer, primary_key=True, server_default=text("nextval('character_id_seq'::regclass)"))
    code = Column(Text, nullable=False)
    name = Column(Text, nullable=False)
    species = Column(Text, nullable=False)
    species_size = Column(Text, nullable=False)
    sex = Column(Text, nullable=False)
    faction = Column(Text)
    alg = Column(Text, nullable=False)
    pocc = Column(Text, nullable=False)
    socc = Column(Text)
    exp_total = Column(Integer, nullable=False)
    exp_remaining = Column(Integer, nullable=False)
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
    skills = Column(Text)
    merits = Column(Text)
    flaws = Column(Text)
    updated_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, nullable=False)


class CharacterCode(Base):
    __tablename__ = 'character_code'

    id = Column(Integer, primary_key=True, server_default=text("nextval('character_code_id_seq'::regclass)"))
    code = Column(Text, nullable=False)
    display_name = Column(Text)
    updated_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, nullable=False)


class InventoryPc(Base):
    __tablename__ = 'inventory_pc'

    id = Column(Integer, primary_key=True, server_default=text("nextval('inventory_pc_id_seq'::regclass)"))
    code = Column(Text, nullable=False)
    character_id = Column(Text, nullable=False)
