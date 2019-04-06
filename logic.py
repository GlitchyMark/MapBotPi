class State:
    def __init__(self, xpos, ypos, theta, func):
        self.xpos = xpos
        self.ypos = ypos
        self.theta = theta
        self.func = func

class GameLogic:
    def __init__(self, owner):
        self.owner = owner

    def startUp(self):
        pass

    def followCircle(self):
        pass

    def retrieveCube(self):
        pass
    
    def returnToCircle(self):
        pass

    def hitByOpponent(self):
        pass 

    def endgame(self):
        pass

    def stall(self):
        pass
        
    def debug(self):
        pass