import serial

from serial_cfg import MOTOR_DRIVER_PORT, BAUD_RATE

class MotorDriverInterface:
    def __init__(self):
        self.port = serial.Serial(MOTOR_DRIVER_PORT, BAUD_RATE)
        self.setMotionAllowed(True)
        self.setTargetVelocities(5, 5, 5)
        self.setMaxVelocities(10, 10, 10)
        self.setMaxAccelerations(5, 5, 5)

    def __del__(self):
        self.setMotionAllowed(False)

    def debugWrite(self, s):
        self.port.write(s)
        print(s)

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