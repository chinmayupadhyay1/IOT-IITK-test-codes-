import serial

ser1 = serial.Serial('COM4', 9600)

def led_on():
    ser1.write('1')

def led_off():
    ser1.write('0')

t=0
while(t<2000):
    if(t%10 == 0):
        print(t)
    t+=1

led_on()
