##
##  VCU IEEE ROBOT 2018 - 2019
##  
##  accessory.py
##  Written by Xander Will / Mark Johnston
##
##  'Classes for the flag and the hatch'

from gpiozero import AngularServo

class Flag:
    """ Controls a wooden flag connected to a
        GPIO servo """
    def __init__(self):
        self.servoFlag = AngularServo(13, min_angle=-90, max_angle=90) 

    def raiseFlag(self):
        self.servoFlag.angle = 5

    def lowerFlag(self):
        self.servoFlag.angle = -5
    

class Hatch:
    def __init__(self):
        pass