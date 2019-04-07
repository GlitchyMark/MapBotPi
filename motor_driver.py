import serial

from serial_cfg import *

class MotorDriverInterface:
    def __init__(self):
        self.port = serial.Serial(MOTOR_DRIVER_PORT, BAUD_RATE)
        self.setMotionAllowed()

    def setMotionAllowed(self):
        self.port.write("[setMotionAllowed=0]")

    def stop(self):
        self.port.write("[stop=0]")

    def setTargetVelocities(self, x=None, y=None, a=None):
        if x is not None:
            self.port.write("[setCommandX=" + str(x) + "]")
        if y is not None:
            self.port.write("[setCommandY=" + str(y) + "]")
        if a is not None:
            self.port.write("[setCommandA=" + str(a) + "]")
        self.port.write("[setTargetVelocities=0]")  

    def setMaxVelocities(self, x=None, y=None, a=None):
        if x is not None:
            self.port.write("[setCommandX=" + str(x) + "]")
        if y is not None:
            self.port.write("[setCommandY=" + str(y) + "]")
        if a is not None:
            self.port.write("[setCommandA=" + str(a) + "]")
        self.port.write("[setMaxVelocities=0]") 
        
    def setMaxAccelerations(self, x=None, y=None, a=None):
        if x is not None:
            self.port.write("[setCommandX=" + str(x) + "]")
        if y is not None:
            self.port.write("[setCommandY=" + str(y) + "]")
        if a is not None:
            self.port.write("[setCommandA=" + str(a) + "]")
        self.port.write("[setMaxAccelerations=0]")     

    def setMicrostepping(self, step):
        self.port.write("[setMicrostepping=" + str(step & 0xFF) + "]")

    def gotoXYA(self, x=None, y=None, a=None):
        if x is not None:
            self.port.write("[setCommandX=" + str(x) + "]")
        if y is not None:
            self.port.write("[setCommandY=" + str(y) + "]")
        if a is not None:
            self.port.write("[setCommandA=" + str(a) + "]")
        self.port.write("[gotoXYA=0]")

    def gotoXY(self, x=None, y=None, a=None):
        if x is not None:
            self.port.write("[setCommandX=" + str(x) + "]")
        if y is not None:
            self.port.write("[setCommandY=" + str(y) + "]")
        self.port.write("[gotoXY=0]")  

    def moveFR(self, f=None, r=None):
        if f is not None:
            self.port.write("[setCommandX=" + str(f) + "]")
        if r is not None:
            self.port.write("[setCommandY=" + str(r) + "]")
        self.port.write("[moveFR=0.000]")

    def rotateTo(self, theta):
        self.port.write("[rotateTo=" + str(theta) + "]")

    def rotate(self, theta):  
        self.port.write("[rotate=" + str(theta) + "]") 

    def resetPosition(self, x=None, y=None, a=None):
        if x is not None:
            self.port.write("[setCommandX=" + str(x) + "]")
        if y is not None:
            self.port.write("[setCommandY=" + str(y) + "]")
        if a is not None:
            self.port.write("[setCommandA=" + str(a) + "]")
        self.port.write("[resetPosition=0]")
        print(self.port.readline())