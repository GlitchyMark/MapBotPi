import time

class State:
    def __init__(self, xpos, ypos, targetXpos, targetYpos, theta, func, prev_func):
        self.xpos = xpos
        self.ypos = ypos
        self.targetXpos = targetXpos
        self.targetYpos = targetYpos
        self.theta = theta
        self.func = func
        self.prev_func = None
        self.next_func = None

    def __eq__(self, other):
        if self.xpos != other.xpos:
            return False
        elif self.ypos != other.ypos:
            return False
        elif self.targetXpos != other.targetXpos:
            return False
        elif self.targetYpos != other.targetYpos:
            return False
        elif self.theta != other.theta:
            return False
        else:
            return True

class StateBuffer:
    def __init__(self):
        self.buffer = list()
        self.current_state = None
        self.len = 0

    def addState(self, state):
        self.len += 1
        self.buffer.append(state)
        self.current_state = self.buffer[len(self.buffer)-1]  # current_state is the new addition
        if len(self.buffer) > 10:
            self.buffer.pop(0)  # remove the head
            self.len -= 1

    def get(self, index):
        try:
            return self.buffer[index]
        except IndexError:
            return None

class GameLogic:
    def __init__(self, owner):
        self.owner = owner
        self.state_buffer = owner.state_buffer

    def startUp(self):
        current_state = self.state_buffer.current_state
        if current_state.prev_func != self.startUp:        
            current_state.targetXpos = 54   # halfway point of the field
            if current_state.ypos < 54:     
                current_state.targetYpos = 30   # just an arbitrary starting point for the circle atm
            else:
                current_state.targetYpos = 78
            self.owner.motor_driver.gotoXYA(current_state.targetXpos, current_state.targetYpos, 69) # dunno A yet
        else:
            if abs(current_state.xpos - current_state.targetXpos) < 3:
                if abs(current_state.ypos - current_state.targetYpos) < 3:
                    current_state.next_func = self.followCircle
        current_state.next_func = self.startUp

    def getToCircle(self):
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
        while True:
            self.owner.motor_driver.resetPosition(0, 0, 0)
            self.owner.motor_driver.setMaxVelocities(3, 3, 2)
            self.owner.motor_driver.setMaxAccelerations(10, 10, 5)
            self.owner.motor_driver.moveFR(0, 1000)
            self.owner.motor_driver.rotateTo(1000)
           # self.owner.motor_driver.gotoXYA(10, 10, 90)
            print(self.owner.motor_driver.port.readline())
            time.sleep(100)
