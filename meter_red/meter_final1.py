import time
import numpy
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from bitstring import BitArray

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
        ActP=client.read_holding_registers(0x64, 0x02,unit=1)
##      print ((ActP.registers))
        time.sleep(1)
    
        Voltage=client.read_holding_registers(0x8c, 0x02,unit=1)
        #print (Voltage.registers)
        time.sleep(1)
##
        Current=client.read_holding_registers(0x94, 0x02,unit=1)
        #print (Current.registers)
        time.sleep(1)
##
        Frequency=client.read_holding_registers(0x9c, 0x02,unit=1)
        #print (Frequency.registers)
        time.sleep(1)
##
        AptP=client.read_holding_registers(0x7c, 0x02,unit=1)
        #print (AptP.registers)
        time.sleep(1)
##
        Wh=client.read_holding_registers(0x9e, 0x02,unit=1)
        #print (Wh.registers)
        time.sleep(1)

        PF=client.read_holding_registers(0x74 , 0x02,unit=1)
        #print (PF.registers)
        time.sleep(1)


#    #ActivePower
        firstActP=(ActP.registers[1])
        secondActP=(ActP.registers[0])

        R0=str(format(firstActP, '016b'))
        R1=str(format(secondActP, '016b'))
        RB=R0+R1

        S=sign(RB)
        E=expo(RB)
        M=mant(RB)

        finalActP=calc(S,E,M)


   
##    #Voltage
        firstVol=(Voltage.registers[1])
        secondVol=(Voltage.registers[0])

        R0=str(format(firstVol, '016b'))
        R1=str(format(secondVol, '016b'))
        RB=R0+R1

        S=sign(RB)
        E=expo(RB)
        M=mant(RB)

        finalVoltage=calc(S,E,M)

        
      #Current
        firstCur=(Current.registers[1])
        secondCur=(Current.registers[0])

        R0=str(format(firstCur, '016b'))
        R1=str(format(secondCur, '016b'))
        RB=R0+R1

        S=sign(RB)
        E=expo(RB)
        M=mant(RB)

        finalCurrent=calc(S,E,M)
##
##
##    #Frequency
        firstFre=(Frequency.registers[1])
        secondFre=(Frequency.registers[0])

        R0=str(format(firstFre, '016b'))
        R1=str(format(secondFre, '016b'))
        RB=R0+R1

        S=sign(RB)
        E=expo(RB)
        M=mant(RB)

        finalFrequency=calc(S,E,M)

##
##    #ApparentPower
        firstAptP=(AptP.registers[1])
        secondAptP=(AptP.registers[0])

        R0=str(format(firstAptP, '016b'))
        R1=str(format(secondAptP, '016b'))
        RB=R0+R1

        S=sign(RB)
        E=expo(RB)
        M=mant(RB)

        finalAptP=calc(S,E,M)

##
##    #kW hour
        firstWh=(Wh.registers[1])
        secondWh=(Wh.registers[0])

        R0=str(format(firstWh, '016b'))
        R1=str(format(secondWh, '016b'))
        RB=R0+R1

        S=sign(RB)
        E=expo(RB)
        M=mant(RB)

        finalWattHour=calc(S,E,M)

        #Power Factor
        firstpf=(PF.registers[1])
        secondpf=(PF.registers[0])

        R0=str(format(firstpf, '016b'))
        R1=str(format(secondpf, '016b'))
        RB=R0+R1

        S=sign(RB)
        E=expo(RB)
        M=mant(RB)

        finalpowerfactor=calc(S,E,M)
##
##
##    #PrintData
        print("Active Power is " +str(round(finalActP,2))+ " Watts\n")
        print("Voltage is " + str(round(finalVoltage,2))+ " volts\n")
        print("Current is " + str(round(finalCurrent,2)) + " Amps\n")
        print("Frequency is " + str(round(finalFrequency,2))+ " Hertz\n")
        print("Apparent Power is " + str(round(finalAptP,2)) + " Watts\n")
        print("Energy is " +str(round((finalWattHour/1000),2)) + " kW-Hours\n")
        print("Power Factor is " + str((finalpowerfactor)) + "\n")
## 
