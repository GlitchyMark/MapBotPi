##
##  VCU IEEE ROBOT 2018 - 2019
##  
##  main.py
##  Written by Xander Will
##
##  'Main loop + terminal argument handling'

import sys

import robot

from gpiozero import Button

start_button = Button(19, pull_up=False)
r = robot.Robot()

if len(sys.argv) > 1 and sys.argv[1] == "shutdown":
    r.motor_driver.setMotionAllowed(False)
    exit()

def main():
    while True:
        if len(sys.argv) > 1 and sys.argv[1] == "debug":
            if len(sys.argv) > 3:
                r.motor_driver.setTargetVelocities(sys.argv[2], sys.argv[3])
            r.logic.debug()
            print(r.motor_driver.port.readline())
        else:
            r.run()    

if __name__ == "__main__":
    start_button.when_pressed = main
    while True:
        pass