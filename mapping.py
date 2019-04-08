import math

class Mapper:
    # everything is in inches!!!
    pos_table = {
        "yellow" :  (0, 0),
        "red"    :  (0, 108),
        "blue"   :  (108, 0),
        "green"  :  (108, 108)
    }

    def __init__(self):
        self.block_list = list()

    def getCurrPosFromPole(self, color, theta, distance_from):
        ref_pos = self.pos_table[color]
        xpos = distance_from * math.sin(theta) + ref_pos[0]
        if xpos > 108:
            xpos -= 108
        ypos = distance_from * math.cos(theta) + ref_pos[1]
        if ypos > 108:
            ypos -= 108
        return xpos, ypos

            

class Block:
    def __init__(self, color, xpos, ypos, theta, distance_from, pole=False):
        self.color = color
        self.pole = pole
        self.xpos = distance_from * math.sin(theta) + xpos
        self.ypos = distance_from * math.cos(theta) + ypos
