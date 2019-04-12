##
##  VCU IEEE ROBOT 2018 - 2019
##  
##  logic.py
##  Written by Xander Will
##
##  'Classes for performing game logic'

import time
import math

class State:
    """ Used to track data between logic states, and
        to preserve old data as well """

    def __init__(self, camera_data, mpu_data, func, prev_func):
        self.camera_d = camera_data
        self.mpu_d = mpu_data
        self.func = func
        self.prev_func = None
        self.next_func = None

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

TOLERANCE = 3.0
class GameLogic:
    """ The actual state machine, holds
        all of the functions for robot execution """

    def __init__(self, owner):
        self.owner = owner
        self.motor_driver = owner.motor_driver
        self.state_buffer = owner.state_buffer

    home_lookup = {
        "YELLOW"    :   "RED",
        "RED"       :   "GREEN",
        "GREEN"     :   "BLUE",
        "BLUE"      :   "YELLOW"
    }
    def startUp(self):
        """ Initial state, finds the first position
            of our circle """
        cs = self.state_buffer.current_state
        if cs.prev_func != self.startUp:        # state entry
            self.owner.home = self.home_lookup.get(cs.camera_data.get("color"))
            self.motor_driver.setTargetVelocities(x=2, a=0.3) # dunno A yet
            cs.next_func = self.startUp
        else:   # wait until at circle
            if cs.camera_d.get("distance") is not None:
                if checkIfClose(cs.camera_d.get("distance"), 60, TOLERANCE):    # arbitrary value, please test
                    cs.next_func = self.helix  # transition to setupCircle state
                else:
                    cs.next_func = self.startUp

    static_a = 1    # TEST THIS
    stop_a  = 5    # TEST THIS
    def helix(self):
        """ Spin in a ever-shrinking circle
            into the center of the arena """
        cs = self.state_buffer.current_state
        self.motor_driver.setTargetVelocities(x=1.0, a=self.static_a)
        self.static_a += 0.1
        if self.static_a == self.stop_a:
            cs.next_func = self.constantSpin
        else:
            cs.next_func = self.helix
    
    def constantSpin(self):
        """ Spin around the center pole """
        cs = self.state_buffer.current_state
        self.motor_driver.setTargetVelocities(x=1.0, a=self.stop_a)
        cs.next_func = self.constantSpin
    
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
        # cs = self.state_buffer.current_state
        # if cs.prev_func != self.returnToCircle: # state entry
        #     for state in self.state_buffer.reversed():
        #         if state.func == self.followCircle or state.func == self.setupCircle:
        #             position = state.xpos, state.ypos
        #     self.motor_driver.gotoXY(position[0], position[1])
        # else:   # wait until destination reached to restart circle
        #     if checkIfClose(cs.xpos, cs.targetXpos, TOLERANCE) == True:
        #         cs.next_func = self.setupCircle
        #     else:
        #         cs.next_func = self.returnToCircle
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
            self.owner.motor_driver.setTargetVelocities(2, 2)
           # self.owner.motor_driver.gotoXYA(10, 10, 90)
            print(self.owner.motor_driver.port.readline())
            time.sleep(100)

def checkIfClose(x, y, tolerance):
    """ Used for state transition when
        a certain point is reached """
    if abs(x - y) < tolerance:
        return True
    return False