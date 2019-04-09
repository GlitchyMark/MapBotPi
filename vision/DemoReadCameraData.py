import serial
import json
import thread
ser = serial.Serial('/dev/ttyACM0', 115200)
	
while 1:
	z = json.loads(ser.readline().rstrip().replace("'",'"'))
	print(z["Red_Pole_Distance"])