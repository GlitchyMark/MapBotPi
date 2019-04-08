##
##  VCU IEEE ROBOT 2018 - 2019
##  
##  motor_driver.py
##  Written by Xander Will
##
##  'OO interface for 2017 motor driver'

import serial
import time
import json

class MotorDriverInterface:
    """ Interface for talking to the
        motor driver, each method wraps
        a set of commands"""

    def __init__(self, address, baud):
        self.port = serial.Serial(address, baud)
        self.setMotionAllowed(True)
        # self.setTargetVelocities(0.3, 0.3, 0.25)
        self.setMaxVelocities(5, 5, 5)
        self.setMaxAccelerations(1.5, 1.5, 1.5)
        self.setMaxAccelerations(1.5, 1.5, 1.5)     # to ensure it doesn't get dropped

    def __del__(self):
        self.setMotionAllowed(False)

    def getTelemetry(self):
        return json.loads(self.port.readline())

    def debugWrite(self, s):
        self.port.write(s)
        print(s)
        time.sleep(0.0001)

    def setMotionAllowed(self, value):
        if value is True:
            self.debugWrite(b"[setMotionAllowed=1]")
        else:
            self.debugWrite(b"[setMotionAllowed=0]")

    def stop(self):
        self.debugWrite(b"[stop=0]")

    def setTargetVelocities(self, x=None, y=None, a=None):
        if x is not None:
            self.debugWrite(b"[setCommandX=" + str(x).encode('ascii') + b"]")
        if y is not None:
            self.debugWrite(b"[setCommandY=" + str(y).encode('ascii') + b"]")
        if a is not None:
            self.debugWrite(b"[setCommandA=" + str(a).encode('ascii') + b"]")
        self.debugWrite(b"[setTargetVelocities=0]")

    def setMaxVelocities(self, x=None, y=None, a=None):
        if x is not None:
            self.debugWrite(b"[setCommandX=" + str(x).encode('ascii') + b"]")
        if y is not None:
            self.debugWrite(b"[setCommandY=" + str(y).encode('ascii') + b"]")
        if a is not None:
            self.debugWrite(b"[setCommandA=" + str(a).encode('ascii') + b"]")
        self.debugWrite(b"[setMaxVelocities=0]")
        
    def setMaxAccelerations(self, x=None, y=None, a=None):
        if x is not None:
            self.debugWrite(b"[setCommandX=" + str(x).encode('ascii') + b"]")
        if y is not None:
            self.debugWrite(b"[setCommandY=" + str(y).encode('ascii') + b"]")
        if a is not None:
            self.debugWrite(b"[setCommandA=" + str(a).encode('ascii') + b"]")
        self.debugWrite(b"[setMaxAccelerations=0]")

    def setMicrostepping(self, step):
        self.debugWrite(b"[setMicrostepping=" + str(step & 0xFF) + b"]")

    def gotoXYA(self, x=None, y=None, a=None):
        if x is not None:
            self.debugWrite(b"[setCommandX=" + str(x).encode('ascii') + b"]")
        if y is not None:
            self.debugWrite(b"[setCommandY=" + str(y).encode('ascii') + b"]")
        if a is not None:
            self.debugWrite(b"[setCommandA=" + str(a).encode('ascii') + b"]")
        self.debugWrite(b"[gotoXYA=0]")

    def gotoXY(self, x=None, y=None, a=None):
        if x is not None:
            self.debugWrite(b"[setCommandX=" + str(x).encode('ascii') + b"]")
        if y is not None:
            self.debugWrite(b"[setCommandY=" + str(y).encode('ascii') + b"]")
        self.debugWrite(b"[gotoXY=0]")

    def moveFR(self, f=None, r=None):
        if f is not None:
            self.debugWrite(b"[setCommandX=" + str(f).encode('ascii') + b"]")
        if r is not None:
            self.debugWrite(b"[setCommandY=" + str(r).encode('ascii') + b"]")
        self.debugWrite(b"[moveFR=0]")

    def rotateTo(self, theta):
        self.debugWrite(b"[rotateTo=" + str(theta).encode('ascii') + b"]")

    def rotate(self, theta):  
        self.debugWrite(b"[rotate=" + str(theta).encode('ascii') + b"]")

    def resetPosition(self, x=None, y=None, a=None):
        if x is not None:
            self.debugWrite(b"[setCommandX=" + str(x).encode('ascii') + b"]")
        if y is not None:
            self.debugWrite(b"[setCommandY=" + str(y).encode('ascii') + b"]")
        if a is not None:
            self.debugWrite(b"[setCommandA=" + str(a).encode('ascii') + b"]")
        self.debugWrite(b"[resetPosition=0]")
        print(self.port.readline())