import serial
import json

from logic import State, StateBuffer, GameLogic
from mapping import Mapper
from motor_driver import MotorDriverInterface

from serial_cfg import MV_PORT, BAUD_RATE

class Robot:
    def __init__(self):
        self.mv = serial.Serial(MV_PORT, BAUD_RATE)

        self.motor_driver = MotorDriverInterface()
        self.logic = GameLogic(self)
        self.mapper = Mapper()
        self.state_buffer = StateBuffer()

        self.state_buffer = list()
        self.logic.startUp()

    def run(self):
        self.updatePosition()
        self.updateState()
        self.execute()

    def updatePosition(self):
        self.mv.write("s")
        self.mv_data = json.loads(self.mv.readline())
        self.telemetry = self.motor_driver.getTelemetry()

        self.xpos, self.ypos = self.telemetry["xpos"], self.telemetry["ypos"]
        for obj in self.mv_data:
            if obj["pole"] is True:
                theta = self.telemetry["angle"] - obj["angle"]
                self.xpos, self.ypos = self.mapper.getCurrPosFromPole(obj["color"], theta, obj["distance"])
 
    def updateState(self):
        txpos = self.state_buffer.current_state.targetXpos
        typos = self.state_buffer.current_state.targetYpos
        prev_func = self.state_buffer.current_state.func
        func = self.state_buffer.current_state.next_func
        self.state_buffer.addState(State(self.xpos, self.ypos, txpos, typos, self.telemetry["angle"], func, prev_func))

    def execute(self):
        self.state_buffer.current_state.func()

