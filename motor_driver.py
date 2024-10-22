##
##  VCU IEEE ROBOT 2018 - 2019
##  
##  motor_driver.py
##  Written by Xander Will
##
##  'interface for 2017 motor driver'

import serial
import time
import json

class MotorDriverInterface:
    """ Interface for talking to the
        motor driver, each method wraps
        a set of commands """

    def __init__(self, address, baud, debug=False):
        self.port = serial.Serial(address, baud)
        self.debug = debug

        self.write(b"[setCommandX=0]")
        self.write(b"[setCommandY=0]")
        self.write(b"[setCommandA=0]")
        self.setMotionAllowed(True)
        self.setMotionAllowed(True)
        self.setMaxVelocities(x=5, a=5)
        self.setMaxAccelerations(x=1.5, a=1.5)

    def __del__(self):
        self.setMotionAllowed(False)

    def read(self):
        while True:
            try:
                return self.port.readline().decode()
            except:
                continue

    def findMCC(self, string):
        commands = string.split("[")
        for command in commands:
            if command[0:18] == "motionCommandCount":
                return float(command.split("=")[1].split("]")[0])

    def write(self, s):
        old_cmd_cnt = self.findMCC(self.read())
        while True:
            self.port.write(s)
            if self.debug == True:
                print(s)
            time.sleep(0.001)
            try:
                new_cmd_cnt = self.findMCC(self.read())
                if old_cmd_cnt < new_cmd_cnt:
                    return   # function exit
                if self.debug == True:
                    print("Message failed, sending again")
            except:
                continue

    def setMotionAllowed(self, value):
        if value is True:
            self.port.write(b"[setMotionAllowed=1]")
        else:
            self.port.write(b"[setMotionAllowed=0]")

    def stop(self):
        self.write(b"[stop=1]")

    def setTargetVelocities(self, x=None, y=None, a=None):
        if x is not None:
            self.write(b"[setCommandX=" + str(x).encode('ascii') + b"]")
        if y is not None:
            self.write(b"[setCommandY=" + str(y).encode('ascii') + b"]")
        if a is not None:
            self.write(b"[setCommandA=" + str(a).encode('ascii') + b"]")
        self.write(b"[setTargetVelocities=1]")

    def setMaxVelocities(self, x=None, y=None, a=None):
        if x is not None:
            self.write(b"[setCommandX=" + str(x).encode('ascii') + b"]")
        if y is not None:
            self.write(b"[setCommandY=" + str(y).encode('ascii') + b"]")
        if a is not None:
            self.write(b"[setCommandA=" + str(a).encode('ascii') + b"]")
        self.write(b"[setMaxVelocities=1]")
        
    def setMaxAccelerations(self, x=None, y=None, a=None):
        if x is not None:
            self.write(b"[setCommandX=" + str(x).encode('ascii') + b"]")
        if y is not None:
            self.write(b"[setCommandY=" + str(y).encode('ascii') + b"]")
        if a is not None:
            self.write(b"[setCommandA=" + str(a).encode('ascii') + b"]")
        self.write(b"[setMaxAccelerations=1]")

    def setMicrostepping(self, step):
        self.write(b"[setMicrostepping=" + str(step & 0xFF) + b"]")

    def gotoXYA(self, x=None, y=None, a=None):
        if x is not None:
            self.write(b"[setCommandX=" + str(x).encode('ascii') + b"]")
        if y is not None:
            self.write(b"[setCommandY=" + str(y).encode('ascii') + b"]")
        if a is not None:
            self.write(b"[setCommandA=" + str(a).encode('ascii') + b"]")
        self.write(b"[gotoXYA=1]")

    def gotoXY(self, x=None, y=None):
        if x is not None:
            self.write(b"[setCommandX=" + str(x).encode('ascii') + b"]")
        if y is not None:
            self.write(b"[setCommandY=" + str(y).encode('ascii') + b"]")
        self.write(b"[gotoXY=1]")

    def moveFR(self, f=None, r=None):
        if f is not None:
            self.write(b"[setCommandX=" + str(f).encode('ascii') + b"]")
        if r is not None:
            self.write(b"[setCommandY=" + str(r).encode('ascii') + b"]")
        self.write(b"[moveFR=0]")

    def rotateTo(self, theta):
        self.write(b"[rotateTo=" + str(theta).encode('ascii') + b"]")

    def rotate(self, theta):  
        self.write(b"[rotate=" + str(theta).encode('ascii') + b"]")

    def resetPosition(self, x=None, y=None, a=None):
        if x is not None:
            self.write(b"[setCommandX=" + str(x).encode('ascii') + b"]")
        if y is not None:
            self.write(b"[setCommandY=" + str(y).encode('ascii') + b"]")
        if a is not None:
            self.write(b"[setCommandA=" + str(a).encode('ascii') + b"]")
        self.write(b"[resetPosition=0]")