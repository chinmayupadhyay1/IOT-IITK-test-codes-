import pymodbus
import serial
from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusSerialClient as ModbusClient 
from pymodbus.transaction import ModbusRtuFramer

import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

client= ModbusClient(method = "rtu", port="/dev/ttyUSB2", stopbits = 1, bytesize = 8, parity = 'E' ,baudrate= 9600)
connection = client.connect()

print (connection)

result= client.read_holding_registers(40101,1,unit=1)
print(result)

client.close()
