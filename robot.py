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
from positioning import Accelerometer
from camera import Camera

from serial_cfg import MV_PORT, MOTOR_DRIVER_PORT, BAUD_RATE

class Robot:
    """ Director class, holds the game loop
        as well as data collection, state 
        buffer manipulation, time management
        and minor bits of logic """
        
    def __init__(self):
        self.start_time = time.time()

        self.camera = Camera(MV_PORT, BAUD_RATE)
        self.motor_driver = MotorDriverInterface(MOTOR_DRIVER_PORT, BAUD_RATE)
        self.accelerometer = Accelerometer()
        self.logic = GameLogic(self)
        self.mapper = Mapper()
        self.state_buffer = StateBuffer()

        self.state_buffer = list()
        self.state_buffer.addState(State(0,0,0,0,0,None,None))

    def run(self):
        self.updatePosition()
        self.updateState()
        self.execute()

    def updatePosition(self):
        self.camera_data = self.camera.getData()
        self.telemetry = self.motor_driver.getTelemetry()

        self.xpos, self.ypos = self.telemetry["xpos"], self.telemetry["ypos"]
        for obj in self.camera_data:
            if obj["pole"] is True:
                theta = self.telemetry["angle"] - obj["angle"]
                self.xpos, self.ypos = self.mapper.getCurrPosFromPole(obj["color"], theta, obj["distance"])
 
    def updateState(self):
        txpos = self.state_buffer.current_state.targetXpos
        typos = self.state_buffer.current_state.targetYpos
        prev_func = self.state_buffer.current_state.func
        func = self.state_buffer.current_state.next_func
        self.state_buffer.addState(State(self.xpos, self.ypos, txpos, typos, self.telemetry["angle"], func, prev_func))

    def execute(self):
        self.state_buffer.current_state.func()

