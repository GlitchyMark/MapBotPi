import sys

import robot

from gpiozero import Button

start_button = Button(17)    # update with pin number
r = robot.Robot()

if len(sys.argv) > 1 and sys.argv[1] == "shutdown":
    r.motor_driver.setMotionAllowed(False)
    exit()

def main():
    while True:
        if len(sys.argv) > 1 and sys.argv[1] == "debug":
            r.logic.debug()
            # print(r.motor_driver.port.readline())
        else:
            r.run()    

if __name__ == "__main__":
    start_button.when_pressed = main