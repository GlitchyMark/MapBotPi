##
##  VCU IEEE ROBOT 2018 - 2019
##  
##  logic.py
##  Written by Xander Will / Mark Johnston
##
##  'Classes for performing game logic'

import time

class State:
    """ Used to track data between logic states, and
        to preserve old data as well """

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

TOLERANCE = 3.0
class StateBuffer:
    """ Wrapper for our list of states 
        Use current_state directly to 
        get the current_state """

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

    def reversed(self):
        return reversed(self.buffer)


class GameLogic:
    """ The actual state machine, holds
        all of the functions for robot execution """

    def __init__(self, owner):
        self.owner = owner
        #self.motor_driver = owner.motor_driver
        #self.state_buffer = owner.state_buffer

    def startUp(self):
        """ Initial state, finds the first position
            of our circle """
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
            if checkIfClose(cs.xpos, cs.targetXpos, cs.ypos, cs.targetYpos, TOLERANCE) == True:
                cs.next_func = self.setupCircle  # transition to setupCircle state
            else:
                cs.next_func = self.startUp

    def setupCircle(self):
        """ Sends the motor driver command that
            will begin robot rotation """
        cs = self.state_buffer.current_state
        radius = 0  # add increment radius code, based on however we're doing that
                    # if we're gonna properly spiral, may need to add code that moves the robot in a bit
        self.owner.motor_driver.gotoXYA(cs.targetXpos, cs.targetYpos, radius)
        cs.next_func = self.followCircle
    
    def followCircle(self):
        """ Intermediary state between calls
            to setupCircle() """
        cs = self.state_buffer.current_state
        if checkIfClose(cs.xpos, cs.targetXpos, cs.ypos, cs.targetYpos, TOLERANCE) == True:
            cs.next_func = self.setupCircle  # setup the next circle 
        else:
            cs.next_func = self.followCircle

    def retrieveCube(self):
        # gonna leave this one blank for the time being
        pass
    
    def hitByOpponent(self):
        """ If accelerometer changes significantly, stop
            and return to circle """
        self.motor_driver.stop()
        self.state_buffer.current_state.next_func = self.returnToCircle
        pass 

    def returnToCircle(self):
        """ In cases where the main path has been
            lost, reroute to our old position and
            setup the circle path again """
        cs = self.state_buffer.current_state
        if cs.prev_func != self.returnToCircle: # state entry
            for state in self.state_buffer.reversed():
                if state.func == self.followCircle or state.func == self.setupCircle:
                    position = state.xpos, state.ypos
            self.motor_driver.gotoXY(position[0], position[1])
        else:   # wait until destination reached to restart circle
            if checkIfClose(cs.xpos, cs.targetXpos, cs.ypos, cs.targetYpos, TOLERANCE) == True:
                cs.next_func = self.setupCircle
            else:
                cs.next_func = self.returnToCircle
        pass

    def endgame(self):
        """ Return to starting position from current
            location """
        pass

    def raiseFlag(self):
        """ Raises the flag at the end of the game """
        pass

    def stall(self):
        """ Just chill until the match is over :) """
        pass
        
    def debug(self):
        """ Called when 'debug' command line is used """
        print("Do we get here?")
        while True:
            self.owner.motor_driver.resetPosition(0, 0, 0)
            self.owner.motor_driver.setMaxVelocities(3, 0, 2)
            self.owner.motor_driver.setMaxAccelerations(10, 0, 5)
            self.owner.motor_driver.moveFR(1000, 0)
            self.owner.motor_driver.rotateTo(1000)
           # self.owner.motor_driver.gotoXYA(10, 10, 90)
            print(self.owner.motor_driver.port.readline())
            time.sleep(100)

def checkIfClose(x1, x2, y1, y2, tolerance):
    """ Used for state transition when
        a certain point is reached """
    if abs(x1 - x2) < tolerance:
        if abs(y1 - y2) < tolerance:
            return True
    return False