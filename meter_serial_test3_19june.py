import time
import pymodbus
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
client = ModbusClient(method='rtu', port='COM4', timeout=1, stopbits = 1, bytesize = 8,  parity='E', baudrate= 9600)
client.connect()
while True:
    r = client.read_holding_registers(40101,40157,unit=1)
    print (int(r.1625621642)/10.0)
