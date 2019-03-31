import serial

from serial_cfg import *

class Robot:
    def __init__(self):
        self.mv_left = serial.Serial(MV_LEFT_PORT, BAUD_RATE)
        self.mv_right = serial.Serial(MV_RIGHT_PORT, BAUD_RATE)
        self.motor_driver = serial.Serial(MOTOR_DRIVER_PORT, BAUD_RATE)
        
    def __del__(self):
        pass

    def run(self):
        pass

    def updatePosition(self):
        pass 
    
    def updateState(self):
        pass

    def execute(self):
        pass

class State:
    def __init__(self):
        pass
