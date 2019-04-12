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
        self.setMaxVelocities(5, 5)
        self.setMaxAccelerations(1.5, 1.5)

    def __del__(self):
        self.setMotionAllowed(False)

    #   [motionCommandCount=[0-9]+]
    def getTelemetry(self):
        return json.loads(self.port.readline().decode())

    def findMCC(self, string):
        commands = string.split("[")
        for command in commands:
            if command[0:18] == "motionCommandCount":
                return int(command.split("=")[1].split("]")[0])

    def write(self, s):
        old_cmd_cnt = self.findMCC(self.getTelemetry())
        while True:
            self.port.write(s)
            if self.debug == True:
                print(s)
            time.sleep(3)
            new_cmd_cnt = self.findMCC(self.getTelemetry())
            if old_cmd_cnt < new_cmd_cnt:
                return   # function exit
            if self.debug == True:
                print("Message failed, sending again")

    def setMotionAllowed(self, value):
        if value is True:
            self.write(b"[setMotionAllowed=1]")
        else:
            self.write(b"[setMotionAllowed=0]")

    def stop(self):
        self.write(b"[stop=1]")

    def setTargetVelocities(self, x=None, y=None, a=None): #Use this one, sets the velocity the driver will get to
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

    def gotoXYA(self, x=None, y=None, a=None): #Broken for whatever reason.
        if x is not None:
            self.write(b"[setCommandX=" + str(x).encode('ascii') + b"]")
        if y is not None:
            self.write(b"[setCommandY=" + str(y).encode('ascii') + b"]")
        if a is not None:
            self.write(b"[setCommandA=" + str(a).encode('ascii') + b"]")
        self.write(b"[gotoXYA=1]")

    def gotoXY(self, x=None, y=None): #Don't use
        if x is not None:
            self.write(b"[setCommandX=" + str(x).encode('ascii') + b"]")
        if y is not None:
            self.write(b"[setCommandY=" + str(y).encode('ascii') + b"]")
        self.write(b"[gotoXY=1]")

    def moveFR(self, f=None, r=None): #Only goes forward
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
        print(self.port.readline())