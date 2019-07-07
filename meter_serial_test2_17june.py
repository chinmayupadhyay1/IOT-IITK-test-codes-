import pymodbus
import serial
from pymodbus.client.sync import ModbusSerialClient as ModbusClient

##import pymodbus
##import serial
##from pymodbus.pdu import ModbusRequest
##from pymodbus.client.sync import ModbusSerialClient as ModbusClient #initialize a serial RTU client instance
##from pymodbus.transaction import ModbusRtuFramer
client = ModbusClient(method='rtu', port='COM4', timeout=1, stopbits = 1, bytesize = 8,  parity='E', baudrate= 9600)
client.connect()
r = client.read_holding_registers(40101,2,unit=0x01)

#val=read.registers[float(40101)]
##request=request.raw()
#val=request.decode (byte_order=little, word_order=little, formatters=uint16)      
print(r)
#print(val)
client.close()
