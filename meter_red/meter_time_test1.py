import time
import socket
import datetime
import numpy
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from bitstring import BitArray
host="192.168.1.42" #server ip address
port=5002 #server host
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def sign (RBdash):
        signdash=RBdash[0]
        return int(signdash)

def expo (RBdash):
        exp=RBdash[1:9]
        expdash = BitArray(bin=exp)
        expdashdash=(expdash.uint)
        return int(expdashdash)
	

def mant (RBdash):
        mant=RBdash[9:32]
        mantdash="1."+mant
        mantdashdash = binaryToDecimal(mantdash, len(mantdash))
        return float(mantdashdash)

def binaryToDecimal(binary, length) :
        point = binary.find('.')  
        if (point == -1) : 
                point = length  
  
        intDecimal = 0
        fracDecimal = 0
        twos = 1

        for i in range(point-1, -1, -1):
                intDecimal += ((ord(binary[i]) - ord('0')) * twos)  
                twos *= 2  

        twos = 2
      
        for i in range(point + 1, length): 
                fracDecimal += ((ord(binary[i]) - ord('0')) / twos);  
                twos *= 2.0
    
        ans = intDecimal + fracDecimal 
        return (ans)

def calc (x,y,z):
        res=pow((-1),x) * pow(2,(y-127)) * z
        return res

client = ModbusClient(method = 'rtu', port='/dev/ttyUSB0', timeout=1, stopbit=1, bytesize=8, parity='E', baudrate=9600)
client.connect()


while True:
    
        AllReg=client.read_holding_registers(0x64 , 0x70,unit=1)
        #print(AllReg.registers)
        #time.sleep(0.5)
        

        #ActivePower
        firstActP=(AllReg.registers[1])
        secondActP=(AllReg.registers[0])

        R0=str(format(firstActP, '016b'))
        R1=str(format(secondActP, '016b'))
        RB=R0+R1

        S=sign(RB)
        E=expo(RB)
        M=mant(RB)

        finalActP=calc(S,E,M)

        #Voltage
        firstVol=(AllReg.registers[41])
        secondVol=(AllReg.registers[40])

        R0=str(format(firstVol, '016b'))
        R1=str(format(secondVol, '016b'))
        RB=R0+R1

        S=sign(RB)
        E=expo(RB)
        M=mant(RB)

        finalVoltage=calc(S,E,M)

        #Current
        firstCur=(AllReg.registers[49])
        secondCur=(AllReg.registers[48])

        R0=str(format(firstCur, '016b'))
        R1=str(format(secondCur, '016b'))
        RB=R0+R1

        S=sign(RB)
        E=expo(RB)
        M=mant(RB)

        finalCurrent=calc(S,E,M)

        #Frequency
        firstFre=(AllReg.registers[57])
        secondFre=(AllReg.registers[56])

        R0=str(format(firstFre, '016b'))
        R1=str(format(secondFre, '016b'))
        RB=R0+R1

        S=sign(RB)
        E=expo(RB)
        M=mant(RB)

        finalFrequency=calc(S,E,M)

        #ApparentPower
        firstAptP=(AllReg.registers[25])
        secondAptP=(AllReg.registers[24])

        R0=str(format(firstAptP, '016b'))
        R1=str(format(secondAptP, '016b'))
        RB=R0+R1

        S=sign(RB)
        E=expo(RB)
        M=mant(RB)

        finalAptP=calc(S,E,M)

        #kW hour
        firstWh=(AllReg.registers[59])
        secondWh=(AllReg.registers[58])

        R0=str(format(firstWh, '016b'))
        R1=str(format(secondWh, '016b'))
        RB=R0+R1

        S=sign(RB)
        E=expo(RB)
        M=mant(RB)

        finalWattHour=calc(S,E,M)

        #Power Factor
        firstpf=(AllReg.registers[17])
        secondpf=(AllReg.registers[16])

        R0=str(format(firstpf, '016b'))
        R1=str(format(secondpf, '016b'))
        RB=R0+R1

        S=sign(RB)
        E=expo(RB)
        M=mant(RB)

        finalpowerfactor=calc(S,E,M)

        #DateTime
        #time=str(datetime.datetime.now())
        

        #PrintData
        #print("Date & Time: "+(time)+"\n")
        print("Active Power is " +str(round(finalActP,2))+ " Watts\n")
        print("Voltage is " + str(round(finalVoltage,2))+ " volts\n")
        print("Current is " + str(round(finalCurrent,2)) + " Amps\n")
        print("Frequency is " + str(round(finalFrequency,2))+ " Hertz\n")
        print("Apparent Power is " + str(round(finalAptP,2)) + " Watts\n")
        print("Energy is " +str(round((finalWattHour/1000),2)) + " kW-Hours\n")
        print("Power Factor is " + str((finalpowerfactor)) + "\n")
        print("---------------------------------------\n")

      
        
        s="Active Power = "+str(finalActP)+"Watts"
        s=s.encode()
        sock.sendto(s,(host,port))
        s="Voltage = "+str(finalVoltage)+"Volts"
        s=s.encode()
        sock.sendto(s,(host,port))
        s="Current = "+str(finalCurrent)+"Amps"
        s=s.encode()
        sock.sendto(s,(host,port))
        s="Frequency = "+str(finalFrequency)+"Hertz"
        s=s.encode()
        sock.sendto(s,(host,port))
        s="Apparent Power = "+str(finalAptP)+"Watts"
        s=s.encode()
        sock.sendto(s,(host,port))
        s="Energy = "+str(finalWattHour)+"W-Hour"
        s=s.encode()
        sock.sendto(s,(host,port))
        s="Power Factor = "+str(finalpowerfactor)
        s=s.encode()
        sock.sendto(s,(host,port))
        s="-------------------------------------------"
        s=s.encode()
        sock.sendto(s,(host,port))

