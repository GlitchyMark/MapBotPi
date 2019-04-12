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
    try:
        while True:
            if len(sys.argv) > 1 and sys.argv[1] == "debug":
                r.logic.debug((sys.argv[2], sys.argv[3]))
            else:
                r.run()
    except KeyboardInterrupt:
        r.motor_driver.setMotionAllowed(False)
        exit()  

if __name__ == "__main__":
    start_button.when_pressed = main
    while True:
        pass