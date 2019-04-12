##
##  VCU IEEE ROBOT 2018 - 2019
##  
##  camera.py
##  Written by Xander Will / Akib Rhaat
##
##  'Handles data communication with OpenMV camera'

import serial
import json

class Camera:
    """ Handles communication with the OpenMV """

    def __init__(self, address, baud):
        self.port = serial.Serial(address, baud)

    def getData(self):
        return json.loads(self.port.readline().rstrip().replace("'",'"'))