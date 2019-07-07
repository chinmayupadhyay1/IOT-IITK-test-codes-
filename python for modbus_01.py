import struct
import pymodbus.client.sync
import binascii
import time
import sys

def read_float_reg(client, basereg, unit=1) :
    resp = client.read_input_registers(basereg,2, unit=1)
    if resp == None :
        return None
    # according to spec, each pair of registers returned
    # encodes a IEEE754 float where the first register carries
    # the most significant 16 bits, the second register carries the 
    # least significant 16 bits.
    return struct.unpack('>f',struct.pack('>HH',*resp.registers))



cl = pymodbus.client.sync.ModbusSerialClient('rtu',port='/dev/ttyUSB0', baudrate=9600, parity='N',stopbits=2,timeout=0.125)
values = read_float_reg(cl, 0x40125, unit=1)
print (values)
