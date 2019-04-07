import serial
import json

from logic import State, StateBuffer, GameLogic
from mapping import Mapper
from motor_driver import MotorDriverInterface

from serial_cfg import *

class Robot:
    def __init__(self):
        self.mv_left = serial.Serial(MV_LEFT_PORT, BAUD_RATE)
        self.mv_right = serial.Serial(MV_RIGHT_PORT, BAUD_RATE)

        self.motor_driver = MotorDriverInterface()
        self.logic = GameLogic(self)
        self.mapper = Mapper(self)
        self.state_buffer = StateBuffer()

        self.state_buffer = list()

    def run(self):
        self.updatePosition()
        self.updateState()
        self.execute()

    def updatePosition(self):
        self.mv_left.write("s")
        self.left_data = json.loads(self.mv_left.readline())
        self.mv_right.write("s")
        self.right_data = json.loads(self.mv_right.readline())
  
    def updateState(self):
        pass
        # self.state_buffer.append(State())

    def execute(self):
        self.state_buffer.current_state.func()

