import serial

class Camera():
    """ Handles communication with the OpenMV """
    def __init__(self, address, baud, debug=False):
        self.port = serial.Serial(address, baud)
        self.debug = debug 

    def flush(self):
        self.port.flush()

    def getData(self):
        while True:
            try:
                return json.loads(self.port.readline())
            except:
                continue

home_lookup = {
        "YELLOW"    :   "RED",
        "RED"       :   "GREEN",
        "GREEN"     :   "BLUE",
        "BLUE"      :   "YELLOW"
    }
def FindHomeBase(cam):
    cam.flush()
    data = cam.getData()
    return home_lookup.get(data.get("color"))

before_home_lookup = {
        "YELLOW"    :   "BLUE",
        "RED"       :   "YELLOW",
        "GREEN"     :   "RED",
        "BLUE"      :   "GREEN"
    }
def ReturnToHome(cam, home_color):
    cam.flush()
    data = cam.getData()
    next_color = before_home_lookup.get(data.get("color"))
    if next_color == home_color:
        # go straight here
        # or whatever
        pass
