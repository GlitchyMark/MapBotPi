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
from camera import Camera
from mpu import MPU
from accessory import Flag

from serial_cfg import *

class Robot:
    """ Director class, holds the game loop
        as well as data collection, state 
        buffer manipulation, time management
        and minor bits of logic """
        
    def __init__(self):
        self.home = "RED"   # default home base

        self.state_buffer = StateBuffer()
        self.state_buffer.addState(State(None,None,None,None,None))

        self.camera_left = Camera(MV_LEFT_PORT, BAUD_RATE)
        self.camera_right = Camera(MV_RIGHT_PORT, BAUD_RATE)
        self.mpu = MPU(NANO_PORT, NANO_BAUD)
        self.motor_driver = MotorDriverInterface(MOTOR_DRIVER_PORT, BAUD_RATE, debug=True)
        self.logic = GameLogic(self)
        self.mapper = Mapper()
        self.flag = Flag()
        self.state_buffer = StateBuffer()


    def startTime(self):
        self.start_time = time.time()

    def run(self):
        self.curr_time = time.time() - self.start_time
        self.updatePosition()
        self.updateState()
        self.execute()

    def updatePosition(self):
        self.camera_ldata = self.camera_left.getData()
        self.camera_rdata = self.camera_right.getData()
        self.mpu_data = self.mpu.getData()
 
    def updateState(self):
        ps = self.state_buffer.getPrevious()
        if AccelerationCheck(ps.mpu_d, self.mpu_data):
            func = self.logic.hitByOpponent
        elif self.curr_time >= 150 and self.state_buffer.current_state.prev_func != self.logic.endgame:
            func = self.logic.endgame
        else:
            func = self.state_buffer.current_state.next_func
        prev_func = self.state_buffer.current_state.func
        self.state_buffer.addState(State(self.camera_ldata, self.camera_rdata, self.mpu_data, func, prev_func))

    def execute(self):
        self.state_buffer.current_state.func()

def AccelerationCheck(new_a, old_a):
    new_a_tup = new_a.get("ax"), new_a.get("ay"), new_a.get("az")
    old_a_tup = old_a.get("ax"), old_a.get("ay"), old_a.get("az")
    diff = abs(new_a_tup - old_a_tup)
    for num in diff:
        if num > 40:    # arbitrary value? please test
            return True
    return False