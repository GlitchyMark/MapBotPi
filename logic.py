import time

class State:
    def __init__(self, xpos, ypos, targetXpos, targetYpos, theta, func):
        self.xpos = xpos
        self.ypos = ypos
        self.targetXpos = targetXpos
        self.targetYpos = targetYpos
        self.theta = theta
        self.func = func

    def __eq__(self, other):
        if self.xpos != other.xpos:
            return False
        elif self.ypos != other.ypos:
            return False
        elif self.theta != other.theta:
            return False
        else:
            return True

class StateBuffer:
    def __init__(self):
        self.buffer = list()
        self.current_state = None

    def addState(self, state):
        self.buffer.append(state)
        self.current_state = self.buffer[len(self.buffer)-1]  # current_state is the new addition
        if len(self.buffer) > 10:
            self.buffer.pop(0)  # remove the head

    def get(self, index):
        try:
            return self.buffer[index]
        except IndexError:
            return None

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
        print("Do we get here?")
        self.owner.motor_driver.rotate(10000)
        self.owner.motor_driver.moveFR(10000, 0)
        while True:
            print(self.owner.motor_driver.port.readline())
            time.sleep(1)
