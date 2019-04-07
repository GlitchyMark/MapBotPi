import sys

import robot

from gpiozero import Button

start_button = Button(1)    # update with pin number
r = robot.Robot()

def main():
    while True:
        if len(sys.argv) > 1 and sys.argv[1] == "debug":
            r.logic.debug()
        else:
            r.run()


if __name__ == "__main__":
    start_button.when_pressed = main