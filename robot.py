##
##  VCU IEEE ROBOT 2018 - 2019
##  
##  robot.py
##  Written by Xander Will
##
##  'Main class that directs game loop'

import serial
import json
import time

from logic import State, StateBuffer, GameLogic
from mapping import Mapper
from motor_driver import MotorDriverInterface
from peripheral import Camera, MPU, Flag

from serial_cfg import *

class Robot:
    """ Director class, holds the game loop
        as well as data collection, state 
        buffer manipulation, time management
        and minor bits of logic """
        
    def __init__(self, debug=False):
        self.state_buffer = StateBuffer()
        self.state_buffer.addState(State(None,None,None,None,None))

        self.camera_left = Camera(MV_LEFT_PORT, MV_BAUD, debug)
        self.camera_right = Camera(MV_RIGHT_PORT, MV_BAUD, debug)
        self.mpu = MPU(NANO_PORT, NANO_BAUD)
        self.motor_driver = MotorDriverInterface(MOTOR_DRIVER_PORT, MD_BAUD, debug)
        self.logic = GameLogic(self)
        self.mapper = Mapper()
        self.flag = Flag()

        self.home = self.camera_left.getData().get("color")

    def startTime(self):
        self.start_time = time.time()

    def run(self):
        self.curr_time = time.time() - self.start_time
        self.updatePosition()
        self.updateState()
        self.execute()
        time.sleep(0.1)

    def updatePosition(self):
        self.camera_ldata = self.camera_left.getData()
        self.camera_rdata = self.camera_right.getData()
        self.mpu_data = self.mpu.getData()
 
    def updateState(self):
        cs = self.state_buffer.current_state
        ps = self.state_buffer.getPrevious()
        if cs.func is None:
            cs.next_func = self.logic.startUp
        elif AccelerationCheck(ps.mpu_d, self.mpu_data):
            func = self.logic.hitByOpponent
        elif self.curr_time >= 150 and cs.prev_func != self.logic.endgame:
            func = self.logic.endgame
        else:
            func = cs.next_func
        prev_func = cs.func
        self.state_buffer.addState(State(self.camera_ldata, self.camera_rdata, self.mpu_data, func, prev_func))

    def execute(self):
        self.state_buffer.current_state.func()

def AccelerationCheck(new_a, old_a):
    try:
        new_a_tup = new_a.get("ax"), new_a.get("ay"), new_a.get("az")
        old_a_tup = old_a.get("ax"), old_a.get("ay"), old_a.get("az")
        diff = abs(new_a_tup - old_a_tup)
        for num in diff:
            if num > 40:    # arbitrary value? please test
                return True
    except:
        print("Acceleration check failed: use MPU data only!")
    finally:
        return False