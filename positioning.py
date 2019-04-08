from ctypes import CDLL

class Accelerometer:
    def __init__(self):
        self.accel_lib = CDLL("something.so")
        self.accel_lib.init()

    def getAcceleration(self):
        return self.accel_lib.getAcceleration()

# possible additions
class Gyroscope:
    def __init__(self):
        pass

class Magnetometer:
    def __init__(self):
        pass