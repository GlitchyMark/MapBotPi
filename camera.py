import serial
import json

class Camera:
    def __init__(self, address, baud):
        self.port = serial.Serial(address, baud)

    def getData(self):
        return json.loads(self.port.readline())