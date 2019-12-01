import serial

def set_dev(): # return serial data what raspberry connect with arduino
	try:
		ser = serial.Serial('/dev/ttyACM0',9600)
		ser.flushInput()
		return ser
	except:
		ser = serial.Serial('/dev/ttyACM1',9600)
		ser.flushInput()
	return ser


def get_data(ser): # return sensor data
	line = ser.readline().decode()
	line = line.replace('\n','')
	data = line.split(',')
	print(data)
	return data
