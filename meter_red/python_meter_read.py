import time
from pymodbus.client.sync import ModbusSerialClient as ModbusClient

client = ModbusClient(method = 'rtu', port='/dev/ttyUSB0', timeout=1, stopbit=1, bytesize=8, parity='E', baudrate=9600)
client.connect()

r=client.read_holding_registers(0x9e, 0x02,unit=1)
print (r.registers)
#print(float(r.registers[1])/10)
