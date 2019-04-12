##
##  VCU IEEE ROBOT 2018 - 2019
##  
##  accessory.py
##  Written by Xander Will
##
##  'Classes for the flag and the hatch'
from gpiozero import Servo

class Flag:
    servoFlag = AngularServo(13, min_agle=-90, max_angle=90)
    def __init__(self):
        pass 
    def raiseFlag():
        servoFlag.angle = 5
    def lowerFlag():
        servoFlag.angle = -5
    

class Hatch:
    def __init__(self):
        pass