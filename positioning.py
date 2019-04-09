##
##  VCU IEEE ROBOT 2018 - 2019
##  
##  positioning.py
##  Written by Xander Will
##
##  'Wrappers for various C accessory drivers'


from ctypes import CDLL

class Accelerometer:
    """ Wrapper for Jamie's accelerometer
        driver """

    def __init__(self):
        pass
        #self.accel_lib = CDLL("something.so") #TODO: UNCOMMENT
        #self.accel_lib.init()

    def getAcceleration(self):
        return self.accel_lib.getAcceleration()

# possible additions
class Gyroscope:
    def __init__(self):
        pass

class Magnetometer:
    def __init__(self):
        pass