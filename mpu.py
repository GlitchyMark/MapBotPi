##
##  VCU IEEE ROBOT 2018 - 2019
##  
##  mpu.py
##  Written by Xander Will
##
##  'Wrapper for the MPU9250'

import serial
import json

class MPU:
    def __init__(self, address, baud):
        self.port = serial.Serial(address, baud)
    
    def getData(self):
        data = json.loads(self.port.readline().rstrip())
        return data #.update({lambda n: 39.3701*data[n] for n in data})   # meters to inches