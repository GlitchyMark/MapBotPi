##
##  VCU IEEE ROBOT 2018 - 2019
##  
##  peripheral.py
##  Written by Xander Will / Akib Rhaat
##
##  'Wrappers for peripherals including flag'

import serial
import json

from gpiozero import AngularServo


class Peripheral:
    def __init__(self, address, baud, debug=False):
        self.port = serial.Serial(address, baud)
        self.debug = debug 

    def getData(self):
        return {}


class Camera(Peripheral):
    """ Handles communication with the OpenMV """

    def getData(self):
        a = self.port.readline().rstrip().replace("'",'"')
        if self.debug:
            print(a)
        return json.loads(a)

class MPU(Peripheral):
    """ Handles communication with the MPU """

    def getData(self):
        a = self.port.readline().rstrip()
        if self.debug:
            print(a)
        return json.loads(a)

class Flag:
    """ Controls a wooden flag connected to a
        GPIO servo """
    def __init__(self):
        self.servoFlag = AngularServo(13, min_angle=-90, max_angle=90) 

    def raiseFlag(self):
        self.servoFlag.angle = 5

    def lowerFlag(self):
        self.servoFlag.angle = -5
    