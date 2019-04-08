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

    def getPrevious(self):
        try:
            return self.buffer[len(self.buffer)-2]
        except IndexError:
            return None


class GameLogic:
    def __init__(self, owner):
        self.owner = owner
        self.motor_driver = owner.motor_driver
        self.state_buffer = owner.state_buffer

    def startUp(self):
        cs = self.state_buffer.current_state
        if cs.prev_func != self.startUp:        # state entry
            cs.targetXpos = 54   # halfway point of the field
            if cs.ypos < 54:     
                cs.targetYpos = 30   # just an arbitrary starting point for the circle atm
            else:
                cs.targetYpos = 78
            self.motor_driver.gotoXYA(cs.targetXpos, cs.targetYpos, 69) # dunno A yet
            cs.next_func = self.startUp
        else:   # wait until at circle
            if checkIfClose(cs.xpos, cs.targetXpos, cs.ypos, cs.targetYpos, 3) == True:
                cs.next_func = self.setupCircle  # transition to setupCircle state
            else:
                cs.next_func = self.startUp
        

    def setupCircle(self):
        cs = self.state_buffer.current_state
        radius = 0  # add increment radius code, based on however we're doing that
                    # if we're gonna properly spiral, may need to add code that moves the robot in a bit
        self.owner.motor_driver.gotoXYA(cs.targetXpos, cs.targetYpos, radius)
        cs.next_func = self.followCircle
    
    def followCircle(self):
        cs = self.state_buffer.current_state
        if checkIfClose(cs.xpos, cs.targetXpos, cs.ypos, cs.targetYpos, 3) == True:
            cs.next_func = self.setupCircle  # setup the next circle 
        else:
            cs.next_func = self.followCircle

    def retrieveCube(self):
        # gonna leave this one blank for the time being
        pass
    
    def hitByOpponent(self):
        self.motor_driver.stop()
        self.state_buffer.current_state.next_func = self.returnToCircle
        pass 

    def returnToCircle(self):
        cs = self.state_buffer.current_state
        if cs.prev_func != self.returnToCircle: # state entry
            for state in reversed(self.state_buffer):
                if state.func == self.followCircle or state.func == self.setupCircle:
                    position = state.xpos, state.ypos
            self.motor_driver.gotoXY(position[0], position[1])
        else:   # wait until destination reached to restart circle
            if checkIfClose(cs.xpos, cs.targetXpos, cs.ypos, cs.targetYpos, 3) == True:
                cs.next_func = self.setupCircle
            else:
                cs.next_func = self.returnToCircle
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

def checkIfClose(x1, x2, y1, y2, tolerance):
    if abs(x1 - x2) < 3.0:
        if abs(y1 - y2) < 3.0:
            return True
    return False