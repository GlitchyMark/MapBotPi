import serial

from serial_cfg import *

class MotorDriverInterface:
    def __init__(self):
        self.port = serial.Serial(MOTOR_DRIVER_PORT, BAUD_RATE)
        self.setMotionAllowed(True)
        self.setTargetVelocities(10, 10)

    def __del__(self):
        self.setMotionAllowed(False)

    def debugWrite(self, s):
        self.debugWrite(s)
        print(s)

    def setMotionAllowed(self, value):
        if value is True:
            self.debugWrite("[setMotionAllowed=1]")
        else:
            self.debugWrite("[setMotionAllowed=0]")

    def stop(self):
        self.debugWrite("[stop=0]")

    def setTargetVelocities(self, x=None, y=None, a=None):
        if x is not None:
            self.debugWrite("[setCommandX=" + str(x) + "]")
        if y is not None:
            self.debugWrite("[setCommandY=" + str(y) + "]")
        if a is not None:
            self.debugWrite("[setCommandA=" + str(a) + "]")
        self.debugWrite("[setTargetVelocities=0]")  

    def setMaxVelocities(self, x=None, y=None, a=None):
        if x is not None:
            self.debugWrite("[setCommandX=" + str(x) + "]")
        if y is not None:
            self.debugWrite("[setCommandY=" + str(y) + "]")
        if a is not None:
            self.debugWrite("[setCommandA=" + str(a) + "]")
        self.debugWrite("[setMaxVelocities=0]") 
        
    def setMaxAccelerations(self, x=None, y=None, a=None):
        if x is not None:
            self.debugWrite("[setCommandX=" + str(x) + "]")
        if y is not None:
            self.debugWrite("[setCommandY=" + str(y) + "]")
        if a is not None:
            self.debugWrite("[setCommandA=" + str(a) + "]")
        self.debugWrite("[setMaxAccelerations=0]")     

    def setMicrostepping(self, step):
        self.debugWrite("[setMicrostepping=" + str(step & 0xFF) + "]")

    def gotoXYA(self, x=None, y=None, a=None):
        if x is not None:
            self.debugWrite("[setCommandX=" + str(x) + "]")
        if y is not None:
            self.debugWrite("[setCommandY=" + str(y) + "]")
        if a is not None:
            self.debugWrite("[setCommandA=" + str(a) + "]")
        self.debugWrite("[gotoXYA=0]")

    def gotoXY(self, x=None, y=None, a=None):
        if x is not None:
            self.debugWrite("[setCommandX=" + str(x) + "]")
        if y is not None:
            self.debugWrite("[setCommandY=" + str(y) + "]")
        self.debugWrite("[gotoXY=0]")  

    def moveFR(self, f=None, r=None):
        if f is not None:
            self.debugWrite("[setCommandX=" + str(f) + "]")
        if r is not None:
            self.debugWrite("[setCommandY=" + str(r) + "]")
        self.debugWrite("[moveFR=0]")

    def rotateTo(self, theta):
        self.debugWrite("[rotateTo=" + str(theta) + "]")

    def rotate(self, theta):  
        self.debugWrite("[rotate=" + str(theta) + "]") 

    def resetPosition(self, x=None, y=None, a=None):
        if x is not None:
            self.debugWrite("[setCommandX=" + str(x) + "]")
        if y is not None:
            self.debugWrite("[setCommandY=" + str(y) + "]")
        if a is not None:
            self.debugWrite("[setCommandA=" + str(a) + "]")
        self.debugWrite("[resetPosition=0]")
        print(self.port.readline())