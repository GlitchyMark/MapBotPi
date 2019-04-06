class Mapper:
    def __init__(self, owner):
        self.owner = owner
        self.block_list = list()

class Block:
    def __init__(self, color, xpos, ypos, distance_from):
        self.color = color
        if distance_from is None:
            self.xpos = xpos
            self.ypos = ypos
        else:
            pass