import serial
import time
import struct

class BTPOWER:

	setAddrBytes 		=	[0xB4,0xC0,0xA8,0x01,0x01,0x00,0x1E]
	readVoltageBytes 	= 	[0xB0,0xC0,0xA8,0x01,0x01,0x00,0x1A]
	readCurrentBytes 	= 	[0XB1,0xC0,0xA8,0x01,0x01,0x00,0x1B]

def __init__(self, com="/dev/ttyUSB0", timeout=10.0):
		self.ser = serial.Serial
		(
			port=com4,
			baudrate=9600,
			parity=serial.PARITY_NONE,
			stopbits=serial.STOPBITS_ONE,
        		bytesize=serial.EIGHTBITS,
			timeout = timeout

		)
if self.ser.isOpen():
        self.ser.close()
        
self.ser.open()

def checkChecksum(self, _tuple):
    _list = list(_tuple)
    _checksum = _list[-1]
    _list.pop()
    _sum = sum(_list)
    if _checksum == _sum%256:
    return True
    else:
    raise Exception("Wrong checksum")

def isReady(self):
        self.ser.write(serial.to_bytes(self.setAddrBytes))
        rcv = self.ser.read(7)
	if len(rcv) == 7:
        	unpacked = struct.unpack("!7B", rcv)
        	if(self.checkChecksum(unpacked)):
        		return True

	else:
        	raise serial.SerialTimeoutException("Timeout setting address")

def readVoltage(self):
	self.ser.write(serial.to_bytes(self.readVoltageBytes))
	rcv = self.ser.read(7)
	if len(rcv) == 7:
		unpacked = struct.unpack("!7B", rcv)
		if(self.checkChecksum(unpacked)):
			tension = unpacked[2]+unpacked[3]/10.0
			return tension
	else:
        	raise serial.SerialTimeoutException("Timeout reading tension")

def readCurrent(self):
        self.ser.write(serial.to_bytes(self.readCurrentBytes))
        rcv = self.ser.read(7)
        if len(rcv) == 7:
		unpacked = struct.unpack("!7B", rcv)
		if(self.checkChecksum(unpacked)):
			current = unpacked[2]+unpacked[3]/100.0
			return current
	else:
		raise serial.SerialTimeoutException("Timeout reading current")

def close(self):
self.ser.close()


if __name__ == "__main__":
        try:
        	sensor = BTPOWER()
		print("Checking readiness")
		print(sensor.isReady())
		print("Reading voltage")
		voltage = sensor.readVoltage()
		print(type(voltage))
                print("Reading current")
		print(sensor.readCurrent())

finally:
	sensor.close()
