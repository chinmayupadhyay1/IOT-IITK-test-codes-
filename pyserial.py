import serial

arduino = serial.Serial('COM4', 9600)
while True:
	data = arduino.readline() #the last bit gets rid of the new-line chars
	if data:
		print(data)
