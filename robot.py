import serial
import logic as gl
import mapping as m

from serial_cfg import *

class Robot:
    def __init__(self):
        self.mv_left = serial.Serial(MV_LEFT_PORT, BAUD_RATE)
        self.mv_right = serial.Serial(MV_RIGHT_PORT, BAUD_RATE)
        self.motor_driver = serial.Serial(MOTOR_DRIVER_PORT, BAUD_RATE)

        self.logic = gl.GameLogic(self)
        self.mapper = m.Mapper(self)
        
    def __del__(self):
        pass

    def run(self):
        self.updatePosition()
        self.updateState()
        self.execute()

    def updatePosition(self):
        self.mv_left.write("s")
        self.left_data = self.mv_left.readline()
        self.mv_right.write("s")
        self.right_data = self.mv_right.readline()
    
    def updateState(self):
        pass


    def execute(self):
        # self.current_state.func()

