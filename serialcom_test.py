import serial
ser1 = serial.Serial('COM6', 9600)
ser1.write('s'.encode())
