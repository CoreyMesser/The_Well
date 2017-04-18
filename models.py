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
