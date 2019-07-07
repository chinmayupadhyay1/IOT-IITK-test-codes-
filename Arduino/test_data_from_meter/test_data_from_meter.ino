#include <ModbusMaster.h>

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
Serial.begin(9600);
Serial.println("------");
node.begin(1, Serial);

node.preTransmission(preTransmission);
node.postTransmission(postTransmission);
}

void loop()
{
uint8_t resultMain;
resultMain=node.readInputRegisters(0x40101, 56);
if (resultMain == node.ku8MBSuccess)
{
Serial.println("------");
Serial.print("Voltage: ");
Serial.println(node.getResponseBuffer(0x40125) / 100.0f);
Serial.print("Current: ");
Serial.println(node.getResponseBuffer(0x40149) / 100.0f);
}
delay(1000);
}
