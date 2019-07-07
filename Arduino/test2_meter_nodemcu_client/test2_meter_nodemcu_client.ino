#include<ModbusMaster.h>
#include<ESP8266WiFi.h>
#include<WiFiUdp.h>

WiFiUDP Udp;

#define MAX485_DE     3
#define MAX485_RE_NEG 2

String ssid = "SmartCity";
String password= "69366938";
int remote_port = 5002;

ModbusMaster node;


void setup() 
{
 Serial.begin(9600);    
 WiFi.begin(ssid ,password);
 Serial.print("connecting");

 while(WiFi.status()!= WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
 Serial.println("WiFi connected");
 Serial.print("NodeMCU IP Address");
 Serial.println(WiFi.localIP());  

 pinMode(MAX485_RE_NEG,OUTPUT); 
 pinMode(MAX485_DE, OUTPUT);

 digitalWrite(MAX485_RE_NEG, 0);
 digitalWrite(MAX485_DE, 0);

 node.begin(1, Serial);

 node.preTransmission(preTransmission);
 node.postTransmission(postTransmission);
 Udp.beginPacket("192.168.1.47",remote_port);
}

void loop()
{
 uint8_t resultMain;
 resultMain = node.readInputRegisters(0x40101,56);
 if (resultMain == node.ku8MBSuccess)
  {
    Udp.write("Voltage");
    Udp.write(node.getResponseBuffer(0x40125));
    Udp.write("Current");
    Udp.write(node.getResponseBuffer(0x40149)); 
    Udp.endPacket();    
  }
 delay(500);
}


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
