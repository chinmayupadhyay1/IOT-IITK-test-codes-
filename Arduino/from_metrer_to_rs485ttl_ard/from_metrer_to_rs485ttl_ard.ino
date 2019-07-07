#include<ModbusMaster.h>
#include <RS485.h>
#include <SoftwareSerial.h>

#define MAX485_DE     3
#define MAX485_RE_NEG 2

ModbusMaster node;

void preTransmission()
{
  digitalWrite(MAX485_RE_NEG, 1);
  digitalWrite(MAX485_DE, 1);
}

void postTransmission()
{
  digitalWrite(MAX485_RE_NEG, 0);
  digitalWrite(MAX485_DE, 0);
}

void setup() 
{
 pinMode(MAX485_RE_NEG,OUTPUT); 
 pinMode(MAX485_DE, OUTPUT);

 digitalWrite(MAX485_RE_NEG, 0);
 digitalWrite(MAX485_DE, 0);

 Serial.begin(9600);
 node.begin(1, Serial);

 node.preTransmission(preTransmission);
 node.postTransmission(postTransmission);
 
 uint8_t resultMain;
 resultMain = node.readInputRegisters(0x40101,56);
 Serial.println(node.getResponseBuffer(0x40125),HEX);
// if (resultMain == node.ku8MBSuccess)
// {
//  Serial.println("......");
//  Serial.print(Udp.write("Voltage"););
//  Serial.println(node.getResponseBuffer(0x40125));
//  Serial.print("Current: ");
//  Serial.println(node.getResponseBuffer(0x40149));
// }
 
}

void loop()
{

}
