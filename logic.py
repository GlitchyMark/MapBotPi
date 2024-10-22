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

    def __init__(self, camera_ldata, camera_rdata, mpu_data, func, prev_func):
        self.camera_ld = camera_ldata
        self.camera_rd = camera_rdata
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
            self.motor_driver.setTargetVelocities(x=-1, a=0.6) # hardcoded from tests
            cs.next_func = self.startUp
        else:   # wait until first correction check
            if cs.camera_d.get("distance") is not None:
                if checkIfClose(cs.camera_d.get("angle"), 0, tolerance=5):    # hardcoded from tests
                    cs.next_func = self.constantSpin
                else:
                    cs.next_func = self.startUp

    static_a = 1.0    # TEST THIS
    stop_a  = 5.0    # TEST THIS
    def helix(self):
        """ Spin in a ever-shrinking circle
            into the center of the arena """
        # not used anymore :(

        # cs = self.state_buffer.current_state
        # self.motor_driver.setTargetVelocities(x=1.0, a=self.static_a)
        # self.static_a += 0.001
        # if self.static_a == self.stop_a:
        #     cs.next_func = self.constantSpin
        # else:
        #     cs.next_func = self.helix
        pass
    
    FEEDBACK_COEFF = 0.1
    FORWARD_V = -2.5
    angular_v = 20
    def constantSpin(self):
        """ Spin around the center pole """
        
        DISTANCE = 35.5
        

        cs = self.state_buffer.current_state
        if checkIfClose(cs.camera_rd.get("angle"), 0, tolerance=5):
            self.angular_v += self.FEEDBACK_COEFF*(cs.camera_rd.get("distance") - DISTANCE)
        self.motor_driver.setTargetVelocities(x=self.FORWARD_V, a=self.angular_v)
        cs.next_func = self.constantSpin
    
    def hitByOpponent(self):
        """ If accelerometer changes significantly, stop
            and return to circle """
        self.motor_driver.stop()
        self.motor_driver.moveFR(f=-2)
        self.state_buffer.current_state.next_func = self.constantSpin

    def returnToCircle(self):
        """ In cases where the main path has been
            lost, reroute to our old position and
            setup the circle path again """
        # unfinifhsed :()
        cs = self.state_buffer.current_state
        if cs.prev_func != self.returnToCircle: # state entry
            pass
           

    before_home_lookup = {
        "YELLOW"    :   "BLUE",
        "RED"       :   "YELLOW",
        "GREEN"     :   "RED",
        "BLUE"      :   "GREEN"
    }
    def endgame(self):
        """ Find home base and begin returning """
        cs = self.state_buffer.current_state
        self.target_color = self.before_home_lookup.get(self.owner.home)
        if cs.camera_ld.get("color") == self.target_color:
            self.motor_driver.setTargetVelocities(x=1.0, a=-0.3)
            cs.next_func = self.reachHomeBase
        else:
            cs.next_func = self.endgame

    def reachHomeBase(self):
        """ Wait to stop in home base"""
        cs = self.state_buffer.current_state
        if cs.camera_rd("distance") <= 14:
            self.motor_driver.moveFR(f=14)
            self.motor_driver.stop()
            cs.next_func = self.raiseFlag
        else:
            cs.next_func = self.reachHomeBase

    def raiseFlag(self):
        """ Raises the flag at the end of the game """
        cs = self.state_buffer.current_state
        self.owner.flag.raiseFlag()
        self.motor_driver.setMotionAllowed(0)
        cs.next_func = self.stall

    def stall(self):
        """ Just chill until the match is over :) """
        pass
        
    def debug(self, arg=None):
        """ Called when 'debug' command line is used """
        if arg is not None:
            self.FORWARD_V = arg[0]
            self.angular_v = arg[1]
            self.FEEDBACK_COEFF = arg[2]
        while True:
            self.owner.run()

def checkIfClose(x, y, tolerance):
    """ Used for state transition when
        a certain point is reached """
    try:
        if abs(x - y) < tolerance:
            return True
        return False
    except:
        return False